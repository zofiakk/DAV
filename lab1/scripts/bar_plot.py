"""Bar plot

This script is used to create animated bar plots for 3 types of data.
It is possible to return colored versions as well as the ones using 
only black and white.

This file contains the following function:

    * animated_bar_plot - creates the gif with the possibility of saving it

"""
import textwrap
import pandas as pd
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np

def animated_bar_plot(data: pd.DataFrame, countries: list, year:int, centroid:bool,
                      black_white:bool, save:bool, file_name:str="out.gif"):
    """Function used to create animated bar plots
    showing population sizes in different years

    :param data: Dataframe with the necessary information
    :type data: pd.DataFrame
    :param countries: List of countries which should be plotted
    :type countries: list
    :param year: Year which was chosen to look for the
    most similar countries
    :type year: int
    :param centroid: Whether one country was used as a centroid
    :type centroid: bool
    :param black_white: Whether to use only black and white as colors
    :type black_white: bool
    :param save: Whether to save the gif
    :type save: bool
    :param file_name: Name of the gif file, defaults to "out.gif"
    :type file_name: str, optional
    """
    years = data.columns.to_list()[1:]
    fig = plt.figure(figsize=(12,8))
    axes = fig.add_subplot(1,1,1)

    # Set the plot colors
    palette = list(sns.color_palette("tab10", 5).as_hex())
    hatch = ['///', '--', '\\\'', '\///', 'xxx']

    # Get the data
    count0 = data.loc[countries[0],:].values[1:]/1000000
    count1 = data.loc[countries[1],:].values[1:]/1000000
    count2 = data.loc[countries[2],:].values[1:]/1000000
    count3 = data.loc[countries[3],:].values[1:]/1000000
    count4 = data.loc[countries[4],:].values[1:]/1000000
    maximum_value = max([count0.max(), count1.max(), count2.max(), count3.max(), count4.max()])

    count0_code = data.loc[countries[0],:].values[0]
    count1_code = data.loc[countries[1],:].values[0]
    count2_code = data.loc[countries[2],:].values[0]
    count3_code = data.loc[countries[3],:].values[0]
    count4_code = data.loc[countries[4],:].values[0]

    # Create color dictionary
    if not black_white:
        color_dict = {country:color for country, color in zip(countries, palette)}
    else:
        color_dict = {country:color for country, color in zip(countries, hatch)}

    def animate(i):
        axes.cla()
        axes.grid(visible=True, axis='y')

        # Create the year counter
        time_text = axes.text(0.1, 0.9,"", transform=axes.transAxes, ha='left', va='top',
                              fontsize=30, color='black')
        time_text.set_text(int(i+min(years)))

        # Set the axis limits
        axes.set_ylim(0, maximum_value+maximum_value*0.25)
        axes.set_ylabel("Population [mln]", fontsize=20)

        # Set the x axis label
        if centroid:
            axes.set_xlabel("Countries with the most similar\npopulation to {} in {}".format(
                countries[-1], year), fontsize=20)
        else:
            axes.set_xlabel("5 most populated countries", fontsize=20)

        # Create the tics to use on the x axis
        tickdic = {countries[0]:count0[i], countries[1]:count1[i], countries[2]:count2[i],
                   countries[3]:count3[i], countries[4]:count4[i]}
        sorted_tickdic = sorted(tickdic.items(), key=lambda x: x[1])
        tcks = [i[0] for i in sorted_tickdic]

        # Create the bars
        if not black_white:
            bars = plt.bar(range(5), sorted([count0[i], count1[i], count2[i], count3[i],
                                             count4[i]]),
                           color=[color_dict[i[0]] for i in sorted_tickdic])
        else:
            bars = plt.bar(range(5), sorted([count0[i], count1[i], count2[i], count3[i],
                                             count4[i]]),
                           hatch = hatch, color='w', zorder=10, edgecolor = 'black')

        # Create labels to place above bars
        bar_labels =  {count0[i]:f"{round(count0[i], 2)}\n{count0_code}",
                       count1[i]:f"{round(count1[i], 2)}\n{count1_code}",
                       count2[i]:f"{round(count2[i], 2)}\n{count2_code}",
                       count3[i]:f"{round(count3[i], 2)}\n{count3_code}",
                       count4[i]:f"{round(count4[i], 2)}\n{count4_code}"}
        sorted_bar_labels = sorted(bar_labels.items(), key=lambda x: x[0])
        labels = [i[1] for i in sorted_bar_labels]

        plt.bar_label(bars, labels=labels, fontsize=15)
        plt.title("Population by year", fontsize=30)
        plt.xticks(np.arange(5), tcks, fontsize=15)
        plt.yticks(fontsize=15)

        # Create patches to use in legend
        if centroid:
            if not black_white:
                special_patch = mpatches.Patch(color='m', label='Centroid country')
                for i, bar_i in enumerate(bars):
                    if tcks[i] == countries[-1]:
                        bar_i.set_color("m")
            else:
                special_patch = mpatches.Patch(facecolor='w', edgecolor="black",
                                           hatch='...', label='Centroid country',
                                           zorder= 10)
                for i, bar_i in enumerate(bars):
                    if tcks[i] == countries[-1]:
                        bar_i.set_hatch('...')
            plt.legend(handles=[special_patch], fontsize=20)

        # Set tick labels
        axes.set_xticklabels([textwrap.fill(t.get_text(), 10, break_long_words = False)
                              for t in axes.get_xticklabels()])
        plt.tight_layout()

    ani = FuncAnimation(fig, animate, interval=150, frames=len(years))
    if save:
        writergif = animation.PillowWriter(fps=5)
        ani.save(file_name, writer=writergif)
    else:
        plt.show()
