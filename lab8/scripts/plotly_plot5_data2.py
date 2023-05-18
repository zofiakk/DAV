from utils import save_interactive
import plotly.express as px
from palmerpenguins import load_penguins


# Read the data
penguins = load_penguins()


fig = px.scatter(penguins, x="bill_length_mm", y="bill_depth_mm", color="species",
                                  labels={
                     "bill_length_mm": "Bill Length (mm)",
                     "bill_depth_mm": "Bill depth (mm)",
                     "species": "Penguin species"
                 },
)


# Modify the layout
fig.update_layout(
    font=dict(size=15),
    xaxis_title="Bill length [mm]",
    yaxis_title="Bill depth [mm]",
    title={
        'text': "Penguins bill width vs bill depth",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},)


save_interactive(fig, "plotly_plot5_data2")
    