This program plots 6 linear regression graphs for 6 sub agents used to fetch data from an sqlite table
using multithreading.
Each graph spawns after the other in succession, as we close the previous graph.
FrontEnd__3.py is the user interface and interacts with the user.

BackEnd_3.py contains code that fetches data from a website using Webscraping and insrets it into an sqlite database.
It uses multithreading  for 6 sub agents used to fetch data from the sqlite table.
This file is the the backend and does not interact with the user.

Thus the concepts of Webscraping and multithreading are reinforced in this program .
