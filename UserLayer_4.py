#  Shweta_Shroff 

# FrontEnd / User Layer  

'''
This program is the client end or the user layer of a GUI application to display xy plot with the help of Tkinter. 
A country name is chosen by the user and is sent across to the server side. A json string of data is returned by the server or the 
business layer. The json string is converted back to python string and processed further to plot an xy graph 
using MatPlotlib.

This file is the frontend, which interacts with the user and asks for a choice of a country name and displays its
data in form of graph(xy plot). 

'''

from tkinter import *
import matplotlib.pyplot as plt
import socket
import json

class Tkinteruse: #GUI Layer
    
    '''Provides a user interface for selection of data '''
    
    def __init__(self):
        
        pass  # Python makes an instance of a class by default, if we do not make one	
            
    def tk(self):
        
        '''Prepares the Tkinter window for the GUI'''
        
        countryList = ['None','Australia', 'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Canada', 'Croatia',
                       'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'European Union', 'Finland', 'France',\
                       'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Japan', 'Latvia', \
                       'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Monaco', 'Netherlands', \
                       'New Zealand', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation',\
                       'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', \
                       'United Kingdom', 'United States of America']
        
        def Country(s):
            return(s)
        
        master = Tk()
        master.title("Please choose a country name or ' None ' to exit")
        master.geometry('500x300')
        variable = StringVar()
        variable.set(countryList[0]) # default value
        w = OptionMenu(master, variable, *countryList, command=Country).pack()
        mainloop()
        if variable.get():
            return str(variable.get()) #Provides the country name as a user choice
        else:
            return False
 
class Client: #Client Socket
    
    '''Sets up the network connection from the user or client end, requests data from the server and  
    after receiving the data from the server, displays the data.'''
    
    def __init__(self,nport): #constructor
        self.host = socket.gethostname()  # as both code is running on same pc
        self.port = nport  # socket server port number
        self.client_socket = socket.socket()  # instantiate
        self.client_socket.connect((self.host, self.port))  # connect to the server
        
    def connect(self):
        
        '''Connects the program file to the server'''
        
        message = str(Tkinteruse().tk())  # take user choice
        print('sending {!r}'.format(message))
        
        while message!= 'None':  #For a continuous stream of user choices till user chooses 'None'
            self.client_socket.send(message.encode())  # send message across to the server side
            data = self.client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
            data = json.loads(data) #Converts the JSON data received from server end to python data
            fullList = [row for row in data]
            yearList = [int(fullList[i][0]) for i in range(len(fullList))] #Prepares list for the x-axis of xy plot
            valueList = [round(float(fullList[i][1]),2) for i in range(len(fullList))] #Prepares list for the y-axis of xy plot
            
            #Code for the xy plot from Matplotlib
                
            lo = min(yearList) #Lower limit of X-axis range
            up = max(yearList) #Upper limit of X-axis range
            years = range(lo, up+1) # Data plotted on X-axis(years)
            data1 = valueList  # Data plotted on Y-axis - (Value for the year)
            
            plt.plot(years, data1,color = 'purple',linewidth = 2) # Line plot of the value data
            
            plt.legend(['Value']) #Show legend
            plt.autoscale(enable=True, axis='both', tight=True) # Show the graph within X-axis and Y-axis range
            plt.title('Values for years 1990-2017 : '+str(message))
            plt.xlabel('Years')
            plt.ylabel('Value') 
            plt.tick_params(axis ='x', rotation = 45) #Rotate the tick of x-axis
            plt.tick_params(axis ='y', rotation =-45) #Rotate the tick of y-axis
            
            plt.show() #Display XY plot
        
            message = str(Tkinteruse().tk()) 
            print('sending {!r}'.format(message))
        self.client_socket.close()  # close the connection
        return
        

if __name__ == '__main__': #Runs the program
    client = Client(5000)
    client.connect()
    



