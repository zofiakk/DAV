import plotly.graph_objects as go
from utils import save_interactive, get_population_data
import plotly.express as px


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")
data = data[data["variable"] == "2010"]

fig = go.Figure()

# Create the plot
fig = px.pie(data, values='value', names='Country Name',
             labels={'value':"Population", 'Country Name':"Country"})


fig.update_traces(textposition='outside', textinfo='percent+label',
                  hoverinfo="percent+name")

# Modify the layout
fig.update_layout(
    font=dict(size=15),
    xaxis_title="Year",
    yaxis_title="Country population [mln]",
    legend_title_text='Country',
    title={
        'text': "Population in Poland and its neighbors in 2010",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},)


save_interactive(fig, "plotly_plot3_data1")
    