

#    Shweta__Shroff

#FrontEnd
'''
This program is an example of OOP where there are two files, BackEnd(this one) which contains Data class which reads in different files, 'Co2.html' containing 
yearly values of Co2 emossion levels for every month of the years 1951 through 2019, and another file 'Temperature.html' that contains average temperature data for the years 1850 
through 2018.
This file contains methods for reading the data,storing the temperature values in a default dictionary, average CO2 emission levels in a named tuple and yearly data in 
a default dictionary with year,temp and CO2 values. It also contains a method for a generator to yield the yearly values.

'''

import re
import collections

DEFAULT_FILE_1 = ("Co2.html")
DEFAULT_FILE_2 = ("Temperature.html")   # Class constants

class Data :
        ''' read data from file into memory and provide searches'''
        
        def __init__(self):
                
                self._dataList = []
                self._tempList =  []
                self._readFile()
                emTuple = collections.namedtuple('emTuple',['Year','Co2_level'])   #named tuple
                self._emList = []
                self._diTemp = collections.defaultdict(lambda:"No Data")            #lambda expression,default dictionary
                self._emTuple = emTuple  
                self._dataDict = {} 
                
        def _readFile(self) :    # private method
                                      
                '''Reads the data from html files and temporarily stores the data for further processing'''
                
                with open(DEFAULT_FILE_1) as inFile : 
                        
                
                        for line in inFile :
                                line = line.strip().split()
                                for i in range(len(line)):
                                        m = re.search('(\d{4})(.)*(\\b\d{3}.\d{2}\\b)',line[i])      #regex (Regular Expression)
                                
                                if m:
                                        self._dataList.append((m.group(1),float(m.group(3))))    
                                        
                       

                with open(DEFAULT_FILE_2) as inFile : 
                        for line in inFile :
                                line = line.strip().split()
                                for i in range(len(line)):
                                        n = re.search('(\d{4})\<\D+\>(-*0.\d{,4})',line[i])      #regex (Regular Expression)
                                if n:
                                        self._tempList.append((n.group(1),n.group(2)))               
              
                     
                return (self._dataList,self._tempList)
        
        
        
        def  getAvgEmission(self):  
                
                '''Computes the yearly average CO2 emission levels and stores the data in appropriate data structures'''
                
                deDi1 = collections.defaultdict(int)
                for i in range(len(self._dataList)):                   #default dictionary
                        deDi1[self._dataList[i][0]] += 1        
                      
        
             
                
                deDi2 = collections.defaultdict(float)               
                
                for i in range(len(self._dataList)):
                        deDi2[self._dataList[i][0]] += self._dataList[i][1]     #default dictionary
                        
         
                
                list1 = list(deDi1.values())   
                list2 = list(deDi2.values())  
                list3 = list(deDi1.keys())
                list4 = []
                for i in range(len(deDi1)):
                        list4.append(list2[i]/list1[i])
                list5 = []
                for p in range(len(deDi1)):
                        list5.append([list3[p],list4[p]])
                
                #for u in range(len(deDi1)) :
                        #self._emList.append(self._emTuple._make(list5[u]))
                self._emList = [self._emTuple._make(list5[u]) for u in range(len(deDi1))]  #List comprehension
               
                return (self._emList)        
            
        def getTemp(self):
        
                '''Stores the temperature data in appropriate data structure'''
        
                
                
                for i in range(len(self._tempList)) :
                        self._diTemp[self._tempList[i][0]] = self._tempList[i][1]                     

                return (self._diTemp)
        
        
        def getYearlyData(self):
                
                '''Gets the data for both yearly temperature and average yearly CO2 emission levels and stores it in required data structures'''
                
                #Dictionary comprehension
                self._dataDict = {self._emTuple.Year : (round(self._emTuple.Co2_level,2), self._diTemp[self._emTuple.Year]) for self._emTuple in self._emList} 
                return (self._dataDict)

        def generateData(self): 
        
                '''generates data ready to be printed'''
        
                return ((k,v) for k,v in self._dataDict.items())   #generator
                
                
                
                

        
        
        
        
        
        
        

                











