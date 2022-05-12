# SQLAlchemy-Challenge
Climate Analysis and Exploration using SQLAlchemy of precipitation and temperature data in Hawaii. Results show a strong correlation between time of year and temperature. 

![SQLAlchemy readme image](https://user-images.githubusercontent.com/93561950/167983797-7e344aac-2890-44c1-9870-a737d146599b.png)

## Methods Used
Barplot, Statistic Summaries, T-test

## Technologies
Python, Matplotlib, SQLAlchemy, SQLite, Flask

## Featured Notebooks
  <!-- Unordered List (bullet pointed) -->
  <ul>
    <li>climate.ipynb</li>
    <li>temp_analysis_1.ipynb</li>
    <li>Stemp_analysis_2.ipynb</li>
    <li>app.py</li>
  </ul>

Climate notebook - Using SQLAlchemy ORM, queries are made from a SQLite file with Hawaii climate data.
Temperature analysis 1 & 2 - Further exploration and visualization of climate analysis with specific timeframes. 
App.py - Climate data API created using Flask.

## Data Source
Data found in resources/hawaii-measurements.csv and resources/hawaii-stations.csv.

## Installation
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


