
from bokeh.models import ColumnDataSource, NumeralTickFormatter, Legend, HoverTool
from bokeh.plotting import figure
from utils import save_bokeh
from palmerpenguins import load_penguins
import numpy as np
import pandas as pd

# Read the data
penguins = load_penguins()
species = penguins.species.unique()

new_data= pd.DataFrame()

for species, species_data in  penguins.groupby("species"):
    arr_hist, edges = np.histogram(species_data.body_mass_g, 
                                bins = int(180/5),
                               range = [2400,6400])
    spec_col = [species] * arr_hist.shape[0]
    n_data = pd.DataFrame({"species":spec_col,
                           'mass': arr_hist, 
                       'left': edges[:-1], 
                       'right': edges[1:]})
    new_data = new_data.append(n_data, ignore_index = True)

new_data['f_interval'] = ['%d to %d grams' % (left, right) for left, right in zip(new_data['left'], new_data['right'])]

source = ColumnDataSource(data = new_data)

p = figure(title="Penguins body mass distribution",
           height=500,
            width=1000,
            tools=["wheel_zoom", "box_select", "pan"],
            toolbar_location="below",
            x_axis_label="Penguin body mass [g]",
            y_axis_label="Penguins",)

colors = ["red", "green", "blue"]
for index, (species, species_data) in  enumerate(new_data.groupby("species")):
    count_data = ColumnDataSource(new_data[new_data["species"] == species])
    p.quad(source = count_data, bottom=0, top='mass', 
        left='left', right='right', alpha=0.4,
        fill_color=colors[index], line_color='black', legend_label=species,
        hover_fill_alpha = 1.0)


p.add_tools(HoverTool(
    tooltips=[
        ("Species", "@species"),
        ('Body mass', '@f_interval'),
        ('Num of Penguins', '@mass')
    ]
))

p.legend.click_policy="hide"
p.add_layout(Legend(), 'right')

p.title.text_font_size = '20pt'
p.title.align = 'center'

p.legend.label_text_font_size = "12pt"
p.yaxis.axis_label_text_font_size = "15pt"
p.yaxis.major_label_text_font_size = "10pt"
p.xaxis.axis_label_text_font_size = "15pt"
p.xaxis.major_label_text_font_size = "10pt"
p.yaxis[0].formatter = NumeralTickFormatter(format="0. a")

save_bokeh(p, "bokeh_plot6_data2")
