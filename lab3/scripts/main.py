"""Main

This script is used to call of the functions necessary to create 5 types of plots
and save them to the images folder

This file contains the following functions:

    * main- saves gifs and stationary images

"""
import os
from clean_data import read_file_to_df, filter_data ,save_clean_data
from analyze_data import read_file_to_df as read_to_analyze, chose_random_country, \
    chose_random_year, find_4_closest, find_5_most_populated, get_density
from line_plot import animated_line_plot
from bubble_plot import animated_bubble_plot
from bar_plot import animated_bar_plot
from pie_chart import animated_pie_chart
from gantts_plot import gantts_plot
from calendar_data import save_calendar_data, add_to_calendar_data

def main():
    """Call all of the functions to save gif to images folder
    """
    file_path = "../data/clean_data.csv"
    file_path_area = "../data/clean_data_area.csv"
    file_path_calendar = "../data/calendar_data.csv"

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

    # Make sure that csv with calendar data exists
    if not os.path.isfile(file_path_calendar):
        save_calendar_data(file_path_calendar)

    calendar_df = add_to_calendar_data(file_path_calendar)

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
    print("Saving gifs and pdf files to 'images' folder")


    # Bar plots
    # Color
    animated_bar_plot(filtered_data, most_populated_countries, centroid=False, year=None,
                      black_white=False, event_year=None, event_text=None, event_title=None,
                      save=True, file_name="../images/bar_a_color.gif")
    animated_bar_plot(filtered_data, countries=closest[:5]+[country], year=rand_year,
                      event_title=None, centroid=True,
                      black_white=False, event_year=None, event_text=None,
                      save=True, file_name="../images/bar_b_color.gif")
    animated_bar_plot(filtered_data, countries=closest_to_pl[:5]+['Poland'], year=pl_year,
                      black_white=False, event_year=None, event_text=None, event_title=None,
                      centroid=True, save=True,
                      file_name="../images/bar_c_color.gif")

    # Black n white
    animated_bar_plot(filtered_data, most_populated_countries, centroid=False, year=None,
                      black_white=True, event_year=None, event_text=None, event_title=None,
                      save=True, file_name="../images/bar_a_black_white.gif")
    animated_bar_plot(filtered_data, closest[:5]+[country], centroid=True, year=rand_year,
                      black_white=True, event_year=None, event_text=None, event_title=None,
                      save=True, file_name="../images/bar_b_black_white.gif")
    animated_bar_plot(filtered_data, countries=closest_to_pl[:5]+['Poland'], year=pl_year,
                      centroid=True, black_white=True, event_year=None, event_text=None,
                      event_title=None, save=True,
                      file_name="../images/bar_c_black_white.gif")

    # Special event
    animated_bar_plot(filtered_data, find_4_closest(filtered_data,"Bosnia and Herzegovina", 1992,
                                                    exclude=True) + ["Bosnia and Herzegovina"],
                      centroid=False, year=None, black_white=False, event_year=[1992,1995],
                      event_text=["Start of the Bosnian war", "Bosnian war\n 1992-1995",
                                  "Bosnian war\n 1992-1995", "End of the war"],
                      event_title="Population growth rate compared to\n Bosnia and Herzegovina",
                      save=True, file_name="../images/bar_event.gif")

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

    # Gantt's plot
    gantts_plot(calendar_df, black_white=False, save=True,
                file_name="../images/gantt_color.pdf")
    gantts_plot(calendar_df, black_white=True, save=True,
                file_name="../images/gantt_black_white.pdf")


if __name__ == "__main__":
    main()
