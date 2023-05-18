
"""Task5e

This script is used to create the time series line plot
with subplots where each plot shows temperatures
in different countries

This file contains the following functions:

    * main- calls the function to create the image
    * make_subplots_e- creates the plot
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import numpy as np
import matplotlib as mpl
from utils import parse_args, load_data

def main():
    """calls the function to create the image
    """
    args = parse_args()
    _, _, avg_city = load_data()
    make_subplots_e(avg_city, save=args.display,
                   fig_name="../images/fig15.png")


def make_subplots_e(data:pd.DataFrame, save:bool, fig_name:str):
    sns.set_style("whitegrid")
    fig = plt.figure(figsize=(14,12))
    data=pd.melt(data, ['year', 'Country', 'City'])
    palette = {'Ukraine':mpl.cm.terrain,
               'France':mpl.cm.Purples,
               'New Zealand':mpl.cm.Blues,
               'South Africa':mpl.cm.Greens,
               'Poland':mpl.cm.Oranges,
               'Japan':mpl.cm.Reds,
               'Sweden':mpl.cm.pink,
               'Brazil':mpl.cm.winter}
    new_palette = {key:{} for key in palette.keys()}
    norm = mpl.colors.Normalize(vmin=-5, vmax=10)
    for country, city in zip(data['Country'], data['City']):
        cmap = mpl.cm.ScalarMappable(norm=norm, cmap=palette[country])
        if len(new_palette[country].keys()) == 0:
            new_palette[country][city] = cmap.to_rgba(0)
        elif len(new_palette[country].keys()) != 0 and city not in new_palette[country].keys():
            new_palette[country][city] = cmap.to_rgba(1+len(new_palette[country].keys()))
    new_palette2={}
    for key in palette.keys():
        new_palette2.update(new_palette[key])
    g = sns.FacetGrid(data, col="Country", col_wrap=3, height=2, aspect=2, hue="Country", despine=False)
    
    g.map(sns.lineplot, 'year','value', 'City', palette=new_palette2)
    
    legend_handles = [plt.Line2D([0], [0], marker="_", markersize=10, markeredgewidth=2,
                                 color=color, label=label,
                                 linestyle='') for label, color in dict(reversed(list(new_palette2.items()))).items()]
    legend = plt.legend(handles=legend_handles, ncol=3,  columnspacing=0.2,
                        bbox_to_anchor= (1.05, 1.0), title="Country", fontsize=11)
    plt.setp(legend.get_title(), fontsize=16)
    g.set(xlabel=None, ylabel=None)
    g.set(yticks=np.arange(-5,25,5))
    g.set(xticks=np.arange(1750,2020,50))
    
    g.set_yticklabels(labels=np.arange(-5,25,5), fontsize = 15)
    g.set_xticklabels(labels = np.arange(1750,2020,50), fontsize = 15)

    plt.xlabel("Year of observation", fontsize=20)
    g.fig.supylabel("Average Temperature [C]", fontsize=20)

    fig.tight_layout()

    g.fig.subplots_adjust(wspace=0.1, hspace=0.29)
    g.fig.subplots_adjust(top = 0.85, left=0.085, right=0.95)
    g.set_titles(col_template='{col_name}', size=20)

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
