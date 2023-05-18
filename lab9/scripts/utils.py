"""Utils

This script contains the functions wildly used amongst the other
scripts to minimalize the code redundancy

This file contains the following functions:

    * parse_args- returns parsed command line arguments
    * load_data- loads all of the data analyzes them
"""
import argparse
import os

import pandas as pd
from analyze_data import get_average_year_temperature
from clean_data import filter_data, read_file_to_df, save_clean_data


def parse_args() -> argparse.ArgumentParser:
    """Function which parses the command line arguments

    :return: Parsed arguments
    :rtype: argparse.ArgumentParser
    """
    # create argument parser object
    parser = argparse.ArgumentParser(
        description='Save or display plots created for a given CSV file with temperatures')

    # define arguments
    parser.add_argument('display', type=int, nargs='?', const=0, choices=[0, 1],
                        default=1,
                        help='[0/1]. If option to "0" is chosen then the plots will be displayed \
                            in the interactive mode. If any other value is provided then the \
                                plots will be saved to the "images" folder')

    # parse arguments from command line
    args = parser.parse_args()

    # Check if the plots should be saved
    if args.display == 1:
        print("Saving png files to 'images' folder")
    elif args.display == 0:
        print("Created plots will be displayed")
    return args


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Function which loads and analyzes the data from the csv file

    :return: DataFrames with analyzed data
    :rtype: tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
    """
    # Add path to the csv file with the temperatures
    file_path = "../data/temperature_clean.csv"

    # Make sure that clean data exists and read it to data frame
    if not os.path.isfile(file_path):
        file_path_unfiltered = "../data/temperature.csv"
        data = read_file_to_df(file_path_unfiltered)
        filtered_data = filter_data(data)
        save_clean_data(filtered_data, file_path)

    filtered_data = read_file_to_df(file_path)

    # Get the average temperature for each country in each year
    avg_temp = get_average_year_temperature(filtered_data)

    return filtered_data, avg_temp
