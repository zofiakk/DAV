import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from utils import parse_args, load_data
from statsmodels.tsa.api import AutoReg
import warnings
warnings.filterwarnings("ignore")

def main():
    """Call all of the necessary functions
    """
    _, data = load_data()
    args = parse_args()
    for count in ["Japan", "Ukraine", "Poland"]:
        get_ar_model(data, count, save=args.display)
    

def get_ar_model(data:pd.DataFrame, country:str, save:bool):
    """Function creating AR model and using it to
    forecast temperatures in the next 250 years

    :param data: Temperatures data
    :type data: pd.DataFrame
    :param country: Country for which the
    model should be made
    :type country: str
    :param save: Whether to save the plot or display it
    :type save: bool
    """
    sns.set_theme()
    sns.set_style("darkgrid")
    plt.figure(figsize=(14, 8))
    
    # Choose the data
    data = data[data.Country == country]
    data = data[['year','AverageTemperatureCelsius']]
    max_year = max(data.year.to_list())
    
    # Create the model
    res = AutoReg(data.AverageTemperatureCelsius, lags=10)
    res = res.fit()
    # Plot the actual temperatures and fitted model
    plt.plot(data["year"], data.AverageTemperatureCelsius, label="Actual temperatures")
    plt.plot(data["year"][10:], res.fittedvalues, color='red', label = "Fitted model")
    
    # Predict the data
    pred_data = res.get_prediction(start=len(data.year.unique()), end=len(data.year.unique())+250)
    conf_df = pd.concat([pred_data.predicted_mean, pred_data.conf_int()], axis = 1)
    conf_df = conf_df.rename(columns={'lower': 'Lower CI',
                                      'upper': 'Upper CI'})
    upper = conf_df['Upper CI']
    lower = conf_df['Lower CI']

    # Plot the forecast and its confidence levels
    plt.plot(np.arange(max_year, 250+max_year+1), conf_df['predicted_mean'],
             color = 'orange', label = 'Predicted')
    plt.plot(np.arange(max_year, 250+max_year+1), upper,color = 'grey')
    plt.plot(np.arange(max_year, 250+max_year+1), lower,color = 'grey')
    plt.fill_between(np.arange(max_year, 250+max_year+1), lower, upper,
                     color='grey', alpha=0.2, label = "Confidence Interval")

    # Add legend and axis titles
    plt.legend(loc = 'best', fontsize = 20)
    plt.title(f"AR- Predicted temperatures in {country}", size=29)
    plt.xlabel("Year", fontsize=20)
    plt.ylabel("Average Year Temperature [C]", fontsize=25)
    plt.xticks(fontsize=17, rotation=90)
    plt.yticks(fontsize=17)

    # Change axis bounds
    plt.xlim([1740, 2015+250])
    plt.locator_params(axis='x', nbins=30)
    plt.subplots_adjust(top=0.94, bottom=0.12, right=0.96, left=0.08)

    # Save or display the plot
    if save:
        path = "../images/"
        plt.savefig(path + country.replace(" ", "_") + "_ar.png")
        plt.clf()
        plt.close()
    else:
        plt.show()
        plt.close()

if __name__ == "__main__":
    main()
