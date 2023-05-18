"""Pie chart

This script is used to create animated pie charts for 3 types of data.

This file contains the following function:

    * animated_pie_chart - creates the gif with the possibility of saving it
"""
import textwrap
import pandas as pd
import seaborn as sns
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animated_pie_chart(data:pd.DataFrame, countries:list, centroid:bool, year:int,
                       save:bool, file_name:str="out.gif"):
    """Function which creates animated pie charts which show
    population sizes in years and allows to save them to gif files

    :param data: Dataframe with the necessary information
    :type data: pd.DataFrame
    :param countries: List of countries which should be plotted
    :type countries: list
    :param centroid: Whether one country was used as a centroid
    :type centroid: bool
    :param year: Year which was chosen to look for the
    most similar countries
    :type year: int
    :param save: Whether to save the gif
    :type save: bool
    :param file_name: Name of the gif file, defaults to "out.gif"
    :type file_name: str, optional
    """
    years = data.columns.to_list()[1:]
    fig = plt.figure(figsize=(12,8))
    axes = fig.add_subplot(1,1,1)

    # Get the necessary data
    count0 = data.loc[countries[0],:].values[1:]/1000000
    count1 = data.loc[countries[1],:].values[1:]/1000000
    count2 = data.loc[countries[2],:].values[1:]/1000000
    count3 = data.loc[countries[3],:].values[1:]/1000000
    count4 = data.loc[countries[4],:].values[1:]/1000000

    count0_code = data.loc[countries[0],:].values[0]
    count1_code = data.loc[countries[1],:].values[0]
    count2_code = data.loc[countries[2],:].values[0]
    count3_code = data.loc[countries[3],:].values[0]
    count4_code = data.loc[countries[4],:].values[0]

    count_data = [count0, count1, count2, count3, count4]
    codes = [count0_code, count1_code, count2_code, count3_code, count4_code]
    explode = (0.0, 0.0, 0.0, 0.0, 0.0)

    # Create labels and palette used while plotting
    if not centroid:
        labels = [f"{textwrap.fill(country, 10, break_long_words = False)} ({code})" 
                  for country, code in zip(countries, codes)]
        palette = list(sns.color_palette("tab10", 5).as_hex())
    else:
        labels = [f"{textwrap.fill(country, 10, break_long_words = False)} ({code})" 
                  for country, code in zip(countries[:4], codes[:4])]
        labels.append(f"Centroid country:\n{textwrap.fill(countries[4], 10, break_long_words = False)} ({count4_code})")
        palette = list(sns.color_palette("tab10", 4).as_hex())
        palette.append("m")

    def animate(i):
        axes.cla()
        # Add year counter
        time_text = axes.text(-0.2, 0.92, "", transform=axes.transAxes,
                               ha='left', va='top',
                              fontsize=30, color='black')
        time_text.set_text(int(i+min(years)))
        
        # Add cumulative population number
        sum_text = axes.text(1.2, 0.92, "", transform=axes.transAxes,
                               ha='center', va='top',
                              fontsize=25, color='black')
        sum_text.set_text("Total population:\n" + 
                          str(round(sum([count_value[i] for count_value in count_data]),2)) + "mln")

        # Create labels used on the pie chart
        labels_pie = [f"{round(count_value[i],2)}mln\n({code})" for count_value, code in zip(count_data,
                                                                                          codes)]

        # Set title
        if not centroid:
            axes.set_title("Population in years for 5 most populated countries\n", fontsize=25)
        else:
            axes.set_title("Population in years for the countries with most similar \n" \
                           "population to {} in {}\n".format(countries[-1], year), fontsize=25)

        # Create the plot
        data = [count0[i], count1[i], count2[i], count3[i], count4[i]]
        axes.pie(data, explode=explode, colors=palette, labels=labels_pie,
            autopct='%1.1f%%', shadow=False, startangle=120, labeldistance=1.15, pctdistance=0.8,
            textprops={'fontsize': 18})

        # Add legend
        axes.legend(labels, loc="lower right", bbox_to_anchor=(1.5, 0.01), fontsize=15)
        plt.tight_layout()
    ani = FuncAnimation(fig, animate, interval=150, frames=len(years))
    if save:
        writergif = animation.PillowWriter(fps=5)
        ani.save(file_name, writer=writergif)
    else:
        plt.show()
    