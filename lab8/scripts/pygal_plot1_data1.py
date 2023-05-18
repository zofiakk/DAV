import pygal
from utils import save_pygal, get_population_data
from pygal.style import Style


custom_style = Style(
  background='transparent',
  label_font_size=16,
  legend_font_size=20,
  title_font_size= 25,
  major_label_font_size = 16,
  minor_label_font_size = 16,
  value_label_font_size = 16,
  tooltip_font_size=20)


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")

line_chart = pygal.Line(height=550, width=1200,
                        truncate_label=False, x_label_rotation=90,
                        value_formatter=lambda x: '{} mln'.format(x),
                        style=custom_style,
                        print_labels=True)

line_chart.title = 'Population in Poland and its neighbors across the years'
line_chart.x_title= 'Years'
line_chart.y_title = 'Country population\n[mln]'
labels = [str(i) for i in list(data["variable"].unique())]
line_chart.x_labels = labels

for country, data_for_country in data.groupby("Country Name"):
    line_chart.add(country, [round(i/1000000, 2) for i in data_for_country.value.to_list()])

save_pygal(line_chart, "pygal_plot1_data1")
