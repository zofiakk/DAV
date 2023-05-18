"""Gannt's plot

This script is used to create stationary Gantt's plot showing
the academic calendar of The Warsaw University and save it to
the pdf file

This file contains the following function:

    * gantts_plot - creates the plot with the possibility of saving it
"""
import datetime as dt
import sys
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def gantts_plot(data: pd.DataFrame, black_white: bool, save: bool,
                file_name: str = "out.gif"):
    """Function which creates the Gannt's plot showing the academic
    calendar in the color and black and white versions and allows
    to save it to the pdf file

    :param data: DataFrame with the necessary data
    :type data: pd.DataFrame
    :param black_white: Whether to prepare the black'n white version
    :type black_white: bool
    :param save: Whether to save the plot to a pdf file
    :type save: bool
    :param file_name: Name of the output file, defaults to "out.gif"
    :type file_name: str, optional
    """
    fig = plt.figure(figsize=(12, 8))
    axes = fig.add_subplot(1, 1, 1)

    plt.title("Academic Calendar- University of Warsaw 2023/24", fontsize=28)

    for index, row in data.iterrows():
        index = index*2
        # Winter dates
        if not black_white:
            axes.broken_barh(xranges=[(row['days_to_start_1_winter'],
                                       row['task_duration_1_winter']),
                                      (row['days_to_start_2_winter'],
                                       row['task_duration_2_winter'])],
                             yrange=(index + 1, 1.85), color='m', alpha=0.5)
        else:
            axes.broken_barh(xranges=[(row['days_to_start_1_winter'],
                                       row['task_duration_1_winter']),
                                      (row['days_to_start_2_winter'],
                                       row['task_duration_2_winter'])],
                             yrange=(index + 1, 1.85), hatch='\\\\\'',
                             facecolor='w', zorder=2, edgecolor='grey', alpha=0.5)
        if len(max(row['name_1_winter'].split(), key=len)) > 8:
            fontsize = 11
            offset = 1.04
        else:
            fontsize = 12
            offset = 1.1
        if row['task_duration_1_winter'] > 10:
            axes.text(float(row['days_to_start_1_winter']+1), float(index+offset),
                      row['name_1_winter'].replace(" ", "\n"), color='black', ha='left',
                      va='bottom', rotation=90, fontsize=fontsize)
        else:
            axes.text(float(row['days_to_start_1_winter']+row['task_duration_1_winter']+1),
                      float(
                          index+offset),  row['name_1_winter'].replace(" ", "\n"),
                      color='black', ha='left', va='bottom', rotation=90, fontsize=fontsize)
        if len(max(row['name_2_winter'].split(), key=len)) > 8:
            fontsize = 11
            offset = 1.04
        else:
            fontsize = 12
            offset = 1.1
        if row['task_duration_2_winter'] > 10:
            axes.text(float(row['days_to_start_2_winter']+1),
                      float(
                          index+offset),  row['name_2_winter'].replace(" ", "\n"),
                      color='black', ha='left', va='bottom', rotation=90, fontsize=fontsize)
        else:
            axes.text(float(row['days_to_start_2_winter'] + row['task_duration_2_winter'] + 1),
                      float(
                          index+offset),  row['name_2_winter'].replace(" ", "\n"),
                      color='black', ha='left', va='bottom', rotation=90, fontsize=fontsize)
        # Summer dates
        if not black_white:
            axes.broken_barh(xranges=[(row['days_to_start_1_summer'],
                                       row['task_duration_1_summer']),
                                      (row['days_to_start_2_summer'],
                                       row['task_duration_2_summer'])],
                             yrange=(index + 1, 1.85), color='b', alpha=0.5)
        else:
            axes.broken_barh(xranges=[(row['days_to_start_1_summer'],
                                       row['task_duration_1_summer']),
                                      (row['days_to_start_2_summer'],
                                       row['task_duration_2_summer'])],
                             yrange=(index + 1, 1.85),  hatch="//", alpha=0.5, zorder=2,
                             facecolor='w', edgecolor='grey')
        if len(max(row['name_1_summer'].split(), key=len)) > 8:
            fontsize = 11
            offset = 1.04
        else:
            fontsize = 12
            offset = 1.1
        if row['task_duration_1_summer'] > 10:
            axes.text(float(row['days_to_start_1_summer']+1), float(index+offset),
                      row['name_1_summer'].replace(" ", "\n"),
                      color='black', ha='left', va='bottom', rotation=90, fontsize=fontsize)
        else:
            axes.text(float(row['days_to_start_1_summer']+row['task_duration_1_summer']+1),
                      float(
                          index+offset),  row['name_1_summer'].replace(" ", "\n"),
                      color='black', ha='left', va='bottom', rotation=90, fontsize=fontsize)
        if len(max(row['name_2_summer'].split(), key=len)) > 8:
            fontsize = 11
            offset = 1.04
        else:
            fontsize = 12
            offset = 1.1
        if row['task_duration_2_summer'] > 10:
            axes.text(float(row['days_to_start_2_summer']+1), float(index+offset),
                      row['name_2_summer'].replace(" ", "\n"),
                      color='black', ha='left', va='bottom', rotation=90, fontsize=fontsize)
        else:
            axes.text(float(row['days_to_start_2_summer']+row['task_duration_2_summer']+1),
                      float(
                          index+offset),  row['name_2_summer'].replace(" ", "\n"),
                      color='black', ha='left', va='bottom', rotation=90, fontsize=fontsize)
        # No semester
        if row['start_none'] is not None:
            if not black_white:
                axes.barh(y=0.26, height=30, width=data['task_duration_none'],
                          left=data['days_to_start_none'],  color='pink', alpha=0.4)
            else:
                axes.barh(y=0.26, height=30, width=data['task_duration_none'],
                          left=data['days_to_start_none'],  hatch="...", alpha=0.2,
                          zorder=2, facecolor='w', edgecolor='grey')
            axes.text(float(row['days_to_start_none']+1.1), 6,  row['task'],
                      color='black', ha='left', va='bottom', rotation=90, fontsize=12)

    # Set the y axis limits
    axes.get_yaxis().set_visible(False)
    axes.set_ylim(0.85, 15)

    # Set x ticks and length of the axis
    xticks = np.arange(7, max(data['days_to_end_1_summer'].max(),
                              data['days_to_end_2_summer'].max()) + 9, 14)

    xticklabels = pd.date_range(start=min(data['start_1_winter'].min(),
                                          data['start_2_winter'].min())
                                + dt.timedelta(days=4),
                                end=max(data['end_1_summer'].max(),
                                        data['end_2_summer'].max())
                                + dt.timedelta(days=4)).strftime("%d/%m/%y")

    axes.set_xticks(xticks, xticklabels[::14], rotation=75)
    axes.set_xlim(axes.get_xlim()[0] + 15, axes.get_xlim()[1]-10)

    # Readability
    axes.xaxis.grid(True, alpha=0.5)
    plt.tight_layout()
    plt.subplots_adjust(top=0.94, bottom=0.093)

    # Add the legend
    if not black_white:
        special_patches = [mpatches.Patch(facecolor='m', label='Dates pertaining\nwinter semester',
                                          zorder=10, alpha=0.5),
                           mpatches.Patch(facecolor='b', label='Dates pertaining\nsummer semester',
                                          zorder=10, alpha=0.5)]
    else:
        special_patches = [mpatches.Patch(label='Dates pertaining\nwinter semester',
                                          hatch='\\\\\'', facecolor='w', zorder=2,
                                          edgecolor='black', alpha=0.6),
                           mpatches.Patch(label='Dates pertaining\nsummer semester',
                                          facecolor='w', zorder=2, edgecolor='black',
                                          hatch="///", alpha=0.6)]

    plt.legend(loc='lower right', handles=special_patches, fontsize=12)

    if save:
        with open(file_name, 'w', encoding="UTF-8") as _:
            pass
        null = open(file_name, encoding="UTF-8")
        sys.stdout = sys.stderr = null
        plt.savefig(file_name, orientation='landscape')

    else:
        plt.show()
