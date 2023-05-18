import sys
import plotly.graph_objects as go
import pandas as pd
import pygal
from bokeh.plotting import figure, show, output_file, save

def save_interactive(fig: go.Figure, name: str):
    """Function which allows to display or save
    the interactive figure to correct folder

    :param fig: Figure which is to be saved
    :type fig: go.Figure
    :param name: Name of the output file
    :type name: str
    """
    args = sys.argv
    if len(args) > 1:
        if args[1] == "1":
            path = "../images/"
            fig.write_html(f"{path}{name}.html")
            print(f"The plot was saved to {path}{name}.html")
        elif args[1] == "0":
            fig.show()
    else:
        fig.show()

def save_pygal(fig:pygal.Line, name:str):
    """Function for saving plots made by pygal
    
    :param fig: Figure which is to be saved
    :type fig: pygal.Line
    :param name: Name of the output file
    :type name: str
    """
    args = sys.argv
    if len(args) > 1:
        if args[1] == "1":
            path = "../images/"
            fig.render_to_file(f"{path}{name}.svg")
            print(f"The plot was saved to {path}{name}.svg")
        elif args[1] == "0":
            fig.render_in_browser()
    else:
        fig.render_in_browser()


def save_bokeh(fig:figure, name:str):
    """Function for saving plots made by bokeh

    :param fig: Bokeh figure which is to be saved
    or displayed
    :type fig: figure
    :param name: Name of the output file
    :type name: str
    """
    args = sys.argv
    if len(args) > 1:
        if args[1] == "1":
            path = "../images/"
            output_file(filename=f"{path}{name}.html", mode='inline')
            save(fig)
            print(f"The plot was saved to {path}{name}.html")
        elif args[1] == "0":
            show(fig)
    else:
        show(fig)


def get_population_data(path:str,
                        countries:list=["Poland", "Czechia", "Germany",
                                        "Slovak Republic", "Belarus",
                                        "Ukraine", "Lithuania"])->pd.DataFrame:
    """Function for reading csv files to
    DataFrame and subsetting it to contain
    only some countries

    :param path: Name of the csv input file
    :type path: str
    :param countries: Countries to choose
    from the csv file
    :type countries: list
    :return: Smaller data
    :rtype: pd.DataFrame
    """
    # Read the data and choose its subset
    data = pd.read_csv(path)
    data = data[data["Country Name"].isin(countries)]
    data = data.fillna(method="ffill")
    data = data.melt(id_vars=["Country Code", "Country Name"])
    return data
