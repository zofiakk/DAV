import pandas as pd
import matplotlib.pyplot as plt
from utils import parse_args, load_data

from statsmodels.tsa.arima.model import ARIMA
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
import numpy as np


def main():
    """Call all of the functions"""
    _, data = load_data()
    args = parse_args()
    for count in ["Japan", "Ukraine", "Poland"]:
        get_arima_model(data, count, args.display)


def get_arima_model(data: pd.DataFrame, country: str, save: bool):
    """Function used to create ARIMA model and use
    it to predict temperatures in a chosen country

    :param data: Temperature data
    :type data: pd.DataFrame
    :param country: Country which is to be used in a model
    :type country: str
    :param save: Whether to save or display the figure
    :type save: bool
    """
    sns.set_theme()
    sns.set_style("darkgrid")
    plt.figure(figsize=(14, 8))

    # Get the data
    data = data[data.Country == country]

    # Create abd fit the model
    model = ARIMA(data.AverageTemperatureCelsius, order=(0, 2, 3))
    results = model.fit()

    # Plot the actual temperatures and fitted model
    plt.plot(data["year"], data.AverageTemperatureCelsius, label="Actual temperatures")
    plt.plot(data["year"], results.fittedvalues, color="red", label="Fitted model")

    # Predict the data and get confidence intervals
    pred_data = results.get_forecast(250)
    conf_df = pd.concat([pred_data.predicted_mean, pred_data.conf_int()], axis=1)
    conf_df = conf_df.rename(
        columns={
            "lower AverageTemperatureCelsius": "Lower CI",
            "upper AverageTemperatureCelsius": "Upper CI",
        }
    )

    upper = conf_df["Upper CI"]
    lower = conf_df["Lower CI"]

    # Plot the forecast and confidence intervals
    plt.plot(
        np.arange(2013, 250 + 2013),
        conf_df["predicted_mean"],
        color="orange",
        label="Predicted",
    )
    plt.plot(np.arange(2013, 250 + 2013), upper, color="grey")
    plt.plot(np.arange(2013, 250 + 2013), lower, color="grey")
    plt.fill_between(
        np.arange(2013, 250 + 2013),
        lower,
        upper,
        color="grey",
        alpha=0.2,
        label="Confidence Interval",
    )

    # Add legend and axis titles
    plt.legend(loc="upper left", fontsize=20)
    plt.title(f"ARIMA- Predicted temperatures in {country}", size=29)
    plt.xlabel("Year", fontsize=20)
    plt.ylabel("Average Year Temperature [C]", fontsize=25)
    plt.xticks(fontsize=17, rotation=90)
    plt.yticks(fontsize=17)

    # Change axis bounds
    plt.xlim([1740, 2015 + 250])
    plt.locator_params(axis="x", nbins=30)
    plt.subplots_adjust(top=0.94, bottom=0.12, right=0.96, left=0.08)

    # Save or display the data
    if save:
        path = "../images/"
        plt.savefig(path + country.replace(" ", "_") + "_arima.png")
        plt.clf()
        plt.close()
    else:
        plt.show()
        plt.close()


if __name__ == "__main__":
    main()
