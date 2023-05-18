# Lab 8

All of the scripts contained in a 'scripts' folder are written in Python. They serve the purpose of creating six types of interactive plots using three different Python libraries. They are used to present two different datasets - one contains information about populations across the years of different countries while the other one characterizes three penguin species. It is possible to save created plots by using an additional argument while calling the scripts.


## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [License](#license)
* [Author](#author)

## General Information

All of the scripts can be grouped into 2 categories. The first on consists of the 'utils.py' file.It is used to prepare the data for the following part of the workflow- plotting the data as well as saving them to separate files. This file contains all of the functions widely used across the different scripts to reduce code redundancy. 

The second group consist of all of the scripts following this naming system <library_name>_plot<nb>_data<nb>.py. For each type of plot there is one python script which is used to make them and ensure that they are readable.


## Usage
To run the scripts simply make sure that you have the needed files in the "data" folder and then move to the 'scripts' catalogue. Then use the following command which will create all of the plot. It is also possible to chose wether to save it to the 'images' folder or display it based on the additional argument (1 for saving them and 0 for displaying them). If no value is provided then the plots will be automatically displayed. 

```python 
python <script_name>.py 0                            #displays the plot
python <script_name>.py 1[/anything_else]            #saves the plot
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
Zofia Kochańska
