"""Task2b

This script is used to create the scatter plot
with all of the data point

This file contains the following functions:

    * main- calls the function to create the image
    * make_scatter_b- creates the plot

"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from utils import parse_args, load_data


def main():
    """calls the function to create the image
    """
    args = parse_args()
    filtered_data, _, _ = load_data()
    make_scatter_b(filtered_data, save=args.display,
                   fig_name="../images/fig2.png")


def make_scatter_b(data: pd.DataFrame, save: bool, fig_name: str):
    """Function which creates the scatter plot with dots
    instead of circles

    :param data: DataFrame with the temperatures
    :type data: pd.DataFrame
    :param save: Wether to save the plot
    :type save: bool
    :param fig_name: Name of the figure if the plot
    is to be saved
    :type fig_name: str
    """
    sns.set_theme()
    sns.set_style("darkgrid")
    fig = plt.figure(figsize=(14, 8))

    plt.scatter(
        x=data['year'], y=data['AverageTemperatureCelsius'], color='black', marker='.')
    plt.xlabel("Year", fontsize=18)
    plt.ylabel("Average Temperature [C]", fontsize=18)
    plt.title("Average temperature across the years", fontsize=27)
    plt.xticks(fontsize=15)
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
