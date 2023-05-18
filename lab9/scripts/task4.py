"""Task4

Script allowing to calculate and save to file
a table with the average MAE calculated for
TimeSeriesSplit which allow to quantify model fitness
"""
import warnings

warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from utils import parse_args, load_data
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.api import VAR
from sklearn.metrics import mean_absolute_error


def main():
    """Call all of the functions"""
    _, data = load_data()
    args = parse_args()
    make_table(data, ["Ukraine", "Poland"], save=args.display)


def make_table(data: pd.DataFrame, countries: list, save: bool):
    """Function used to calculate MAE for 3 models and 2 countries

    :param data: Temperature data
    :type data: pd.DataFrame
    :param countries: List of countries for which
    the MAE should be calculated
    :type countries: list
    :param save: Whether to save or display the table
    :type save: bool
    """
    # Get the country data
    country1_data = data[data.Country == countries[0]].reset_index()
    country2_data = data[data.Country == countries[1]].reset_index()

    # Create the split
    tscv = TimeSeriesSplit(n_splits=10)
    MAE_list = [[] for i in range(6)]

    for train_index, test_index in tscv.split(country1_data):
        y_train_1, y_test_1 = (
            country1_data.AverageTemperatureCelsius[train_index],
            country1_data.AverageTemperatureCelsius[test_index],
        )
        y_train_2, y_test_2 = (
            country2_data.AverageTemperatureCelsius[train_index],
            country2_data.AverageTemperatureCelsius[test_index],
        )
        years_train, _ = country1_data.year[train_index], country1_data.year[test_index]

        # Create the lists of used models
        models_1 = [
            AutoReg(y_train_1, lags=10),
            ARIMA(y_train_1, order=(0, 2, 3)),
            VAR(pd.concat([y_train_1, years_train], axis=1)),
        ]
        models_2 = [
            AutoReg(y_train_2, lags=10),
            ARIMA(y_train_2, order=(0, 2, 3)),
            VAR(pd.concat([y_train_2, years_train], axis=1)),
        ]

        # Calculate MAE for each model and each split
        for index, model in enumerate(models_1):
            if index < 2:
                model_fitted = model.fit()
                predicted = model_fitted.predict(test_index[0], test_index[-1])
            else:
                model_fitted = model.fit(4)
                predicted = model_fitted.forecast(
                    model_fitted.endog, steps=len(y_test_1)
                )[:, 0]
            MAE = mean_absolute_error(y_test_1, predicted)
            MAE_list[index].append(MAE)

        for index, model in enumerate(models_2):
            if index < 2:
                model_fitted = model.fit()
                predicted = model_fitted.predict(test_index[0], test_index[-1])
            else:
                model_fitted = model.fit(4)
                predicted = model_fitted.forecast(
                    model_fitted.endog, steps=len(y_test_2)
                )[:, 0]
            MAE = mean_absolute_error(y_test_2, predicted)
            MAE_list[index + 3].append(MAE)

    # Calculate the MAE mean and show it as a table
    MAE_mean = [np.mean(i) for i in MAE_list]
    MAE_tab = np.array(MAE_mean).reshape(2, 3)
    MAE_tab = pd.DataFrame(
        MAE_tab, columns=["AR", "ARIMA", "VAR"], index=[countries[0], countries[1]]
    )

    # Save or display the table
    if save:
        print("Saving table to data folder")
        MAE_tab.to_csv("../data/task4_table.csv")
    else:
        print(MAE_tab)


if __name__ == "__main__":
    main()
