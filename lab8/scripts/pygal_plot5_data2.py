import pygal
from utils import save_pygal
from pygal.style import Style
from palmerpenguins import load_penguins


# Read the data
penguins = load_penguins()

custom_style = Style(
  background='transparent',
  label_font_size=14,
  legend_font_size=20,
  title_font_size= 25,
  value_label_font_size =12,
  tooltip_font_size=20,
  major_label_font_size = 14,)


xy_chart  = pygal.XY(stroke=False, height=450, width=1100,
                        x_value_formatter=lambda x: '{}mm'.format(x),
                        value_formatter=lambda y: '{}mm'.format(y),
                        style=custom_style)

xy_chart.title = 'Penguins bill width vs bill depth'

for index, (species, data_for_species) in enumerate(penguins.groupby("species")):
    values = list(zip(data_for_species.bill_length_mm, data_for_species.bill_depth_mm))
    xy_chart.add(species, values)



xy_chart.y_title = 'Bill depth [mm]'
xy_chart.x_title = 'Bill width [mm]'


save_pygal(xy_chart, "pygal_plot5_data2")
