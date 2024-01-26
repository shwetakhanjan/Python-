This program is a GUI application to display graphs of various kinds, viz. XY Plot, Bar Chart and Linear Regression 
displayed with the help of Tkinter.
The file FrontEnd_1.py is the frontend, which interacts with the user and asks for a choice and displays the chosen graph.

The file BackEnd_1.py is the backend part of the GUI application to display graphs of various kinds, viz. XY Plot, Bar Chart and Linear Regression 
displayed with the help of Tkinter, which contains all the programs required to run the FrontEnd. 
This file imports fom modules scipy,matplotlib,sqlite3,re and numpy.

This program contains objects from two classes, class Sqlite and class Mplotlib. The object from Sqlite class
is the database that stores data read from an html file 'Temperature.html'. This object is made in the 
constructor method of the next class Mplotlib and different methods of Sqlite class are called on it.
Mplotlib class contains different methods of its own that construct different types of graphs based on the data 
read from the html file.

The graphs are displayed when the methods of the objects of  Mplotlib class are called on its object in the 
FrontEnd file.
