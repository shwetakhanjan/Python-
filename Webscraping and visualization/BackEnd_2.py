#  Shweta_Khanjan_Shroff 

# BackEnd 

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
'''


list1 = []
list2 = []


import re
import sqlite3
import requests
from bs4 import BeautifulSoup


DEFAULT_URL = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"
class Scrapedata:
    
    '''Scrapes the required data from a webpage'''
   
    
    def __init__(self):   
        self._req = requests.get(DEFAULT_URL)
        
    def getData(self):
        try:
            soup = BeautifulSoup(self._req.text,'html.parser')
        
            data = soup.find_all('tbody')[1].find_all('tr')
            for group in data[5:]:
                list1.append((group.find_all('td')[0].get_text().strip(),group.find_all('td')[4].get_text()))
            for i in range(len(list1)):
                m = re.search('(\d+.\d+)',list1[i][1])
                list2.append((list1[i][0],float(m.group())))
            return (list2)
        except:
            raise IOError("Input file not opened")
        
        

        
class Database:
    '''Stores data in an SQLite dtabase table'''
    
    def __init__(self):  #constructor
        
        self._sqConnect = sqlite3.connect('SQLite_Data.db')
        self._cursor = self._sqConnect.cursor() 
        self._data = Scrapedata().getData()
        
    def  connectTable(self):
        
        '''Connects to an existing database or creates a new database and connects to it '''
                       
        if (self._sqConnect): 
            
            return True
        
        else:
            return False
        

    
    def  createTable(self):
        
            '''Creates a table format within the database'''
            
            
            sqlite_create_table_query = ''' DROP TABLE 'CO2_DATA';''' 
            sqlite_create_table_query_1 = ''' CREATE TABLE 'CO2_DATA'                                       
                                                (  country TEXT primary key,
                                                   percentage REAL);'''              
                
            try:                       
                sqliteTable = self._cursor.execute(sqlite_create_table_query)  # Exception handling if table already exists 
                sqliteTable_1 = self._cursor.execute(sqlite_create_table_query_1)
                
            except:
                sqliteTable_1 = self._cursor.execute(sqlite_create_table_query_1)
            
            self._sqConnect.commit()
            
            if sqliteTable_1 :
                
                return True
    
        
            else:
                
                return False
    
    def insertTable(self):
        
        '''Insert data values into table'''
    
        sqlite_insert_query = """ INSERT INTO CO2_DATA
                                  (country, percentage) VALUES (?, ?)"""
                                         

              
        sqliteInsert = self._cursor.executemany(sqlite_insert_query,(self._data))    
        self._sqConnect.commit()
        
        if sqliteInsert :
    
            return True
    
        else:
    
            return False


    def fetch(self):
        
        '''Fetch the data from table'''
        
        
        sel = 'SELECT country, percentage  FROM CO2_DATA '
    
        fetchData = self._cursor.execute(sel)
        
        if fetchData :
    
            return fetchData
    
        else:
    
            return False
             
    def closeTable(self):
        
        '''Close the existing database connection when called in another class
        after data from the table is read in another class'''
    
        closeTable=self._cursor.close()
        if closeTable :
            return True
        else:
            return False         
      

