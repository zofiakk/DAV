"""Clean data

This script is used to read and clean provided csv file. As a result it
returns cleaned DataFrame and saves it to another csv file

This file contains the following functions:

    * read_file_to_df - returns pandas Dataframe
    * filter_data - returns Dataframe's filtered to contain only valid countries
    * save_clean_data- saves Dataframe's to csv files
    
"""

import sys

import pandas as pd


def main():
    """Call all of the functions to save cleaned data to csv file
    """
    file_path = "../data/temperature.csv"
    new_file_name = "../data/temperature_clean.csv"
    data = read_file_to_df(file_path)
    filtered_data = filter_data(data)
    save_clean_data(filtered_data, new_file_name)


def read_file_to_df(file_path: str) -> pd.DataFrame:
    """Function to read csv file to pandas DataFrames

    :param file_path: Path to csv input file
    :type file_path: str
    :return: Dataframe with loaded data
    :rtype: pd.DataFrame
    """
    try:
        data_frame = pd.read_csv(file_path, sep=",")
    except FileNotFoundError:
        print("File not found.")
        sys.exit(-1)
    except pd.errors.EmptyDataError:
        print("No data")
        sys.exit(-1)
    except pd.errors.ParserError:
        print("Parser error")
        sys.exit(-1)
    return data_frame  # type: ignore


def filter_data(data: pd.DataFrame) -> pd.DataFrame:
    """Remove invalid rows of the raw dataset, clean it (converting Fahrenheit
    to Celsius), and drop unnecessary columns.

    :param data: Initial dataframe
    :type data: pd.DataFrame
    :return: Cleaned dataframe
    :rtype: pd.DataFrame
    """
    # Remove rows with empty 'City' or 'Country' columns
    data = data[data['City'].notna()]
    data = data[data['Country'].notna()]

    # Remove rows where 'AverageTemperatureFahr' or 'AverageTemperatureUncertaintyFahr' is nan
    data = data[data['AverageTemperatureFahr'].notna()]
    data = data[data['AverageTemperatureUncertaintyFahr'].notna()]

    # Remove 'day' column
    data.drop(columns="day", inplace=True)

    # Convert Fahrenheit's to Celsius and remove unnecessary columns
    data["AverageTemperatureCelsius"] = round(
        (data["AverageTemperatureFahr"] - 32)/1.8, 4)
    data["AverageTemperatureUncertaintyCelsius"] = round(
        (data["AverageTemperatureUncertaintyFahr"] - 32)/1.8, 4)
    data.drop(columns="AverageTemperatureFahr", inplace=True)
    data.drop(columns="AverageTemperatureUncertaintyFahr", inplace=True)
    return data


def save_clean_data(clean_data: pd.DataFrame, file_name: str):
    """Save filtered data to the new csv file

    :param clean_data: filtered DataFrame
    :type clean_data: pd.DataFrame
    :param file_name: Name of the new csv file
    :type file_name: str
    """
    clean_data.to_csv(file_name)
    return


if __name__ == "__main__":
    main()
