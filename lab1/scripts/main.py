"""Main

This script is used to call of the functions necessary to create 4 types of plots
and save them to the images folder

This file contains the following functions:

    * main- saves gifs

"""
import os
from clean_data import read_file_to_df, filter_data ,save_clean_data
from analyze_data import read_file_to_df as read_to_analyze, chose_random_country, \
    chose_random_year, find_4_closest, find_5_most_populated, get_density
from line_plot import animated_line_plot
from bubble_plot import animated_bubble_plot
from bar_plot import animated_bar_plot
from pie_chart import animated_pie_chart


def main():
    """Call all of the functions to save gif to images folder
    """
    file_path = "../data/clean_data.csv"
    file_path_area = "../data/clean_data_area.csv"

    # Make sure that clean data exists and read it to data frame
    if not os.path.isfile(file_path) or not os.path.isfile(file_path_area):
        file_path_unfiltered = "../data/API_SP.POP.TOTL_DS2_en_csv_v2_4898931.csv"
        file_path_area_unfiltered = "../data/API_AG.SRF.TOTL.K2_DS2_en_csv_v2_4908031.csv"
        data = read_file_to_df(file_path_unfiltered)
        filtered_data = filter_data(data)
        save_clean_data(filtered_data, file_path)
        data_area = read_file_to_df(file_path_area_unfiltered)
        filtered_data_area = filter_data(data_area)
        save_clean_data(filtered_data_area, file_path_area)

    filtered_data = read_to_analyze(file_path)

    # Get random year and country
    country = chose_random_country(filtered_data)
    rand_year = chose_random_year(filtered_data)
    pl_year = chose_random_year(filtered_data)

    # Find closest countries
    closest = find_4_closest(filtered_data, country, rand_year,
                             exclude=True)
    closest_to_pl = find_4_closest(filtered_data, "Poland",
                                   pl_year, exclude=True)

    # Find most populated countries
    most_populated_countries = find_5_most_populated(filtered_data)

    # Get population density
    density = get_density(filtered_data, data_area=read_to_analyze(file_path_area))

    print(f"Randomly chosen country: {country} and year: {rand_year}")
    print(f"Randomly chosen year to use with Poland as a centroid: {pl_year}")
    print("Saving gifs to 'images' folder")

    # Bar plots
    # Color
    animated_bar_plot(filtered_data, most_populated_countries, centroid=False, year=None,
                      black_white=False, save=True, file_name="../images/bar_a_color.gif")
    animated_bar_plot(filtered_data, countries=closest[:5]+[country], year=rand_year, centroid=True,
                      black_white=False, save=True, file_name="../images/bar_b_color.gif")
    animated_bar_plot(filtered_data, countries=closest_to_pl[:5]+['Poland'], year=pl_year,
                      black_white=False, centroid=True, save=True,
                      file_name="../images/bar_c_color.gif")

    # Black n white
    animated_bar_plot(filtered_data, most_populated_countries, centroid=False, year=None,
                      black_white=True, save=True, file_name="../images/bar_a_black_white.gif")
    animated_bar_plot(filtered_data, closest[:5]+[country], centroid=True, year=rand_year,
                      black_white=True, save=True, file_name="../images/bar_b_black_white.gif")
    animated_bar_plot(filtered_data, countries=closest_to_pl[:5]+['Poland'], year=pl_year,
                      centroid=True, black_white=True, save=True,
                      file_name="../images/bar_c_black_white.gif")

    # Line plots
    animated_line_plot(filtered_data, most_populated_countries, centroid=False,
                       year=None, save=True, file_name="../images/line_a.gif")
    animated_line_plot(filtered_data, closest[:5]+[country],
                       centroid=True, year=rand_year, save=True, file_name="../images/line_b.gif")
    animated_line_plot(filtered_data, closest_to_pl[:5]+["Poland"],
                       centroid=True, year=pl_year, save=True, file_name="../images/line_c.gif")

    # Bubble plots
    animated_bubble_plot(data=filtered_data, density=density,
                         countries=most_populated_countries, centroid=False,
                         year=None, save=True, file_name="../images/bubble_a.gif")
    animated_bubble_plot(data=filtered_data, density=density,
                        countries=closest[:5]+[country], centroid=True,
                        year=rand_year, save=True, file_name="../images/bubble_b.gif")
    animated_bubble_plot(data=filtered_data, density=density,
                        countries=closest_to_pl[:5]+["Poland"], centroid=True,
                        year=pl_year, save=True, file_name="../images/bubble_c.gif")

    # Pie charts
    animated_pie_chart(data=filtered_data,
                         countries=most_populated_countries, centroid=False,
                         year=None, save=True, file_name="../images/pie_a.gif")
    animated_pie_chart(data=filtered_data, countries=closest[:5]+[country],
                       centroid=True, year=rand_year, save=True,
                       file_name="../images/pie_b.gif")
    animated_pie_chart(data=filtered_data, countries=closest_to_pl[:5]+["Poland"],
                       centroid=True, year=pl_year, save=True,
                       file_name="../images/pie_c.gif")


if __name__ == "__main__":
    main()
