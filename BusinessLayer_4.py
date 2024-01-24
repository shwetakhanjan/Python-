
#  Shweta_Shroff 

# BackEnd / Server End / Business Layer 

'''
This program is the server end or the business layer of a GUI application to display xy plot with the help of Tkinter. 
It creates the SQL database from the UNData.xml file, and constructs the query.
A country name is received from the user by this server side and a query is made by this layer regarding 
the data specific to the country chosen by the user. A json string of data is returned to the user layer by this 
server end or the business layer and sent back to the User layer.

Hence, this file serves as the backend which accepts a country name from the user from the user layer and returns data 
from the sqlite table as a json string.
 
'''


import json
import sqlite3
import socket

class Getdata: #Part of data layer
    
    '''Reads data from xml file'''
    
    def __init__(self):  #constructor
        self._xmlString = ''
        
    def readFile(self):    
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        # Python XML Parsing
        import xml.etree.ElementTree as ET
        root = ET.parse("UNData.xml").getroot()
        for country in root.iter('Country'):
            c = country.text
            list1.append(c)
            
        for year in root.iter('Year'):
            y = year.text
            list2.append(y)
            
        for value in root.iter('Value'):
            y = value.text
            list3.append(y)
            
        for i in range(len(list3)):
            list4.append((list1[i],list2[i],list3[i]))
        
        return(list4) #Returns the list of data for countries from the xml file
        

    
    

class Database: #Data Layer
    
    '''Stores data in an SQLite dtabase table'''
    
    def __init__(self):  #constructor
        
        self._sqConnect = sqlite3.connect('SQLite_Data.db')
        self._cursor = self._sqConnect.cursor() 
        self._dataList = Getdata().readFile()
        
    def  connectTable(self):
        
        '''Connects to an existing database or creates a new database and connects to it '''
                       
        if (self._sqConnect): 
            return True
        
        else:
            return False
        
    def  createTable(self):
        
            '''Creates a table format within the database'''
            
            
            sqlite_create_table_query = ''' DROP TABLE 'UN_DATA';''' 
            sqlite_create_table_query_1 = ''' CREATE TABLE 'UN_DATA'                                       
                                                (  country TEXT ,
                                                   year TEXT,
                                                   value TEXT);''' 
                                                                
                
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
    
        sqlite_insert_query = """ INSERT INTO UN_DATA
                                  (country ,year ,value) VALUES (?, ?, ? )"""
                                                                                         
        sqliteInsert = self._cursor.executemany(sqlite_insert_query,(self._dataList))    
        self._sqConnect.commit()
        
        if sqliteInsert :
            return True
        else:
            return False
        
    def fetchData(self,country):
        
        '''Fetches data from the sqlite table'''
        
        dataList = []
        
        s = 'SELECT year,value from UN_DATA where country =="{}" ORDER BY year'.format(country)
    
        fetchAll = self._cursor.execute(s)
        for row in fetchAll:
            dataList.append(row)    
        jsonString = json.dumps(dataList)
        self._cursor.close()
        return jsonString    #Returns the data as a JSON string 
        

class Server: #Server Socket
    
    '''Controls the database access and sends a JSON string in response to client query'''
    
    def __init__(self,port):
        self.host = socket.gethostname()
        self.port = port  # initiate port no above 1024
        self.server_socket = socket.socket()  # get instance
        self.server_socket.bind((self.host, self.port))  # bind host address and port together
    def Connect(self,nports):
        '''Connects to the client port'''
        # configure how many client the server can listen simultaneously
        self.server_socket.listen(nports)
        conn, address = self.server_socket.accept()  # accept new nnection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            Database().connectTable()
            Database().createTable()
            Database().insertTable()            
            d = Database().fetchData(data)
            conn.send(d.encode())  # send data to the client
        conn.close()  # close the connection
        
if __name__ == '__main__':
    server = Server(5000)
    server.Connect(2)