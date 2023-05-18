from bokeh.plotting import figure
from utils import get_population_data, save_bokeh
from bokeh.models import HoverTool, Legend
from bokeh.palettes import Category10_10
from bokeh.transform import cumsum
from math import pi

# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")
data = data[data["variable"] == "2010"]

data['angle'] = data['value']/data['value'].sum() * 2*pi

countries = data["Country Name"].to_list()
colors = [Category10_10[index] for index, _ in enumerate(countries)]
data['color'] = colors

p = figure(title="Population in Poland and its neighbors in 2010",
           height=500,
            width=1000,
            tools=["wheel_zoom", "box_select", "pan"],
            toolbar_location="below")

p.add_layout(Legend(), 'right')

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='Country Name', source=data)

p.title.text_font_size = '20pt'
p.title.align = 'center'

p.legend.label_text_font_size = "12pt"
p.yaxis.axis_label_text_font_size = "15pt"
p.yaxis.major_label_text_font_size = "10pt"
p.xaxis.axis_label_text_font_size = "15pt"
p.xaxis.major_label_text_font_size = "10pt"

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

p.add_tools(HoverTool(
    tooltips=[
        ("Country name", "@{Country Name}"),
        ("Population", "@value{(0.00 a)}")
    ]
))


save_bokeh(p, "bokeh_plot3_data1")
