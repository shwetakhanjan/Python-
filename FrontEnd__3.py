

'''
This program plots 6 linear regression graphs for 6 sub agents used to fetch data from an sqlite table
using multithreading.
Each graph spawns after the other in succession, as we close the previous graph.
This is the user interface and interacts with the user.
'''
    
    
    
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression    
from BackEnd_3 import  Getdata
    
    
class Plotdata:
    '''Plots linear regression graphs using data from sqlite table'''
    def __init__(self):
        
        self._data = Getdata()
        self._tuplist = self._data.threadData()  #obtaining relevant data for arguments
        self._data._listCO2 = list(self._data._setCO2)#of function to plot linear regression
        self._yearListCO2 = []
        self._dataListCO2 = []        
        self._data._listCO2.sort(key=lambda x: x[1])
        for tup in self._data._listCO2 :
            self._yearListCO2.append(tup[1])
            self._dataListCO2.append(tup[0])
            
        self._data._listCH4 = list(self._data._setCH4)
        self._yearListCH4 = []
        self._dataListCH4 = []        
        self._data._listCH4.sort(key=lambda x: x[1])
        for tup in self._data._listCH4 :
            self._yearListCH4.append(tup[1])
            self._dataListCH4.append(tup[0])
            
        self._data._listn2O = list(self._data._setn2O)
        self._yearListn2O = []
        self._dataListn2O = []        
        self._data._listn2O.sort(key=lambda x: x[1])
        for tup in self._data._listn2O :
            self._yearListn2O.append(tup[1])
            self._dataListn2O.append(tup[0])
            
        self._data._listcFC12 = list(self._data._setcFC12)
        self._yearListcFC12 = []
        self._dataListcFC12 = []        
        self._data._listcFC12.sort(key=lambda x: x[1])
        for tup in self._data._listcFC12 :
            self._yearListcFC12.append(tup[1])
            self._dataListcFC12.append(tup[0])
            
        self._data._listcFC11 = list(self._data._setcFC11)
        self._yearListcFC11 = []
        self._dataListcFC11 = []        
        self._data._listcFC11.sort(key=lambda x: x[1])
        for tup in self._data._listcFC11 :
            self._yearListcFC11.append(tup[1])
            self._dataListcFC11.append(tup[0])
        
        self._data._listmINOR = list(self._data._setmINOR)
        self._yearListmINOR = []
        self._dataListmINOR = []        
        self._data._listmINOR.sort(key=lambda x: x[1])
        for tup in self._data._listmINOR :
            self._yearListmINOR.append(tup[1])
            self._dataListmINOR.append(tup[0])    
        
        
        
        
                
        
    def linReg(self,year,data,name):
        '''Plots a linear regression graph'''
        
        
        X = np.array(year).reshape(-1, 1)  #  converts it into a numpy array
        Y = np.array(data).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
        linear_regressor = LinearRegression()  # create object for the class LinearRegression of sklearn.linear_model
        linear_regressor.fit(X, Y)   # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions
        plt.scatter(X, Y,color='green')     #Display details
        plt.plot(X, Y_pred,color='red',linewidth=4)
        plt.legend(['Regression','Noise'])
        plt.autoscale(enable=True, axis='both', tight=True) # Show the graph within X-axis and Y-axis range
        plt.title('Global Radiative Forcing, from 1979-2019,Agent:'+ str(name))
        plt.xlabel('Years')
        plt.ylabel('Global Radiative Forcing(W m-2)')          
    
        plt.show()   # display graph
        
        
        
        
    def run(self):    
        '''Runs the program'''
        #method call for each of the agents
        functCO2 = self.linReg(self._yearListCO2,self._dataListCO2,'CO2')
        functCH4 = self.linReg(self._yearListCH4,self._dataListCH4,'CH4')
        functN2O = self.linReg(self._yearListn2O,self._dataListn2O,'N2O')
        functCFC12 = self.linReg(self._yearListcFC12,self._dataListcFC12,'CFC12')
        functCFC11 = self.linReg(self._yearListcFC11,self._dataListcFC11,'CFC11')
        functMINOR = self.linReg(self._yearListmINOR,self._dataListmINOR,'MINOR15')
        
        #functlist = [functCO2,functCH4,functN2O,functCFC12,functCFC11,functMINOR]
           
            
        
        return    
        
        
                    
    
    
    
            
Plotdata().run()

