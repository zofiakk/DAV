from utils import save_interactive
import plotly.express as px
from palmerpenguins import load_penguins


# Read the data
penguins = load_penguins()

fig = px.histogram(penguins, x="body_mass_g", color="species",
                   opacity=0.7,  barmode="overlay",
                   labels={
                       "body_mass_g": "Body mass (g)",
                                      "species": "Penguin species"
                   },
                   )

fig.update_xaxes(range=[2400, 6400])

# Modify the layout
fig.update_layout(
    font=dict(size=15),
    xaxis_title="Body mass [g]",
    yaxis_title="Number of penguins",
    title={
        'text': "Penguins body mass distribution",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},)


save_interactive(fig, "plotly_plot6_data2")
