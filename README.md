


[![License](https://poser.pugx.org/ali-irawan/xtra/license.svg)](https://poser.pugx.org/ali-irawan/xtra/license.svg)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-373/)


# Statistical Modelling with AIC_c test



## Table of contents
* [General info](#general-info)
* [Prerequisites](#technologies)
* [Setup](#setup)
* [Sample output](#output)

## General info
This is a simple modular python code to statistically model any data, and check the distribution to which it fits. 
The output is rendered as a `.html` page, which can be saved as `.svg` or `.png`. 
	
## Technologies
Project is created with:
* python: 3.x
* Holoviews-bokeh: install with ```python $conda install -c pyviz holoviews bokeh ```
* Pandas: install with ```conda install pandas```
* Scipy 
* Numpy
	
## Setup
To run this project, download the repository to any folder. Open the folder and run the following commands from command line:
```
$python3 mainCall.py -f 'path-to-the-csv-file' -c 1 -sr 3
```
`-f` is the complete filepath,`-c` is the column number to be read ( remember python is *0 indexed* ), and 
`-sr` is the number of rows to skip (text or header)

By default, it will read 1<sup>st</sup> column, and will skip 1<sup>st</sup> row as a header.

## Sample output
