"""Clean data

This script is used to read and clean provided files. As a result it
returns cleaned DataFrames and saves them to csv files

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
    file_path = "../data/API_SP.POP.TOTL_DS2_en_csv_v2_4898931.csv"
    file_path_area = "../data/API_AG.SRF.TOTL.K2_DS2_en_csv_v2_4908031.csv"
    new_file_name = "../data/clean_data.csv"
    new_file_area = "../data/clean_data_area.csv"
    data = read_file_to_df(file_path)
    filtered_data = filter_data(data)    
    save_clean_data(filtered_data, new_file_name)
    data_area = read_file_to_df(file_path_area)
    filtered_data_area = filter_data(data_area)
    save_clean_data(filtered_data_area, new_file_area)


def read_file_to_df(file_path: str) -> pd.DataFrame:
    """Function to read csv files to pandas DataFrames

    :param file_path: Path to csv input file
    :type file_path: str
    :return: Dataframe with loaded data
    :rtype: pd.DataFrame
    """
    try:
        data_frame = pd.read_csv(file_path, header=2, sep=",")
        data_frame = data_frame.iloc[:, :-1]
        year = list(data_frame.columns)
        year[4:] = list(map(int, year[4:]))  # type: ignore
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


def filter_data(data:pd.DataFrame) -> pd.DataFrame:
    """Clean the dataframe

    :param data: Initial dataframe
    :type data: pd.DataFrame
    :return: Cleaned dataframe
    :rtype: pd.DataFrame
    """
    unnecessary = ['Middle East & North Africa (IDA & IBRD countries)', 'OECD members',
                  'Other small states', 'Pacific island small states', 'Post-demographic dividend',
                  'IBRD only', 'IDA & IBRD total', 'IDA total', 'IDA blend', 'IDA only', 'World',
                  'European Union', 'Fragile and conflict affected situations', 'Euro area',
                  'Africa Eastern and Southern', 'Africa Western and Central', 'High income',
                  'Central Europe and the Baltics','Upper middle income', 'Small states',
                  'Sub-Saharan Africa (excluding high income)', 'Middle East & North Africa',
                  'East Asia & Pacific (IDA & IBRD countries)', 'North America',
                  'Heavily indebted poor countries (HIPC)', 'Arab World',
                  'Europe & Central Asia (IDA & IBRD countries)', 'Not classified', 'South Asia',
                  'Lower middle income', 'Latin America & Caribbean', 'Sub-Saharan Africa', 
                  'Least developed countries: UN classification', 'Low income',
                  'Low & middle income', 'Pre-demographic dividend', 'West Bank and Gaza',
                  'East Asia & Pacific (excluding high income)', 'Early-demographic dividend',
                  'East Asia & Pacific', 'Europe & Central Asia (excluding high income)',
                  'Europe & Central Asia', 'Latin America & Caribbean (excluding high income)',
                  'Latin America & the Caribbean (IDA & IBRD countries)',
                  'Middle income', 'Late-demographic dividend', 'Pre-demographic dividend',
                  'South Asia (IDA & IBRD)', 'Sub-Saharan Africa (IDA & IBRD countries)',
                  'Middle East & North Africa (excluding high income)']

    data = data.drop(['Indicator Name', 'Indicator Code'], axis=1)
    new_data = data[~data['Country Name'].isin(unnecessary)]
    new_data = new_data.set_index('Country Name')
    return new_data


def save_clean_data(clean_data:pd.DataFrame, file_name:str):
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
