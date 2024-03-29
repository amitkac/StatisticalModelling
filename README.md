


[![License](https://poser.pugx.org/ali-irawan/xtra/license.svg)](https://poser.pugx.org/ali-irawan/xtra/license.svg)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-373/)


# Statistical Modelling with AIC_c test
 Before you go ahead with the setup, check this cool image out. This is the magic of ` Holoviews -Bokeh` plot.
 
![](img/Screen2.png)


## Table of contents
* [General info](#general-info)
* [Prerequisites](#technologies)
* [Setup](#setup)
* [Sample output](#sample-output)

## General info
This is a simple modular python code to statistically model any data, and check the distribution to which it fits. 
The output is rendered as a `.html` page, which can be saved as `.svg` or `.png`. 

So, what exactly is Akaike Information Criteria (AIC)? especially AIC_c (AIC corrected). For that, check out these cool resources:
*  Wikipedia- (https://en.wikipedia.org/wiki/Akaike_information_criterion)
*  Data Science- (https://www.statisticshowto.datasciencecentral.com/akaikes-information-criterion/)

The overall basic idea is to estimate the given distribution parameters using **MLE**, plot the corresponding pdf, and then find out how close is the estimated ditribution close to real distribution using the AIC metric.

## Citation

If you are using this repo or a part of it for your research, kindly consider citing the following paper,

```
@ARTICLE{8726308,
  author={Kachroo, Amit and Vishwakarma, Surbhi and Dixon, Jacob N. and Abuella, Hisham and Popuri, Adithya and Abbasi, Qammer H. and Bunting, Charles F. and Jacob, Jamey D. and Ekin, Sabit},
  journal={IEEE Access}, 
  title={Unmanned Aerial Vehicle-to-Wearables (UAV2W) Indoor Radio Propagation Channel Measurements and Modeling}, 
  year={2019},
  volume={7},
  number={},
  pages={73741-73750},
  doi={10.1109/ACCESS.2019.2920103}}

```
	
## Technologies
Project is created with:
* python: 3.x
* Holoviews-bokeh: install with ```python $conda install holoviews ```
* Pandas: install with ```$conda install pandas```
* Scipy 
* Numpy
	
## Setup
To run this project, download the repository to any folder. Open the folder and run the following commands from command line:
```
$python3 -W ignore mainCall.py -f 'path-to-the-csv-file' -c 1 -sr 3
```
`-f` is the complete filepath,`-c` is the column number to be read ( remember python is *0 indexed* ), and 
`-sr` is the number of rows to skip (text or header)
`W ignore` ignoring the warning caused by division by zero errors for some distributions

By default, it will read 1<sup>st</sup> column, and will skip 1<sup>st</sup> row as a header. Here is the sample cmd:

![Cmd](img/Screen3.png)

## Sample output

The output `Bokeh Plot` as an `.html` should look like the below image,  with all the distribution plots. Now, don't forget to try `Pan`, `Box Zoom`, and **my favorite** ` Wheel Zoom`.  Check out the cool `.gif` below, where wheel zooming the data changes all the fitted distributions, and thus removing the need to recode your data.

<img src= "img/out2.gif" > 



