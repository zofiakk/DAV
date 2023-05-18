import pygal
from utils import save_pygal, get_population_data
from pygal.style import Style


custom_style = Style(
  background='transparent',
  label_font_size=12,
  legend_font_size=20,
  title_font_size= 25,
  value_label_font_size =12,
  tooltip_font_size=20)


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")
data = data[data["variable"] == "2010"]


bar_chart = pygal.Bar(height=450, width=1100,
                        value_formatter=lambda x: '{} mln'.format(x),
                        style=custom_style)

bar_chart.title = 'Population in Poland and its neighbors in 2010'

for index, (country, data_for_country) in enumerate(data.groupby("Country Name")):
    bar_chart.add(country, round(data_for_country.value.to_list()[0]/1000000, 2))



bar_chart.y_title = 'Country population\n[mln]'
bar_chart.x_title = 'Countries'


save_pygal(bar_chart, "pygal_plot4_data1")
