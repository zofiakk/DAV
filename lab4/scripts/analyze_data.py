"""Analyze data

This script is used to analyze the data read
from a csv file with the temperatures

This file contains the following functions:

    * get_average_year_temperature- returns the average
    temperature for each country in each year
    * get_average_year_city_temperature- return the average
    temperature in each city in each year
"""
import pandas as pd


def get_average_year_temperature(data:pd.DataFrame) -> pd.DataFrame:
    """Function which calculates the average
    temperature in each year for each country

    :param data: DataFrame with the information
    about the temperatures
    :type data: pd.DataFrame
    :return: DataFrame with the average temperatures
    :rtype: pd.DataFrame
    """
    avg_temp = data.groupby(['Country', 'year'], as_index=False)['AverageTemperatureCelsius'].mean()
    return avg_temp

def get_average_year_city_temperature(data:pd.DataFrame) -> pd.DataFrame:
    """Function which calculates the average temperatures
    for each city in each year

    :param data: DataFrame with the information
    about the temperatures
    :type data: pd.DataFrame
    :return: DataFrame with the average temperatures
    :rtype: pd.DataFrame
    """
    avg_temp = data.groupby(['Country', 'year', 'City'],
                            as_index=False)['AverageTemperatureCelsius'].mean()
    return avg_temp
