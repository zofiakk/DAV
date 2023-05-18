import plotly.graph_objects as go
from utils import save_interactive, get_population_data


# Read the data and choose its subset
data = get_population_data("../data/clean_data.csv")
data = data[data["variable"] == "2010"]

fig = go.Figure()

text = round(data.value/1000000, 2).to_list()
text = [str(i) + " mln" for i in text]

fig.add_traces(go.Bar(
                x=data["Country Name"],
                y=round(data.value/1000000, 2),
                marker_color=['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                       'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                       'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                       'rgb(227, 119, 194)',],
                text=text,
                hovertemplate="Country: %{x}<br>Population: %{y:.2f} mln<br><extra></extra>",
                visible=True))

# Modify text above bars
fig.update_traces(textfont_size=16, textangle=0,
                  textposition="outside",
                  cliponaxis=False
                  )

# Modify the layout
fig.update_layout(
    font=dict(size=15),
    xaxis_title="Countries",
    yaxis_title="Country population [mln]",
    title={
        'text': "Population in Poland and its neighbors in 2010",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},)


save_interactive(fig, "plotly_plot4_data1")
    