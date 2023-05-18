import pygal
from utils import save_pygal
from pygal.style import Style
from palmerpenguins import load_penguins
import numpy as np


# Read the data
penguins = load_penguins()

custom_style = Style(
  background='transparent',
  label_font_size=16,
  legend_font_size=20,
  title_font_size= 25,
  value_label_font_size =12,
  tooltip_font_size=20,
  major_label_font_size = 16,)

new_data =pd.DataFrame()
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
    
pygal_histogram  = pygal.Histogram(height=450, width=1100,
                        style=custom_style)

pygal_histogram.title = 'Penguin body mass distribution'

for index, (species, data_for_species) in enumerate(new_data.groupby("species")):
    
    bars = [(height, edges[i], edges[i+1]) for i, height in enumerate(data_for_species.mass)]
    pygal_histogram.add(species, bars)

pygal_histogram.value_formatter = lambda x: "%.2f" % x


pygal_histogram.y_title = 'Number of penguins'
pygal_histogram.x_title = 'Body mass(g)'


save_pygal(pygal_histogram, "pygal_plot6_data2")
