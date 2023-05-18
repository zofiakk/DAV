
"""Task4c

This script is used to create the time series line plot
with years on the x axis and average temperatures
on the Y axis 

This file contains the following functions:

    * main- calls the function to create the image
    * make_time_series_c- creates the plot
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import rc
from utils import parse_args, load_data

def main():
    """calls the function to create the image
    """
    args = parse_args()
    _, avg_temp, _ = load_data()
    make_time_series_c(avg_temp, save=args.display,
                   fig_name="../images/fig10.png")


def make_time_series_c(data:pd.DataFrame, save:bool, fig_name:str):
    """Function which creates the plot showing the
    average temperatures across the years- one line
    for each country in separate colors

    :param data: DataFrame with the average temperatures
    :type data: pd.DataFrame
    :param save: Wether to save the plot
    :type save: bool
    :param fig_name: Name of the figure if the plot
    is to be saved
    :type fig_name: str
    """
    rc('text', usetex=True) 
    fig = plt.figure(figsize=(14,8))
    sns.lineplot(x='year', y='value', hue='Country', data=pd.melt(data, ['year', 'Country']))
    legend = plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.,
                        fontsize=14, title=r"$\textbf{Countries}$")
    plt.setp(legend.get_title(),fontsize=16)
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
