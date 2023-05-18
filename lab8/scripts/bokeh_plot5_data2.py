from bokeh.plotting import figure
from utils import save_bokeh
from bokeh.models import HoverTool, Legend, ColumnDataSource, NumeralTickFormatter
from palmerpenguins import load_penguins


# Read the data
penguins = load_penguins()

# Add the color column
colormap = {'Adelie': 'red', 'Chinstrap': 'green', 'Gentoo': 'blue'}
colors = [colormap[x] for x in penguins['species']]
penguins["colors"] = colors

p = figure(title="Penguins bill length vs bill depth",
           height=500,
            width=1000,
            tools=["wheel_zoom", "box_select", "pan"],
            toolbar_location="below",
            x_axis_label="Bill length [mm]",
            y_axis_label="Bill depth [mm]",)

source = ColumnDataSource(data=penguins)
for species, species_data in  penguins.groupby("species"):
    count_data = ColumnDataSource(penguins[penguins["species"] == species])
    colors = [colormap[x] for x in species_data['species']]
    p.scatter(x = "bill_length_mm", y= "bill_depth_mm",
            color="colors", fill_alpha=0.2, size=10, legend_label=species,
            source=count_data)

p.add_layout(Legend(), 'right')

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
        ("Species", "@species"),
        ("Bill length", "@bill_length_mm{(0.0)}"),
        ("Bill depth", "@bill_depth_mm{(0.0)}"),
    ]
))

p.legend.click_policy="hide"

save_bokeh(p, "bokeh_plot5_data2")
