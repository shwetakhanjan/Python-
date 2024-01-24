#  Shweta__Shroff

# BackEnd  1

'''
This program is the backend part of a GUI application to display graphs of various kinds, viz. XY Plot, Bar Chart and Linear Regression 
displayed with the help of Tkinter.
This file is the BackEnd, which contains all the programs required to run the FrontEnd. 
This file imports fom modules scipy,matplotlib,sqlite3,re and numpy.

This program contains objects from two classes, class Sqlite and class Mplotlib. The object from Sqlite class
is the database that stores data read from an html file 'Temperature.html'. This object is made in the 
constructor method of the next class Mplotlib and different methods of Sqlite class are called on it.
Mplotlib class contains different methods of its own that construct different types of graphs based on the data 
read from the html file.

The graphs are displayed when the methods of the objects of  Mplotlib class are called on its object in the 
FrontEnd file.
'''



from scipy import linspace, polyval, polyfit, sqrt, stats, randn
import sqlite3
import re
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

DEFAULT_FILE = ("Temperature.html")   # Class constant

class Sqlite:
    
    ''' Save data oject by creating a database into memory and provide searches'''

    def __init__(self):
        
        '''Constructor of the class'''

        self._sqConnect = sqlite3.connect('SQLite_Data.db')
        
        self._cursor = self._sqConnect.cursor() 
        self._filename = DEFAULT_FILE
        self._dataList = []
        
    def  connectTable(self):
        
        '''Connects to an existing database or creates a new database and connects to it '''
                       
        if (self._sqConnect): 
            
            return True
        
        else:
            return False
        

    
    def  createTable(self):
        
            '''Creates a table format within the database'''
            
            
            sqlite_create_table_query = ''' DROP TABLE 'Temperature_2';''' 
            sqlite_create_table_query_1 = ''' CREATE TABLE 'Temperature_2' (                                        
                                                year INTEGER primary key,
                                                temp REAL);'''              
                
            try:                       
                sqliteTable = self._cursor.execute(sqlite_create_table_query)  # Exception handling if table already exists 
                sqliteTable_1 = self._cursor.execute(sqlite_create_table_query_1)
                
            except:
                sqliteTable_1 = self._cursor.execute(sqlite_create_table_query_1)
            
            self._sqConnect.commit()
            
            if sqliteTable :
                
                return True
    
        
            else:
                
                return False
        
    def convertToBinaryData(self,filename):  #Makes the SQLite member functions as generic as possible to handle storing any type of data.
        
        '''Convert digital data to binary format'''
        
        with open(self._filename, 'rb') as file: # Used when we insert text data,changed to blob data
            blobData = file.read()
        return blobData             
    
    def insertTable(self):
        
        '''Insert data values into table'''
        
        with open(DEFAULT_FILE) as inFile : 
            for line in inFile :
                line = line.strip().split() # Read text file
                for i in range(len(line)):
                    n = re.search('(\d{4})\<\D+\>(-*0.\d{,4})',line[i])      #regex (Regular Expression)
                if n:
    
                    self._dataList.append((n.group(1),n.group(2)))         
        
        sqlite_insert_query = """ INSERT INTO Temperature_2
                                  (year, temp) VALUES (?, ?)"""
                                         

              
        sqliteInsert = self._cursor.executemany(sqlite_insert_query,(self._dataList))    
        self._sqConnect.commit()
        
        if sqliteInsert :
    
            return True
    
        else:
    
            return False


    def fetch(self):
        
        '''Fetch the data from table'''
        
        con = sqlite3.connect('SQLite_Python.db')
        sel = 'SELECT year, temp  FROM Temperature_2 '
    
        fetchData = self._cursor.execute(sel)
        
        if fetchData :
    
            return fetchData
    
        else:
    
            return False
     
      
    def readTable(self): #Makes the SQLite member functions as generic as possible to perform any type of data manipulation
        
        '''Read a file in read-only mode'''
        
        sqlite_select_query = """SELECT * from Temperature_2"""
        self._cursor.execute(sqlite_select_query)
        records = self._cursor.fetchall() 
    
        if records :
            return True

        else:
            return False

            

                    
    
        
    def deleteTable(self):  #Helps in data manipulation
        
        '''Delete  table along with data values'''
        
        sql_delete_query = """DELETE from Temperature_2 where year = 1950 """
        sqliteDelete = self._cursor.execute(sql_delete_query)
        self._sqConnect.commit() 
        
        if sqliteDelete :
            
            return True
        else:
            return False            
            
        
    def updateTable(self,Id, htext):  #Helps in data manipulation
        
        '''Update data values in the table'''
        
        sql_update_query = """Update Temperature_2 set temp = ? where year = ?"""
        data = (htext, Id)
        sqliteUpdate = self._cursor.execute(sql_update_query, data)
        self._sqConnect.commit()
        
        if sqliteUpdate :
            return True
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
           
        
       

