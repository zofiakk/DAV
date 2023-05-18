import plotly.graph_objects as go
from utils import save_interactive, get_population_data


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")

fig = go.Figure()

# Create the plot
for country, data_for_country in data.groupby("Country Name"):
    fig.add_scatter(x=data_for_country.variable,
                    y=data_for_country.value,
                    name=country, mode='lines+markers',
                    line=dict(width=2),
                    marker=dict(size=5),
                    hovertemplate="Year: %{x}<br>Population: %{y}",)


# Modify the layout
fig.update_layout(
    font=dict(size=15),
    xaxis_title="Year",
    yaxis_title="Country population [mln]",
    legend_title_text='Country',
    title={
        'text': "Population in Poland and its neighbors across the years",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},)

save_interactive(fig, "plotly_plot1_data1")
    