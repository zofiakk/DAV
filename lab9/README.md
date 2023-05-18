# Lab 10

All of the scripts contained in a 'scripts' folder are written in Python. They are used to analyze the temperatures in some countries and forecast them. All of the plots and models are based on the single .csv file stored in 'data' folder, which is then accordingly modified. The last script in this project serves the purpose of analyzing the fitness of the created models and creates a csv table which can be saved tp the'data' folder by using an additional argument.


## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [License](#license)
* [Author](#author)

## General Information

All of the scripts are written using python and can by grouped into 2 categories the first one consists off all of the files named following "task<nb>.py" convention. Only those script should be used and and as such are easily callable. All of the other scripts, not following such naming contain the supporting functions used to for example, clean the data or parse command line arguments.


## Usage
To run the scripts simply make sure that you have the needed files in the "data" folder and then move to the 'scripts' catalogue. Then use the following command which will create all of the plots and a table. It is also possible to chose wether to save it to the 'images' or 'data' (in case of task4) folder or display it based on the additional argument (1 for saving them and 0 for displaying them). If no value is provided then the plots will be automatically saved. 

```python 
python <script_name>.py 0                            #displays the plot
python <script_name>.py 1[/anything_else]            #saves the plot
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
Zofia Kochańska
