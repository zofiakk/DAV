from bokeh.plotting import figure
from utils import get_population_data, save_bokeh
from bokeh.models import HoverTool, NumeralTickFormatter, Legend, Whisker, ColumnDataSource
import pandas as pd
from bokeh.transform import factor_cmap
import warnings
warnings.filterwarnings('ignore')


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv", ["Kenya", "Argentina", "Tanzania", "Poland", "Colombia"])
kinds = data["Country Name"].unique()


# compute quantiles
qs = data.groupby("Country Name").value.quantile([0.25, 0.75])
qs = qs.unstack().reset_index()
qs.columns = ["Country Name", "q1", "q3"]
data2 = pd.merge(data, qs, on="Country Name", how="left")

# compute IQR outlier bounds
iqr = data2.q3 - data2.q1
data2["upper"] = data2.q3 + iqr
data2["lower"] = data2.q1 - 0.4*iqr

groups = data.groupby("Country Name")
q1 = groups.quantile(q=0.25)
q2 = groups.quantile(q=0.5)
q3 = groups.quantile(q=0.75)
iqr = q3 - q1
upper = q3 + iqr
lower = q1 - 0.4 * iqr

boxes_data = pd.concat([
    q1.rename(columns={"value":"q1"}),
    q2.rename(columns={"value":"q2"}),
    q3.rename(columns={"value":"q3"}),
    iqr.rename(columns={"value":"iqr"}),
    lower.rename(columns={"value":"lower"}),
    upper.rename(columns={"value":"upper"})
], axis=1)

source = ColumnDataSource(data=boxes_data)


p = figure(x_range=kinds, 
           y_range = (0, 78000000),
           title="Population of Poland and 4 other countries across the years",
           x_axis_label="Years", y_axis_label="Country population\n[mln]",
           height=500,
            width=1000,
            tools=["wheel_zoom", "box_select", "pan"],
            toolbar_location="below")
p.add_layout(Legend(), 'right')

cmap = factor_cmap("Country Name", "Category10_10", kinds)

top_box = p.vbar(
    "Country Name", 0.7, "q2", "q3",
    line_color="black", source=source, color=cmap)

bottom_box = p.vbar(
    "Country Name", 0.7, "q1", "q2", 
    line_color="black", source=source, color=cmap)

# outlier range
whisker = Whisker(base="Country Name", upper="upper", lower="lower", source = source)
whisker.upper_head.size = whisker.lower_head.size = 20
p.add_layout(whisker)


# outliers
outliers = data2[~data2.value.between(data2.lower, data2.upper)]
p.scatter("Country Name", "value", source=outliers, size=6, color="black", alpha=0.3)


p.title.text_font_size = '20pt'
p.title.align = 'center'

p.legend.label_text_font_size = "12pt"
p.yaxis.axis_label_text_font_size = "15pt"
p.yaxis.major_label_text_font_size = "10pt"
p.xaxis.axis_label_text_font_size = "15pt"
p.xaxis.major_label_text_font_size = "10pt"
p.yaxis[0].formatter = NumeralTickFormatter(format="0. a")

p.xgrid.grid_line_color = None


p.add_tools(HoverTool(
    renderers=[top_box, bottom_box],
    tooltips=[
        ('Country', '@{Country Name}'),
        ('q1', '@q2{(0.00 a)}'),
        ('q2', '@q1{(0.00 a)}'),
        ('q3', '@q3{(0.00 a)}'),
        ('iqr', '@iqr{(0.00 a)}'),

    ]
))

save_bokeh(p, "bokeh_plot2_data1")
