"""Analyze data

This script is used to analyze cleaned data

This file contains the following functions:

    * read_file_to_df - return pandas DataFrame
    * find_5_most_populated - return list of 5 most populated countries
    * chose_random_country - returns randomly chosen country
    * chose_random_year - returns randomly chosen year
    * find_4_closest -returns list of countries with most similar population
    * get_density - return pandas DataFrame with density information

"""
import sys
import random
import pandas as pd

def read_file_to_df(file_path: str) -> pd.DataFrame:
    """Function to read csv files to pandas DataFrames

    :param file_path: Path to csv input file
    :type file_path: str
    :return: Dataframe with loaded data
    :rtype: pd.DataFrame
    """
    try:
        data_frame = pd.read_csv(file_path, sep=",")
        data_frame = data_frame.set_index('Country Name')
        year = list(data_frame.columns)
        year[1:] = list(map(int, year[1:]))  # type: ignore
        data_frame.columns = pd.Index(year)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(-1)
    except pd.errors.EmptyDataError:
        print("No data")
        sys.exit(-1)
    except pd.errors.ParserError:
        print("Parser error")
        sys.exit(-1)
    return data_frame # type: ignore


def find_5_most_populated(data: pd.DataFrame) -> list:
    """Function which based on one dataframe creates a new one
    with data concerning 5 countries with highest population in 1960

    :param data: Processed pandas DataFrame
    :type data_processed: pd.DataFrame
    :rtype: list
    """
    largest_pop = data[1960].nlargest(5).index.to_list()
    most_populated = data[data.index.isin(largest_pop)]
    return most_populated.index.to_list()

def chose_random_country(data:pd.DataFrame) -> str:
    """Function used to randomly chose a country

    :param data: Dataframe with the data
    :type data: pd.DataFrame
    :return: Name of the chosen country
    :rtype: str
    """
    country = random.choice(list(data.index))
    return country

def chose_random_year(data:pd.DataFrame) -> int:
    """Function used to randomly chose a year

    :param data: Dataframe with the data
    :type data: pd.DataFrame
    :return: Randomly chosen year
    :rtype: int
    """
    year = random.choice(list(data.columns[1:]))
    return year

def find_4_closest(data:pd.DataFrame, country:str, year:int, exclude:bool) -> list:
    """Function used to find countries closest in population
    to a given one in a specified year

    :param data: Dataframe with all the necessary information
    :type data: pd.DataFrame
    :param country: Country which population should be used
    :type country: str
    :param year: Year used while looking for the similar populations
    :type year: int
    :param exclude: Whether to exclude country used in search
    :type exclude: bool
    :return: List of the countries with similar population
    :rtype: list
    """
    value = data[year][country]
    closest = data.iloc[(data[year]-value).abs().argsort()[:5]]
    if exclude:
        closest = closest[~closest.index.isin([country])]
    return closest.index.to_list()

def get_density(data_pop:pd.DataFrame, data_area:pd.DataFrame) -> pd.DataFrame:
    """Get number the density data- number of people divided by surface area

    :param data_pop: Dataframe with the population numbers
    :type data_pop: pd.DataFrame
    :param data_area: Dataframe with the surface area information
    :type data_area: pd.DataFrame
    :return: Dataframe with the density
    :rtype: pd.DataFrame
    """
    return data_pop.iloc[:, 1:]/data_area.iloc[:, 1:]
