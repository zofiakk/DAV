import pygal
from utils import save_pygal, get_population_data
from pygal.style import Style


custom_style = Style(
  background='transparent',
  label_font_size=12,
  legend_font_size=20,
  title_font_size= 25,
  value_label_font_size =12)


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")
data = data[data["variable"] == "2010"]


pie_chart = pygal.Pie(height=400, width=900,
                        value_formatter=lambda x: '{} mln'.format(x),
                        style=custom_style)

pie_chart.title = 'Population in Poland and its neighbors in 2010'


for country, data_for_country in data.groupby("Country Name"):
    pie_chart.add(country, [round(i/1000000, 2) for i in data_for_country.value.to_list()])

save_pygal(pie_chart, "pygal_plot3_data1")
