"""Task3b

This script is used to create the box plot
for separate countries

This file contains the following functions:

    * main- calls the function to create the image
    * make_box_b- creates the plot
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
    make_box_b(filtered_data, save=args.display,
                   fig_name="../images/fig6.png")

def make_box_b(data:pd.DataFrame, save:bool, fig_name:str):
    """Function which creates box plot with added jitter

    :param data: DataFrame with the temperatures
    :type data: pd.DataFrame
    :param save: Wether to save the plot
    :type save: bool
    :param fig_name: Name of the figure if the plot
    is to be saved
    :type fig_name: str
    """
    fig, ax = plt.subplots(figsize=(14,8))
    sns.set_style()
    sns.set_theme()
    # Add jitter
    ax = sns.stripplot(x='country_id', y='AverageTemperatureCelsius',
                       data=data, color="red", alpha=0.2, jitter=0.4, zorder=0.9)
    ax = sns.boxplot(data=data, x=data["country_id"], y=data['AverageTemperatureCelsius'],
                     color="white", medianprops={"color": "black", "linewidth": 3},
                     boxprops={'facecolor':'none', 'edgecolor':'black'},
                     whiskerprops={'color':'black'}, capprops={'color':'black'},
                     flierprops={"markerfacecolor": 'black', "markeredgecolor":'black'},
                     zorder=100)
    ax.set_axisbelow(True)
    plt.xlabel("Country id", fontsize=18)
    plt.ylabel("Average Temperature [C]", fontsize=18)
    plt.title("Average temperature across the countries", fontsize=27)
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
