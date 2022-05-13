
![SQLAlchemy readme image](https://user-images.githubusercontent.com/93561950/167983797-7e344aac-2890-44c1-9870-a737d146599b.png)

# SQLAlchemy Challenge Summary
Climate Analysis and Exploration of precipitation and temperature data in Hawaii using SQLAlchemy ORM. Results show a strong correlation between time of year and temperature. Flask API created from SQLAlchemy queries with both static and dynamic routes. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)


## General Information
- This project analyzes preciptation and temperature data from Hawaii. 
- Using the API created, you can enter any date or range of dates to retreive the minimum temperature, average temperature, and maximum temperature in Hawaii during that time based on historical weather data. 

## Technologies Used
- Python
- Matplotlib
- SQLAlchemy
- Flask
  
## Features
Notebooks:
- climate.ipynb -  Using SQLAlchemy ORM, queries are made from a SQLite file with Hawaii climate data.
- temp_analysis_1.ipynb - Further exploration and visualization of climate analysis with specific timeframes. 
- temp_analysis_2.ipynb - Further exploration and visualization of climate analysis with specific timeframes. 
- app.py - Climate data API created using Flask.


## Screenshots
![waiheetempgraph](https://user-images.githubusercontent.com/93561950/168341807-724fc785-1d30-416d-af17-1e3befbc2cd9.png)

The Waihee Station is the most active station in the dataset, temperatures visualized above. 
  
![precipitationgraph](https://user-images.githubusercontent.com/93561950/168342028-9de65067-fcc9-44ec-8568-5a498e9a1f36.png)

Precipitation charted over a one year period from August 2016 to August 2017. August-September reveals the highest precipitation. 

## Setup
Code was tested using Python 3.8.  The environment also needs pandas and matplotlib. 

The environment was setup as follows:

  <!-- Unordered List (bullet pointed) -->
  <ul>
    <li>conda install pandas</li>
    <li>conda install matplotlib</li>
    <li>conda create -n envpy38 python=3.8 anaconda</li>
    <li>source activate envpy38</li>
    <li>jupyter notebook</li>
  <br>

## Data Source
Data found in resources/hawaii-measurements.csv and resources/hawaii-stations.csv.
