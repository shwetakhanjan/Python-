#  Shweta__Shroff 

# FrontEnd  1

'''
This program is a GUI application to display graphs of various kinds, viz. XY Plot, Bar Chart and Linear Regression 
displayed with the help of Tkinter.
This file is the frontend, which interacts with the user and asks for a choice and displays the chosen graph. 

'''






from tkinter import *
from BackEnd_1 import Mplotlib


class Tkinteruse:
    
    '''Provides a user interface for selection of type of data display'''
    
    def __init__(self): #Constructor class
        
        self._obj = Mplotlib()
                   
    def display_1(self):
        '''Display the XY Plot'''
        return self._obj.xyPlot()
    def display_2(self):
        '''Display the Bar Chart'''
        return self._obj.barChart()
    def display_3(self):
        '''Display the Linear Regression'''
        return self._obj.linReg()  
    
    
    def main(self):
        
        '''Driver function of the class'''
        
        root = Tk()
        root.title("Please choose the graph for display")
        root.geometry("500x300")
        var = IntVar()
        
        R1 = Radiobutton(root, text = " XYPlot", variable = var, value = 1,command = tki.display_1)
        R1.pack( anchor = W )
        
        R2 = Radiobutton(root, text = " BarChart", variable = var, value = 2,command = tki.display_2)
        R2.pack( anchor = W )
        
        R3 = Radiobutton(root, text = " Linear Regresssion", variable = var, value = 3,command = tki.display_3)
        R3.pack( anchor = W)
                      
        label = Label(root)
        label.pack()
        root.mainloop()
        
            
        
       
        
    
tki = Tkinteruse()    
tki.main()
        
            
