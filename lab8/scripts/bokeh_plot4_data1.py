from bokeh.plotting import figure
from utils import get_population_data, save_bokeh
from bokeh.models import HoverTool, LabelSet, Legend, ColumnDataSource, NumeralTickFormatter
from bokeh.palettes import Category10_10

# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")
data = data[data["variable"] == "2010"]


countries = data["Country Name"].to_list()
colors = [Category10_10[index] for index, _ in enumerate(countries)]
data['color'] = colors

text = [str(i) + " mln" for i in round(data['value']/1000000,2).to_list()]
data["text"] = text

source = ColumnDataSource(data=data)

p = figure(title="Population in Poland and its neighbors in 2010",
           height=500,
            width=1000,
            x_range=countries,
            y_range=(0, 90000000),
            tools=["wheel_zoom", "box_select", "pan"],
            toolbar_location="below")

p.add_layout(Legend(), 'right')

p.vbar(x='Country Name',
       top='value', width=0.9, bottom=0,
       color='color',
       legend_field="Country Name", source=source)

labels = LabelSet(x='Country Name', y='value', text='text', level='glyph',
        x_offset=-30.5, y_offset=10, source=source)

p.add_layout(labels)

p.title.text_font_size = '20pt'
p.title.align = 'center'

p.legend.label_text_font_size = "12pt"
p.yaxis.axis_label_text_font_size = "15pt"
p.yaxis.major_label_text_font_size = "10pt"
p.xaxis.axis_label_text_font_size = "15pt"
p.xaxis.major_label_text_font_size = "10pt"
p.yaxis[0].formatter = NumeralTickFormatter(format="0. a")

p.add_tools(HoverTool(
    tooltips=[
        ("Country name", "@{Country Name}"),
        ("Population", "@value{(0.00 a)}")
    ]
))

p.xgrid.grid_line_color = None

save_bokeh(p, "bokeh_plot4_data1")
