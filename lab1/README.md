# Lab 1/2

All of the scripts contained in a "scripts: folder are written in python. They allow to analyze the data pertaining the population sizes in the countries across the world and show them in the form of animated plots. 4 types of charts can be made and saved using them- bar plot, line plot, bubble plot and pie chart. For each of them there are 3 sets of 5 countries that are being analyzed:
* 5 most populated countries in 1960
* 4 countries that have the most similar population to the randomly chosen one in the random year
* 4 countries that have the most similar population to Poland in the random year


## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [License](#license)
* [Author](#author)

## General Information

All of the scripts can be grouped into 2 categories. The first on includes the 'clean_data.py' and 'analyze_data.py'. Both of them are used to prepare the data for the following step which is creating animated plots. They read the data from the .csv files and change them into pandas DataFrames to allow for the easier parsing.
The second group consist of all of the scripts ending with "_plot.py". For each type of plot there is one python script which is used to make them and ensure that they are readable.

All of those scripts and functions in them are being called in the "main.py" file which allows for the easier usage.

## Usage
To run the script simply make sure that you have the needed files in the "data" folder and the move to the "scripts" catalogue. Then use the following command which will create the plots and save them to the "images" folder.

```python 
python main.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
Zofia Kochańska
