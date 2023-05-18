import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from utils import load_data, parse_args


def main():
    """Function used to simplify the process of saving the plot
    """
    _, data = load_data()
    args = parse_args()
    countries = data.Country.unique()
    for country in countries:
        make_scatter(data, country, save=args.display)


def make_scatter(data:pd.DataFrame, country:str, save:bool):
    """Function used to create the scatter plot
    showing average temperatures across
    the years in a chosen country

    :param data: Data containing the calculated averages
    :type data: pd.DataFrame
    :param country: Name of country which is to be plotted
    :type country: str
    :param save: Whether to save or display the plot
    :type save: bool
    """

    data = data[data["Country"] == country]
    sns.set_theme()
    sns.set_style("darkgrid")
    fig = plt.figure(figsize=(14, 8))
    plt.scatter(
        x=data['year'], y=data['AverageTemperatureCelsius'], color='black', marker='.')
    plt.xlabel("Year", fontsize=20)
    plt.ylabel("Average Year Temperature [C]", fontsize=20)
    plt.title(f"Average temperature across the years in {country}", fontsize=34)
    plt.xticks(fontsize=15, rotation=90)
    plt.yticks(fontsize=15)
    fig.tight_layout()
    
    # Change axis bounds
    plt.xlim([1740, 2015])
    plt.ylim([-5, 24])
    plt.locator_params(axis='x', nbins=30)
    plt.subplots_adjust(top=0.94, bottom=0.12)
    
    # Save or display the plot
    if save:
        path = "../images/"
        plt.savefig(path + country.replace(" ", "_") + ".png")
        plt.clf()
        plt.close()
    else:
        plt.show()
        plt.close()

if __name__ == '__main__':
    main()
