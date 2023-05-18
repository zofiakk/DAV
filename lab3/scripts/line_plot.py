"""Line plot

This script is used to create animated line plots for 3 types of data.

This file contains the following function:

    * animated_line_plot - creates the gif with the possibility of saving it
"""
import textwrap
import pandas as pd
import seaborn as sns
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animated_line_plot(data:pd.DataFrame, countries:list, centroid:bool, year:int,
                       save:bool, file_name:str="out.gif"):
    """Function which creates animated line plots which show
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
    # Save the data to a csv file
    df_name = "../data/" + file_name.split("/")[2].split(".")[0] + "_data.csv"
    new_df = pd.DataFrame(columns=data.columns)
    for country in countries:
        new_df = new_df.append(data.loc[country,:])
    new_df.to_csv(df_name)

    years = data.columns.to_list()[1:]
    fig = plt.figure(figsize=(14,8))
    axes = fig.add_subplot(1,1,1)

    # Get the necessary data
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

    count_data = [count0, count1, count2, count3, count4]
    codes = [count0_code, count1_code, count2_code, count3_code, count4_code]

    # Chose the colors used in a plot
    if not centroid:
        palette = list(sns.color_palette("tab10", 5).as_hex())
    else:
        palette = list(sns.color_palette("tab10", 4).as_hex())
        palette.append("m")

    def animate(i):
        axes.cla()
        axes.grid(visible=True, axis='y')
        axes.set_ylim(0, maximum_value+maximum_value*0.2)
        axes.set_xlim(min(years), max(years))
        axes.set_ylabel("Population [mln]", fontsize=20)
        axes.set_xlabel("Years", fontsize=20)
        axes.tick_params(axis='both', which='major', labelsize=15)
        axes.tick_params(axis='both', which='minor', labelsize=8)

        # Add year counter
        time_text = axes.text(0.05, 0.92, "", transform=axes.transAxes,
                               ha='left', va='top',
                              fontsize=30, color='black')
        time_text.set_text(int(i+min(years)))

        # Add plot tiltle
        if not centroid:
            axes.set_title("Population in years for 5 most populated countries", fontsize=25)
        else:
            axes.set_title("Population in years for the countries\nwith most similar " \
                           "population to {} in {}".format(countries[-1], year), fontsize=25)

        # Add lines and text above them
        for code, country_data, color, country_name in zip(codes[:4], count_data[:4],
                                                                  palette[:4], countries[:4]):
            axes.plot(years[:i+1],country_data[:i+1], color=color,
                      label=f"{textwrap.fill(country_name, 10, break_long_words = False)} ({code})")

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

        # Add final line
        if not centroid:
            axes.plot(years[:i+1],count4[:i+1], color=palette[4],
                      label=f"{textwrap.fill(countries[4], 10, break_long_words = False)} ({count4_code})")
        else:
            axes.plot(years[:i+1],count4[:i+1], color="m",
                      label=f"Centroid country:\n{textwrap.fill(countries[4], 10,break_long_words = False)} ({count4_code})")

        # Create legend
        leg = axes.legend(loc='upper left', bbox_to_anchor=(1.001, 0.99), fontsize=15)
        for line in leg.get_lines():
            line.set_linewidth(4.0)
        plt.tight_layout()

    ani = FuncAnimation(fig, animate, interval=150, frames=len(years))
    if save:
        writergif = animation.PillowWriter(fps=5)
        ani.save(file_name, writer=writergif)
    else:
        plt.show()