class Mplotlib:
    
    '''Draw the different types of graph'''
    
    def __init__(this):
        
        '''Constructor of the class'''
        
        this._sqlitedbase = Sqlite() #Object of Sqlite class
        Sqlite().connectTable()      #Method call of Sqlite class Object 
        Sqlite().createTable()
        Sqlite().insertTable()
        this.dataList = Sqlite().fetch()
         
        this._fullList = [row for row in this.dataList]   #Obtaining and storing data from Sqlite class Object
        
        this._yearList = [this._fullList[i][0] for i in range(len(this._fullList))] 
          
        this._tempList = [this._fullList[p][1] for p in range(len(this._fullList))]
        
        Sqlite().closeTable()      #Closing the connection to Sqlite table 
    
    
    def xyPlot(this):
        
        '''Draw XY Plot'''
        
        lo = min(this._yearList) #Lower limit of X-axis range
        up = max(this._yearList) #Upper limit of X-axis range
        years = range(lo, up+1)
        data = this._tempList  #Data plotted on Y-axis(Yearly edian Temperature difference)
        
        plt.plot(years, data,color = 'purple',linewidth = 2) # Line plot of the temperature data
        plt.axhline(linewidth=1, color='orange') # Marks the baseline temperature average (1960-1990)
        plt.legend(['Median difference','Baseline Average']) #Show legend
        plt.autoscale(enable=True, axis='both', tight=True) # Show the graph within X-axis and Y-axis range
        plt.title('Yearly median temperature differential from the baseline Celcius average(0 degrees Celsius) from 1960-1990 ')
        plt.xlabel('Years')
        plt.ylabel('Temperature (Celsius)') 
        plt.tick_params(axis ='x', rotation = 45) #Rotate the tick of x-axis
        plt.tick_params(axis ='y', rotation =-45) #Rotate the tick of y-axis
        
        plt.show() #Display XY plot
        
    def barChart(this):

        fig, ax = plt.subplots()

        bar = ax.bar(this._yearList,this._tempList)         # lists chosen for x-axis and y-axis values

        def gradientbars(bars):
            grad = np.atleast_2d(np.linspace(0,1,256)).T
            ax = bars[0].axes
            lim = ax.get_xlim()+ax.get_ylim()
            for bar in bars:
                bar.set_zorder(1)
                bar.set_facecolor("none")
                x,y = bar.get_xy()
                w, h = bar.get_width(), bar.get_height()
                ax.imshow(grad, extent=[x,x+w,y,y+h], aspect="auto", zorder=0)
                ax.legend(['Median difference'])                                  #Show legend
            ax.axis(lim)
        
        gradientbars(bar)                                   #Draws a bar chart with gradient
        
        plt.title('Yearly median temperature differential from the baseline Celcius average(0 degrees Celsius) from 1960-1990')
        plt.autoscale(enable=True, axis='both', tight=True)            # Show the graph within X-axis and Y-axis range
        plt.xlabel('Years')
        plt.ylabel('Temperature(Celsius)')  
        
        plt.show() # display graph

            
    def linReg(this):
        X = np.array(this._yearList).reshape(-1, 1)  #  converts it into a numpy array
        Y = np.array(this._tempList).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
        linear_regressor = LinearRegression()  # create object for the class LinearRegression of sklearn.linear_model
        linear_regressor.fit(X, Y)   # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions
        plt.scatter(X, Y,color='green')     #Display details
        plt.plot(X, Y_pred,color='red',linewidth=4)
        plt.legend(['Regression','Noise'])
        plt.autoscale(enable=True, axis='both', tight=True) # Show the graph within X-axis and Y-axis range
        plt.title('Yearly median temperature differential from the baseline Celcius average(0 degrees Celsius) from 1960-1990')
        #plt.autoscale(enable=True, axis='both', tight=True)            # Show the graph within X-axis and Y-axis range
        plt.xlabel('Years')
        plt.ylabel('Temperature(Celsius)')          
        
        plt.show()   # display graph
    
    
   
#Sqlite().connectTable()

#Sqlite().createTable()
#Sqlite().insertTable()

#Sqlite().fetch()

#XYPlot = Mplotlib().xyPlot()