# Lab 4-5

All of the scripts contained in a "scripts" folder are written in python. They allow to analyze the data pertaining the temperatures across the years in 8 different countries and show them in the form of plots. 4 types of charts can be made and saved using them- scatter plot, box plot, line plot and line plot with subplots. 


## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [License](#license)
* [Author](#author)

## General Information

All of the scripts can be grouped into 2 categories. The first on includes the 'clean_data.py', 'analyze_data.py'. Two of them are used to prepare the data for the following part of the workflow- plotting the data. They read the data from the .csv file and change them into pandas DataFrames to allow for the easier parsing.
The second group consist of all of the scripts starting with 'task'. For each type of plot there is one python script which is used to make them and ensure that they are readable.

All of those scripts and functions in them are called in the 'main.py' file which allows for the easier usage, while the 'utils.py' file contains the functions commonly used amongst the scripts.

## Usage
To run the script simply make sure that you have the needed files in the "data" folder and then move to the 'scripts' catalogue. Then use the following command which will create all of the plots. It is also possible to chose wether to save them to the 'images' folder or display them based on the additional argument (1 for saving them and 0 for displaying them). If no value is provided then the plots will be automatically saved to the 'images' folder. 

```python 
python main.py 0                            #displays the plots
python main.py 1[/anything_else]            #saves the plots
```
It is also possible to run the separate scripts responsible for different plots. To do it simply replace the "main.py" withe the name of the script you wish to run

```python 
python [script_name].py 0                   #displays the plots
python [script_name].py 1[/anything_else]   #saves the plots
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
Zofia Kochańska
