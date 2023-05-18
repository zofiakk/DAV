"""Main

This script is used to call of the functions necessary to
create 4 different types of plots and allows to chose wether
to save them to the images folder or display them all

This file contains the following functions:

    * main- calls all of the functions to create the images

"""
import pandas as pd
from task2a import make_scatter_a
from task2b import make_scatter_b
from task2c import make_scatter_c
from task2d import make_scatter_d
from task3a import make_box_a
from task3b import make_box_b
from task3c import make_box_c
from task4a import make_time_series_a
from task4b import make_time_series_b
from task4c import make_time_series_c
from task5a import make_subplots_a
from task5b import make_subplots_b
from task5c import make_subplots_c
from task5d import make_subplots_d
from task5e import make_subplots_e
from utils import load_data, parse_args

# TO do violin i kolejny


def main():
    """Call all of the functions to save plots to images folder
    or display them in the interactive windows
    """
    # Parse the arguments
    args = parse_args()

    # Get the data
    filtered_data, avg_temp, avg_city = load_data()

    # Create the plots
    make_plots(filtered_data=filtered_data, avg_tem=avg_temp,
               avg_city=avg_city, save=args.display)


def make_plots(filtered_data: pd.DataFrame, avg_tem=pd.DataFrame, avg_city=pd.DataFrame, save=True):
    """Function which creates all of the plots

    :param filtered_data: DataFrame with the filtered and cleaned values
    :type filtered_data: DataFrame
    :param avg_tem: DataFrame with the average temperatures for each year
    :type avg_tem: DataFrame
    :param avg_city: DataFrame with the average temperatures for each year and city
    :type avg_city: DataFrame
    :param save: Whether to save the plots, defaults to True
    :type save: bool, optional
    """

    # Scatter plots- Task 2
    # A
    make_scatter_a(filtered_data, save=save, fig_name="../images/fig1.png")
    # B
    make_scatter_b(filtered_data, save=save, fig_name="../images/fig2.png")
    # C
    make_scatter_c(filtered_data, save=save, fig_name="../images/fig3.png")
    # D
    make_scatter_d(filtered_data, save=save, fig_name="../images/fig4.png")

    # Box plots- Task 3
    # A
    make_box_a(filtered_data, save=save, fig_name="../images/fig5.png")
    # B
    make_box_b(filtered_data, save=save, fig_name="../images/fig6.png")
    # C
    make_box_c(filtered_data, save=save, fig_name="../images/fig7.png")

    # Time series- Task 4
    # A
    make_time_series_a(avg_tem, save=save, fig_name="../images/fig8.png")
    # B
    make_time_series_b(avg_tem, save=save, fig_name="../images/fig9.png")
    # C
    make_time_series_c(avg_tem, save=save, fig_name="../images/fig10.png")

    # Subplots- Task 5
    # A
    make_subplots_a(avg_tem, save=save, fig_name="../images/fig11.png")
    # B
    make_subplots_b(avg_city, save=save, fig_name="../images/fig12.png")
    # C
    make_subplots_c(avg_city, save=save, fig_name="../images/fig13.png")
    # D
    make_subplots_d(avg_city, save=save, fig_name="../images/fig14.png")
    # E
    make_subplots_e(avg_city, save=save, fig_name="../images/fig15.png")


if __name__ == "__main__":
    main()
