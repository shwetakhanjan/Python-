
#    Shweta__Shroff

#FrontEnd or the user interface
'''
This program is an example of OOP where there are two files, FrontEnd(this one) which contains Printdata class from BackEnd import Data class from BackEnd  
This file prints data for yearly values of Co2 emission levels for every month of the years 1951 through 2019 and average temperature data for the same.
 
This file contains methods for printing  the data,for average CO2 emission levels stored in a dictionary,using a named tuple.

'''



import re

from BackEnd import Data


class Printdata :
    '''Class to print data'''
    def __init__(self):  #Constructor
        self._dataObj = Data()
        
              
    def getPrint(self):
        while True:
            
            try:
                q1 = input("Do you want a range of years or a single year?(r/sy) ").lower().strip()
                if q1 == 'r':
                    gen1 = self._dataObj.generateData()
                    y_1 = input("Please enter a 4-digit starting year(1959-2018): ")
                    if not(1959<=int(y_1) <= 2019):
                        print('Error!,value out of range (1959-2018)')
                        continue
                    y_2 = input("Please enter a 4-digit ending year(1959-2018): ") 
                    if not(1959<=int(y_2) <= 2019):
                        print('Error!,value out of range (1959-2018)')
                        continue                    
                    year1 = re.search('\d{4}', y_1).group()
                    year2 = re.search('\d{4}', y_2).group()     #regex           
                    diff1 = int(year1)-1959 
                    diff2 = int(year2)-int(year1)+1
                    for i in range(diff1):
                        next(gen1)                        #iterator
                    for p in range(diff2):                       #iterator
                        a,b = next(gen1)                  
                        print('Year = ',a,", Co2_emmission_level =",b[0],", Temperature= ",b[1])
            
                elif q1 == "sy":    
                    gen1 = self._dataObj.generateData()
                    y_1 = input("Please enter a 4-digit starting year(1959-2018): ")                      
                    year1 = re.search('\d{4}', y_1).group()
                    diff1 = int(year1)-1959 
                    for i in range(diff1):
                        (next(gen1))
                    a,b = next(gen1)                  
                    print('Year = ',a,", Co2_emmission_level =",b[0],", Temperature= ",b[1])                
                else :
                    raise SystemExit("Faulty input, please try again")
                    
            except StopIteration:
                print("No more data")
            q2 = input("Do you want to continue?(y/n) ").lower().strip()
            if q2 == "y":
                continue
            else:
                break
            
    def main(self):
        '''The driver method'''
        self._dataObj.getAvgEmission()
        self._dataObj.getTemp()
        self._dataObj.getYearlyData()         
        self.getPrint()
        
Printdata().main()


#Sample Output:

'''
Do you want a range of years or a single year?(r/sy) sy
Please enter a 4-digit starting year(1959-2018): 1995
Year =  1995 , Co2_emmission_level = 360.82 , Temperature=  0.325
Do you want to continue?(y/n) y
Do you want a range of years or a single year?(r/sy) r
Please enter a 4-digit starting year(1959-2018): 2005
Please enter a 4-digit ending year(1959-2018): 2020
Year =  2005 , Co2_emmission_level = 379.8 , Temperature=  0.545
Year =  2006 , Co2_emmission_level = 381.9 , Temperature=  0.506
Year =  2007 , Co2_emmission_level = 383.79 , Temperature=  0.491
Year =  2008 , Co2_emmission_level = 385.61 , Temperature=  0.395
Year =  2009 , Co2_emmission_level = 387.43 , Temperature=  0.506
Year =  2010 , Co2_emmission_level = 389.9 , Temperature=  0.56
Year =  2011 , Co2_emmission_level = 391.65 , Temperature=  0.425
Year =  2012 , Co2_emmission_level = 393.85 , Temperature=  0.47
Year =  2013 , Co2_emmission_level = 396.52 , Temperature=  0.514
Year =  2014 , Co2_emmission_level = 398.65 , Temperature=  0.579
Year =  2015 , Co2_emmission_level = 400.83 , Temperature=  0.763
Year =  2016 , Co2_emmission_level = 404.24 , Temperature=  0.797
Year =  2017 , Co2_emmission_level = 406.55 , Temperature=  0.677
Year =  2018 , Co2_emmission_level = 408.52 , Temperature=  0.595
Year =  2019 , Co2_emmission_level = 411.35 , Temperature=  No Data
No more data
Do you want to continue?(y/n) n

'''

'''
Do you want a range of years or a single year?(r/sy) r
Please enter a 4-digit starting year(1959-2018): 20
Error!,please enter year between (1959-2018)
Do you want a range of years or a single year?(r/sy) u
Faulty input, please try again
Process terminated with an exit code of 1

'''
'''
Do you want a range of years or a single year?(r/sy) r
Please enter a 4-digit starting year(1959-2018): 2005
Please enter a 4-digit ending year(1959-2018): 2052
Error!,value out of range (1959-2018)
Do you want a range of years or a single year?(r/sy) r
Please enter a 4-digit starting year(1959-2018): 1950
Error!,value out of range (1959-2018)
Do you want a range of years or a single year?(r/sy) sy
Please enter a 4-digit starting year(1959-2018): 1991
Year =  1991 , Co2_emmission_level = 355.61 , Temperature=  0.254
Do you want to continue?(y/n) y
Do you want a range of years or a single year?(r/sy) r
Please enter a 4-digit starting year(1959-2018): 2004
Please enter a 4-digit ending year(1959-2018): 2006
Year =  2004 , Co2_emmission_level = 377.52 , Temperature=  0.447
Year =  2005 , Co2_emmission_level = 379.8 , Temperature=  0.545
Year =  2006 , Co2_emmission_level = 381.9 , Temperature=  0.506
Do you want to continue?(y/n) n
'''
