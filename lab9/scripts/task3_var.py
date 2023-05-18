import pandas as pd
import matplotlib.pyplot as plt
from utils import parse_args, load_data
from statsmodels.tsa.api import VAR
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

def main():
    """Call all of the functions
    """
    _, data = load_data()
    args = parse_args()
    for count in ["Japan", "Ukraine", "Poland"]:
        get_var_model(data, count, save=args.display)
    
def get_var_model(data:pd.DataFrame, country:str, save:bool):
    """Function used for creating a VAR model and using
    it to forecast temperatures in a given country

    :param data: Temperatures data
    :type data: pd.DataFrame
    :param country: Country used to create the model
    :type country: str
    :param save: Whether to save or display the image
    :type save: bool
    """
    sns.set_theme()
    sns.set_style("darkgrid")
    plt.figure(figsize=(14, 8))

    # Get the data
    data = data[data.Country == country]
    data = data[['year','AverageTemperatureCelsius']]

    # Create and fit the model
    model = VAR(data)
    model_fitted = model.fit(4)

    # Plot the observed temperatures and fitted model
    plt.plot(data.year, data.AverageTemperatureCelsius, label="Observed temperatures")
    plt.plot( model_fitted.fittedvalues.year,
             model_fitted.fittedvalues.AverageTemperatureCelsius,
             color='red', label = "Fitted model")

    # Forecast the temperatures
    forecast = model_fitted.forecast_interval(model_fitted.endog, 250, alpha=0.05)

    # Plot the forecast and its confidence interval
    plt.plot(forecast[0][:,0], forecast[0][:,1], label = "Predicted")
    plt.plot(forecast[1][:,0], forecast[1][:,1], color="grey")
    plt.plot(forecast[2][:,0], forecast[2][:,1], color="grey")
    plt.fill_between(forecast[2][:,0], forecast[1][:,1], forecast[2][:,1],
                     color='grey', alpha=0.2, label = "Confidence Interval")

    # Add legend and axis titles
    plt.legend(loc = 'best', fontsize = 20)
    plt.title(f"VAR- Predicted temperatures in {country}", size=29)
    plt.xlabel("Year", fontsize=23)
    plt.ylabel("Average Year Temperature [C]", fontsize=25)
    plt.xticks(fontsize=17, rotation=90)
    plt.yticks(fontsize=17)

    # Change axis bounds
    plt.xlim([1740, 2015+250])
    plt.locator_params(axis='x', nbins=30)
    plt.subplots_adjust(top=0.94, bottom=0.12, right=0.96, left=0.08)

    if save:
        path = "../images/"
        plt.savefig(path + country.replace(" ", "_") + "_var.png")
        plt.clf()
        plt.close()
    else:
        plt.show()
        plt.close()

if __name__ == "__main__":
    main()