"""Task5a

This script is used to create the time series line plot
with subplots where each plot shows temperatures
in different countries

This file contains the following functions:

    * main- calls the function to create the image
    * make_subplots_a- creates the plot
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
    _, avg_temp, _ = load_data()
    make_subplots_a(avg_temp, save=args.display,
                   fig_name="../images/fig11.png")
    
    
def make_subplots_a(data:pd.DataFrame, save:bool, fig_name:str):
    """Function which creates the plot with subplots
    showing the average temperatures across the years-
    one line for each country in separate colors

    :param data: DataFrame with the average temperatures
    :type data: pd.DataFrame
    :param save: Wether to save the plot
    :type save: bool
    :param fig_name: Name of the figure if the plot
    is to be saved
    :type fig_name: str
    """
    fig = plt.figure(figsize=(14,12))
    data=pd.melt(data, ['year', 'Country'])
    g = sns.FacetGrid(data, col="Country", col_wrap=3, height=2, aspect=2, hue="Country")
    g.map(sns.lineplot, 'year','value')
    legend_data = g._legend_data
    legend = plt.legend(list(legend_data.values()), legend_data.keys(), ncol=2,
                        bbox_to_anchor= (1.13, 0.99), title="Country" )
    plt.setp(legend.get_title(),fontsize=16)
    g.set(xlabel=None, ylabel=None)
    g.set(yticks=np.arange(-10,25,5))

    plt.xlabel("Year", fontsize=20)
    g.fig.supylabel("Average Temperature [C]", fontsize=20)

    fig.tight_layout()

    g.fig.subplots_adjust(top = 0.85, left=0.085)
    g.set_titles(col_template='{col_name}', size=15)

    # Title for the complete figure
    g.fig.suptitle("Average temperature in years", fontsize = 30, fontweight = 'bold' )

    if save:
        plt.savefig(fig_name)
        plt.clf()
        plt.close()
    else:
        plt.show()

if __name__ == "__main__":
    main()
