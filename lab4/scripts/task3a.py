"""Task3a

This script is used to create the box plot
for separate countries

This file contains the following functions:

    * main- calls the function to create the image
    * make_box_a- creates the plot
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import pandas as pd
import seaborn as sns
from utils import parse_args, load_data

def main():
    """calls the function to create the image
    """
    args = parse_args()
    filtered_data, _, _ = load_data()
    make_box_a(filtered_data, save=args.display,
                   fig_name="../images/fig5.png")


def make_box_a(data:pd.DataFrame, save:bool, fig_name:str):
    """Function which creates the basic box plot

    :param data: DataFrame with the temperatures
    :type data: pd.DataFrame
    :param save: Wether to save the plot
    :type save: bool
    :param fig_name: Name of the figure if the plot
    is to be saved
    :type fig_name: str
    """
    fig, ax = plt.subplots(figsize=(14,8))
    sns.set_theme()
    sns.set_style()
    sns.boxplot(data=data, x=data["country_id"], y=data['AverageTemperatureCelsius'], color="white",
                medianprops={"color": "black", "linewidth": 3},
                boxprops={'facecolor':'white', 'edgecolor':'black'},
                whiskerprops={'color':'black'}, capprops={'color':'black'},
                flierprops={"markerfacecolor": 'black', "markeredgecolor":'black'})
    
    plt.xlabel("Country id", fontsize=18)
    plt.ylabel("Average Temperature [C]", fontsize=18)
    plt.title("Average temperature across the countries", fontsize=27)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
    ax.yaxis.grid(True, which="both")
    ax.xaxis.grid(True, which="both")
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
