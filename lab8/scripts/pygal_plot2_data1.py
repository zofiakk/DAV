import pygal
from utils import save_pygal, get_population_data
from pygal.style import Style


custom_style = Style(
  background='transparent',
  label_font_size=12,
  major_label_font_size = 12,
  legend_font_size=20,
  title_font_size= 25,
  tooltip_font_size=10,
  value_font_size=12)


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv", ["Kenya", "Argentina", "Tanzania", "Poland", "Colombia"])

box_plot = pygal.Box(height=490, width=1200,
                        truncate_label=False, x_label_rotation=20,
                        value_formatter=lambda x: '{} mln'.format(round(x,2)),
                        style=custom_style)

box_plot.title = 'Population in Poland and 4 other countries across the years'
box_plot.y_title = 'Country population\n[mln]'
box_plot.x_title = 'Countries'
labels = [str(i) for i in list(data["Country Name"].unique())]
box_plot.x_labels = labels

for country, data_for_country in data.groupby("Country Name"):
    box_plot.add(country, [i/1000000 for i in data_for_country.value.to_list()])
    

save_pygal(box_plot, "pygal_plot2_data1")
    