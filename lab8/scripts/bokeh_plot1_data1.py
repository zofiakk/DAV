from bokeh.plotting import figure, ColumnDataSource
from utils import get_population_data, save_bokeh
from bokeh.models import HoverTool, NumeralTickFormatter, Legend
from bokeh.palettes import Category10_10


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")


source = ColumnDataSource(data=data)


p = figure(title="Population in Poland and its neighbors across the years",
           x_axis_label="Years", y_axis_label="Country population\n[mln]",
           height=500,
            width=1000,
            tools=["wheel_zoom", "box_select", "pan"],
            toolbar_location="below")
p.add_layout(Legend(), 'right')


for index, (country, data_for_country) in enumerate(data.groupby("Country Name")):
    count_data = ColumnDataSource(data[data["Country Name"] == country])
    p.line(x = "variable", y = "value",
           legend_label=country, color = Category10_10[index], source=count_data, line_width=2)
    p.circle(x = "variable", y = "value",
             line_color = Category10_10[index], fill_color= Category10_10[index],
             size=4, source=count_data, legend_label=country)

p.title.text_font_size = '20pt'
p.title.align = 'center'

p.legend.label_text_font_size = "12pt"
p.yaxis.axis_label_text_font_size = "15pt"
p.yaxis.major_label_text_font_size = "10pt"
p.xaxis.axis_label_text_font_size = "15pt"
p.xaxis.major_label_text_font_size = "10pt"
p.yaxis[0].formatter = NumeralTickFormatter(format="0. a")

p.legend.click_policy="hide"


p.add_tools(HoverTool(
    tooltips=[
        ( 'Year',   '@variable'            ),
        ("Country name", "@{Country Name}"),
        ("Population", "@value{(0.00 a)}")
    ]
))


save_bokeh(p, "bokeh_plot1_data1")
