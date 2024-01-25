This program is an application to display a pie graph represntation of information related to top 10 countries in 
Fossil CO2 Emissions '2017 (% of world)' column from the website "https://en.wikipedia.org/wiki/
List_of_countries_by_carbon_dioxide_emissions".
This file imports from  module matplotlib and the module pandas.
This file also imports from  BackEnd_2 the modules Scrapedata and Database.

This file is the frontend, which Extracts the top 10 countries data from the database and displays a pie-plot. 
Using the database passed from the backend, it sorts the data and displays the percentage contribution 
of top10 countries in a pie graph prepared using pandas dataframe of the pandas module of Python.
'''
This program is the backend part of a GUI application to display webscraped information in a pie graph.  

This file is the BackEnd, which contains all the programs required to run the FrontEnd. 
This file imports from  modules sqlite3,requests, and BeautifulSoup.


This program is regarding webscraping of the data from the website "https://en.wikipedia.org/wiki/
List_of_countries_by_carbon_dioxide_emissions", using Beautiful Soup and displaying it in a pie plot. from the web
This program contains objects from two classes, class Sqlite and class Mplotlib. The object from Sqlite class
is the database that stores data read from an html file 'Temperature.html'. This object is made in the 
constructor method of the next class Mplotlib and different methods of Sqlite class are called on it.
Mplotlib class contains different methods of its own that construct different types of graphs based on the data 
read from the html file.

The graphs are displayed when the methods of the objects of  Mplotlib class are called on its object in the 
FrontEnd file.
