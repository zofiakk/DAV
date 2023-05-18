import plotly.graph_objects as go

from utils import save_interactive, get_population_data

# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv", ["Kenya", "Argentina", "Tanzania", "Poland", "Colombia"])

fig = go.Figure()

# Create the plot
for country, data_for_country in data.groupby("Country Name"):
    fig.add_trace(go.Violin(y=data_for_country.value,
                            name = country,
                            box_visible=True,
                            meanline_visible=True, 
                            opacity=0.5))
    
# Modify the layout
fig.update_layout(
    font=dict(size=15),
    xaxis_title="Year",
    yaxis_title="Country population [mln]",
    legend_title_text='Country',
    title={
        'text': "Population in Poland and 4 other countries across the years",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},)


save_interactive(fig, "plotly_plot2_data1")