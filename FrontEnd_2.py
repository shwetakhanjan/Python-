#  Shweta_Khanjan_Shroff 

# FrontEnd 

'''
This program is an  application to display a pie graph represntation of information related to top 10 countries in
Fossil CO2 Emissions '2017 (% of world)' column from the website "https://en.wikipedia.org/wiki/
List_of_countries_by_carbon_dioxide_emissions".
This file imports from  module matplotlib and the module pandas.
This file also imports from  BackEnd_2 the modules Scrapedata and Database.

This file is the frontend, which Extracts the top 10 countries data from the database and displays a pie-plot. 
Using the database passed from the backend, it sorts the data and displays the percentage contribution 
of top10 countries in a pie graph prepared using pandas dataframe of the pandas module of Python.
'''

import pandas as pd
import matplotlib.pyplot as plt
from BackEnd_2 import  Database



class Plotdata:
    '''Plots the data from SQLite dtabase table into a pie plot'''
    def __init__(this):  #constructor
           
        this._sqlitedbase = Database() #Object of Sqlite class
        this._sqlitedbase.connectTable()      #Method call of Sqlite class Object
        this._sqlitedbase.createTable()
        this._sqlitedbase.insertTable()
        this.dataList = this._sqlitedbase.fetch()
         
        this._fullList = [row for row in this.dataList]   #Obtaining and storing data from Sqlite class Object
        this._fullList.sort(key=lambda x: x[1])     #Sorting the data 
        this._fullList1 = (this._fullList[::-1])    #Sorting the data    
        this._countryList = [this._fullList1[i][0] for i in range(10)] # Extracting the top 10 countries data
          
        this._valueList = [this._fullList1[p][1] for p in range(10)]  # Extracting the top 10 countries data
        
        this._sqlitedbase.closeTable()      #Closing the connection to Sqlite table 
    
    
    def piePlot(this):
        
        '''Draw a pie Plot'''
        
        
        df = pd.DataFrame(this._valueList, index=this._countryList, columns=['x'])
        df.plot.pie(subplots=True)
        
        plt.title('Top 10 fossil CO2 emissions by country/region : 2017 (% of the world)')
        plt.show()
        
Plotdata().piePlot()
    


