## SQLAlchemy and Flask Project

### Objective:
Use Python and SQLAlchemy ORM queries with provided hawaii.sqlite database to reflect tables into a new model and perform analysis of Hawaii climate.
Build a Flask Web app using the served queries that will return JSONified query results from API endpoints.

Technologies Used: SQLAlchemy, Python, Pandas, Matplotlib and FLASK
Design a Flask API Web Climate App - app.py

### Climate Analysis and Exploration
Python and SQLAlchemy were used to explore the climate database.

Used SQLAlchemy create_engine to connect to your sqlite database.
Used SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.

### Precipitation Analysis
Designed a query to retrieve the last 12 months of precipitation data.
Filtered only the date and precipitation values.
Loaded the query results into a Pandas DataFrame and set the index to the date column.
Sorted the DataFrame values by date.
Plot the results using Matplotlib.
Create a summary statistics for the precipitation data. prcp

### Weather Station Analysis
Designed a query to calculate the total number of stations.
Designed a query to find the most active stations.
Listed the stations and observation counts in descending order.
Found out which station has the highest number of observations.
Designed a query to retrieve the last 12 months of temperature observation data (tobs).
Filter by the station with the highest number of observations.
Plot the results as a histogram with bins=12. hist

### Temperature Analysis
Defined a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d and return the minimum, average, and maximum temperatures for that range of dates.

Used the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

Plot the min, avg, and max temperature from your previous query as a bar chart.

Daily Rainfall Average.
Calculated the rainfall per weather station using the previous year's matching dates.

Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.

Defined a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d.

Created a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.

Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.

Used Pandas to plot an area plot (stacked=False) for the daily normals.

Area_plot to visualize daily normals from a Pandas DataFrame

## Climate App

Design a Flask API based on the queries that were developed previously to retrieve data from the web and the database.
Used FLASK to create routes to other HTML.
Used Flask jsonify to convert your API data into a valid JSON response object.

Home page.
/api/v1.0/precipitation

Return the JSON representation of your dictionary.
/api/v1.0/stations

Return a JSON list of stations from the dataset.
/api/v1.0/tobs

query for the dates and temperature observations from a year from the last data point.
Return a JSON list of Temperature Observations (tobs) for the previous year.
/api/v1.0/<start> and /api/v1.0/<start>/<end>

![image](https://user-images.githubusercontent.com/70984918/120257232-71ab6a00-c255-11eb-8afc-4c22b54a82ed.png)
  

### Station Analysis

Histogram of 12 months of temperature observation data
![image](https://user-images.githubusercontent.com/70984918/120257247-7c65ff00-c255-11eb-8942-01ba26446a3c.png)

