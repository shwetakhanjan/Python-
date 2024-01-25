
'''
This program fetches data from a website using Webscraping  and insrets it into an sqlite database.
It uses multithreading  for 6 sub agents used to fetch data from the sqlite table.

Thus the concepts of Webscraping and multithreading are reinforced in this exercise.
This file is the the backend and does not interact with the user.
'''

import sqlite3
import requests
from bs4 import BeautifulSoup
import threading
import time    

DEFAULT_SITE = "https://www.esrl.noaa.gov/gmd/aggi/aggi.html"

class Scrapedata:
    
    '''Webscraping  the data from the website'''
    
    def __init__(self):
        
        self._req = requests.get(DEFAULT_SITE)
        
    def getData(self):
        '''Get data and return a list'''
        try:
            list1 = []
            soup = BeautifulSoup(self._req.text,'html.parser')
            data = soup.find_all('tbody')[1].find_all('tr')
            for group in data[2:]:
                list1.append((group.find_all('td')[0].get_text().strip(),\
                              group.find_all('td')[1].get_text().strip(),\
                              group.find_all('td')[2].get_text().strip(),\
                              group.find_all('td')[3].get_text().strip(),\
                              group.find_all('td')[4].get_text().strip(),\
                              group.find_all('td')[5].get_text().strip(),\
                              group.find_all('td')[6].get_text().strip()))
            
            return list1
        except:
            raise IOError("Website not accessible") #Exception handling if website is not accessible             

class Database:
    '''Stores data in an SQLite dtabase table'''
    
    def __init__(self):  #constructor
        
        self._sqConnect = sqlite3.connect('SQLite_Data.db')
        self._cursor = self._sqConnect.cursor() 
        self._list1 = Scrapedata().getData()
        
    def  connectTable(self):
        
        '''Connects to an existing database or creates a new database and connects to it '''
                       
        if (self._sqConnect): 
            return True
        
        else:
            return False
        
    def  createTable(self):
        
            '''Creates a table format within the database'''
            
            
            sqlite_create_table_query = ''' DROP TABLE 'MIXING_RATIO';''' 
            sqlite_create_table_query_1 = ''' CREATE TABLE 'MIXING_RATIO'                                       
                                                (  year INTEGER primary key,
                                                   co2 REAL,
                                                   ch4 REAL,
                                                   n2o REAL,
                                                   cfc12 REAL,
                                                   cfc11 REAL,
                                                   minor15 REAL);'''              
                
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
    
        sqlite_insert_query = """ INSERT INTO MIXING_RATIO
                                  (year, co2,ch4,n2o,cfc12,cfc11,minor15) VALUES (?, ?, ?, ?, ?, ?, ?)"""
                                              
        sqliteInsert = self._cursor.executemany(sqlite_insert_query,(self._list1))    
        self._sqConnect.commit()
        
        if sqliteInsert :
            return True
        else:
            return False
        
    def fetchData(self):
        yearList = []
        dataList = []
        self._sqConnect = sqlite3.connect('SQLite_Data.db')
        self._cursor= self._sqConnect.cursor()
        s = 'SELECT YEAR FROM MIXING_RATIO'
        fetchAll = self._cursor.execute(s)
        for row in fetchAll:
            yearList.append(row)
        self._cursor.close()
        return yearList
        
        
class Getdata:
    '''Extracts data from an SQLite database table''' 
    def __init__(self):
        
        self._dataList = []
        self._cO2list = []
        self._setCO2 = set()
        self._cH4list = []
        self._setCH4 = set()
        self._n2Olist = []
        self._setn2O = set()
        self._cFC12list = []
        self._setcFC12 = set()
        self._cFC11list = []
        self._setcFC11 = set()
        self._mINORlist = []
        self._setmINOR = set()
        self._db = Database()
        self._db.connectTable()
        self._db.createTable()
        self._db.insertTable()        
        self._yearList = self._db.fetchData()        
        self._db._cursor.close()

    def _getData(self,col): 
        for year in self._yearList: 
            self._sqConnect = sqlite3.connect('SQLite_Data.db')
            self._cursor= self._sqConnect.cursor()            
            query = self._cursor.execute('SELECT "{}",year FROM MIXING_RATIO'.format(col))
            print("%s fetching %s" % (col,year))            
            self._sqConnect = sqlite3.connect('SQLite_Data.db')
            self._cursor= self._sqConnect.cursor() 
            for value in query:
                value = (col,value)  
                if value[0] == 'CO2':
                    self._cO2list.append(value[1]) 
                elif value[0] == 'CH4':
                    self._cH4list.append(value[1])
                elif value[0] == 'N2O':
                    self._n2Olist.append(value[1])
                elif value[0] == 'CFC12':
                    self._cFC12list.append(value[1])
                elif value[0] == 'CFC11':
                    self._cFC11list.append(value[1])
                elif value[0] == 'MINOR15':
                    self._mINORlist .append(value[1])  
            self._setCO2 = {value for value in self._cO2list}
            self._setCH4 = {value for value in self._cH4list}
            self._setn2O = {value for value in self._n2Olist}
            self._setcFC12 = {value for value in self._cFC12list}
            self._setcFC11 = {value for value in self._cFC11list}
            self._setmINOR = {value for value in self._mINORlist}
        
        time.sleep(2)
        return 
        
    def threadData(self): 
        
        thread_CO2 = ('CO2',)
        thread_CH4 = ('CH4',)
        thread_N2O = ('N2O',)
        thread_CFC12= ('CFC12',)
        thread_CFC11 = ('CFC11',)
        thread_MINOR = ('MINOR15',)
        thd1 = threading.Thread(target=self._getData,args=thread_CO2)
        thd2 = threading.Thread(target=self._getData,args=thread_CH4)
        thd3 = threading.Thread(target=self._getData,args=thread_N2O)
        thd4 = threading.Thread(target=self._getData,args=thread_CFC12)
        thd5 = threading.Thread(target=self._getData,args=thread_CFC11)
        thd6 = threading.Thread(target=self._getData,args=thread_MINOR)
        
        threadlist = [thd1,thd2,thd3,thd4,thd5,thd6]
              
        for i in range(6):
            threadlist[i].start()
            
        for i in range(6):
            threadlist[i].join()
        
        print("Exiting Main Thread")
        tuplist = (self._setCO2,self._setCH4,self._setn2O,self._setcFC12,self._setcFC11,\
                self._setmINOR )
        return tuplist        

      
