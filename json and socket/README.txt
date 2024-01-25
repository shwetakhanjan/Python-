This program has a user layer of a GUI application to display xy plot with the help of Tkinter. 
A country name is chosen by the user and is sent across to the server side. A json string of data is returned by the server or the 
business layer. The json string is converted back to python string and processed further to plot an xy graph 
using MatPlotlib.

The file UserLayer_4.py is the frontend, which interacts with the user and asks for a choice of a country name and displays its
data in form of graph(xy plot). 



This program also has a server end or the business layer of a GUI application to display xy plot with the help of Tkinter. 
It creates the SQL database from the UNData.xml file, and constructs the query.
A country name is received from the user by this server side and a query is made by this layer regarding 
the data specific to the country chosen by the user. A json string of data is returned to the user layer by this 
server end or the business layer and sent back to the User layer.

Hence, the file BusinessLayer_4.py serves as the backend which accepts a country name from the user from the user layer and returns data 
from the sqlite table as a json string.


Server Socket:

The database access is controlled by the Server Socket.  The client sends a query, and the server sends a JSON string.

Client Socket:

Requests data from the server.  After receiving the data from the server, the client displays the data.

 
 



 

 

 

 

 


