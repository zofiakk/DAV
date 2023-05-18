"""Bubble plot

This script is used to create animated bubble plots for 3 types of data.

This file contains the following function:

    * animated_bubble_plot - creates the gif with the possibility of saving it
"""
import textwrap
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import animation
import numpy as np
import seaborn as sns
import pandas as pd


def animated_bubble_plot(data:pd.DataFrame, density:pd.DataFrame, countries:list,
                         centroid:bool, year:int, save:bool, file_name:str="out.gif"):
    """Function which creates animated bubble plots
    and allows to save them to gif files

    :param data: Dataframe with the necessary information
    :type data: pd.DataFrame
    :param density: DataFrame with density information
    :type density: pd.DataFrame
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
    # Save the data to a csv file
    df_name = "../data/" + file_name.split("/")[2].split(".")[0] + "_data.csv"
    new_df = pd.DataFrame(columns=data.columns)
    for country in countries:
        new_df = new_df.append(data.loc[country,:])
        new_df = new_df.append(density.loc[country,:])
    new_df.to_csv(df_name)

    years = data.columns.to_list()[1:]
    fig = plt.figure(figsize=(14,8))
    axes = fig.add_subplot(1,1,1)
    count0 = data.loc[countries[0],:].values[1:]/1000000
    count1 = data.loc[countries[1],:].values[1:]/1000000
    count2 = data.loc[countries[2],:].values[1:]/1000000
    count3 = data.loc[countries[3],:].values[1:]/1000000
    count4 = data.loc[countries[4],:].values[1:]/1000000

    dens0 = density.loc[countries[0],:].values
    dens1 = density.loc[countries[1],:].values
    dens2 = density.loc[countries[2],:].values
    dens3 = density.loc[countries[3],:].values
    dens4 = density.loc[countries[4],:].values

    maximum_value = max([count0.max(), count1.max(), count2.max(), count3.max(), count4.max()])
    count0_code = data.loc[countries[0],:].values[0]
    count1_code = data.loc[countries[1],:].values[0]
    count2_code = data.loc[countries[2],:].values[0]
    count3_code = data.loc[countries[3],:].values[0]
    count4_code = data.loc[countries[4],:].values[0]

    # Remove nans form density data
    dens_names = [dens0, dens1, dens2, dens3, dens4]
    for dens_data in dens_names:
        mask = np.isnan(dens_data)
        dens_data[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), dens_data[~mask])

    count_data = [count0, count1, count2, count3, count4]
    codes = [count0_code, count1_code, count2_code, count3_code, count4_code]

    # Get the density information to use in legend
    min_dens = max(round(min(map(min, dens_names))/10)*10,1)
    max_dens = round(max(map(max, dens_names))/100)* 100
    mid_dens = round((min_dens + max_dens)/100)* 50
    dens_values = [min_dens, mid_dens, max_dens]

    # Create colors and labels lists
    if not centroid:
        labels_leg = [f"{textwrap.fill(country, 10, break_long_words = False)} ({code})"
                  for country, code in zip(countries, codes)]
        palette = list(sns.color_palette("tab10", 5).as_hex())
    else:
        labels_leg = [f"{textwrap.fill(country, 10, break_long_words = False)} ({code})"
                  for country, code in zip(countries[:4], codes[:4])]
        labels_leg.append(f"Centroid country:\n{textwrap.fill(countries[4], 10,break_long_words = False)} ({count4_code})")
        palette = list(sns.color_palette("tab10", 4).as_hex())
        palette.append("m")

    # Get data about sizes
    scatter_sizes = plt.scatter([years]*5, count_data, s=dens_names)
    handles_sizes, _ = scatter_sizes.legend_elements(prop="sizes", alpha=0.6)
    handles_s = [handles_sizes[0], handles_sizes[len(handles_sizes)//2] , handles_sizes[-1]]

    def animate(i):
        axes.cla()
        axes.grid(visible=True, axis="y")
        axes.set_ylim(0, maximum_value+maximum_value*0.2)
        axes.set_xlim(min(years), max(years))
        axes.set_ylabel("Population [mln]", fontsize=25)
        axes.set_xlabel("Years", fontsize=25)
        axes.tick_params(axis='both', which='major', labelsize=15)
        axes.tick_params(axis='both', which='minor', labelsize=8)

        # Add title
        if not centroid:
            axes.set_title("Population in years for 5 most populated countries\n", fontsize=28)
        else:
            axes.set_title("Population in years for the countries\nwith most similar " \
                           "population to {} in {}\n".format(countries[-1], year), fontsize=28)

        # Add year counter
        time_text = axes.text(0.05, 0.92, "", transform=axes.transAxes,
                               ha='left', va='top', fontsize=30, color='black')
        time_text.set_text(int(i+min(years)))

        # Create alpha gradient- fading bubbles
        gradient=[]
        for _ in range(i+1):
            if len(gradient) == 0:
                gradient.append(1)
            else:
                last = gradient[-1]
                if last > 0.25:
                    gradient.append(last-0.2)
                else:
                    gradient.append(0.15)
        gradient.reverse()

         # Create scatter plot
        plt.scatter([years[:i+1]]*5,
                    [count0[:i+1], count1[:i+1], count2[:i+1], count3[:i+1], count4[:i+1]],
                    s = [dens0[:i+1], dens1[:i+1], dens2[:i+1], dens3[:i+1], dens4[:i+1]],
                    color=np.concatenate([([j]*(i+1)) for j in palette], axis=0),
                    alpha=[gradient] * len(palette))

        # Add text above bubbles
        for code, country_data, color in zip(codes, count_data, palette):
            if i > 2 and i < len(years)-2:
                axes.text(i/len(years)-0.01,country_data[i]/(maximum_value+maximum_value*0.2),
                    f'{code}\n {round(country_data[i],2)}', transform=axes.transAxes,
                    ha='center', va='bottom', fontsize=15, color=color)
            elif i <= 2:
                axes.text(0.04,country_data[i]/(maximum_value+maximum_value*0.2),
                    f'{code}\n {round(country_data[i],2)}', transform=axes.transAxes,
                    ha='center', va='bottom', fontsize=15, color=color)
            else:
                axes.text(0.95,country_data[i]/(maximum_value+maximum_value*0.2),
                    f'{code}\n {round(country_data[i],2)}', transform=axes.transAxes,
                    ha='center', va='bottom', fontsize=15, color=color)

        # Create patches to use in legend
        patches = [mpatches.Patch(color=color) for color in palette]

        # Sizes legend
        labels = [f"{val} people/km\u00b2" for val in dens_values]
        legend = axes.legend(handles_s, labels, loc="lower left",
                             bbox_to_anchor=(1.001, 0.01), title="Sizes",
                             fontsize=15, labelspacing=1.25)
        legend.get_title().set_fontsize('19')
        axes.add_artist(legend)

        # Country legend
        leg = axes.legend(patches, labels_leg, loc='upper left',
                          bbox_to_anchor=(1.001, 0.99), fontsize=15, title="Countries")
        leg.get_title().set_fontsize('19')
        plt.tight_layout()

    ani = FuncAnimation(fig, animate, interval=150, frames=len(years))
    if save:
        writergif = animation.PillowWriter(fps=5)
        ani.save(file_name, writer=writergif)
    else:
        plt.show()
