"""Task3c

This script is used to create the violin plot
for separate countries

This file contains the following functions:

    * main- calls the function to create the image
    * make_box_c- creates the plot
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from utils import parse_args, load_data

def main():
    """calls the function to create the image
    """
    args = parse_args()
    filtered_data, _, _ = load_data()
    make_box_c(filtered_data, save=args.display,
                   fig_name="../images/fig7.png")

def make_box_c(data:pd.DataFrame, save:bool, fig_name:str):
    """Function which creates violin plot

    :param data: DataFrame with the temperatures
    :type data: pd.DataFrame
    :param save: Wether to save the plot
    :type save: bool
    :param fig_name: Name of the figure if the plot
    is to be saved
    :type fig_name: str
    """
    sns.set_theme()
    fig = plt.figure(figsize=(14,8))
    plt.violinplot([data[data['country_id'] == country_id]['AverageTemperatureCelsius']
                    for country_id in list(set(data["country_id"].to_list()))])
    plt.xlabel("Year", fontsize=18)
    plt.ylabel("Average Temperature [C]", fontsize=18)
    plt.title("Average temperature across the countries", fontsize=27)
    plt.xticks(ticks=np.arange(1, len(set(data["country_id"].to_list()))+1),
               labels=list(set(data["country_id"].to_list())), fontsize=15)
    plt.yticks(fontsize=15)
    fig.tight_layout()
    plt.subplots_adjust(top=0.94, bottom=0.093)
    if save:
        plt.savefig(fig_name)
        plt.clf()
        plt.close()
    else:
        plt.show()

if __name__ == "__main__":
    main()
