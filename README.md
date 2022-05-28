
# Surf's Up Ice Cream in Hawaii

## Overview

The purpose of this analysis was to gather climate data for the months of December and June in Hawaii, 
insert the data into a SQLite database, query the data, and finally visualize it and run statistical analysis. 
This was done to provide useful weather information for starting an ice cream business and painting a picture 
of when to expect business to ebb and flow based on the weather.

## Results

A few observations may be made from the weather data collected:

- June temperatures averaged 75°F with no major outliers with which to be concerned. Further, the temperature
swing on either side of the average is quite consistent, with both the positive and negative swing 10°F from 
the average. June temperatures are relatively stable and comfortable with no major swings.

![June_temps](https://github.com/conorwhanson/surfs_up/blob/main/resources/June_temps.png)

- December temperature averaged 4°F cooler than June, coming in at 71°F. The minimum temperature in December was
56°F and the maximum was 83°F. These temperature differences are a little more significant as 56°F is perhaps a
little too cool for ice cream consumption and enjoyment.

![Dec_temps](https://github.com/conorwhanson/surfs_up/blob/main/resources/Dec_temps.png)

- In both December and June the temperatures never stray extremely far from the average, albeit it December the
swing is into temperatures that would likely affect a person's desire to eat ice cream.

## Summary

Based on the above results I would expect to see a high volume of ice cream sales that peaks in or around June,
with sales dipping in the winter months. However, more data is needed beyond temperature. A query to pull the 
precipitation data would be needed, as even hot days can have rain, which would perhaps affect ice cream sales.
A precipitation query below shows some basic statistics. 

![Precipitation_stats](https://github.com/conorwhanson/surfs_up/blob/main/resources/precipitation.png)

Average rainfall is less than 2/10ths of an inch, with the majority of data reporting very low precipitation
overall. However, there are some significant outliers in the data; particularly