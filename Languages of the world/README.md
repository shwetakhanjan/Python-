
# Project Title

Languages of the world. 

# Description 
The application is in 2 files: language.py and lab4.py. 
Data for the project is contained in lab3.txt file.

This is a study in Object Oriented Programming(OOP) to print to files the names and total number of countries in the database, names and total number of languages.It prints to program the list of the most common languages, all languages from the chosen countries and the common language among the chosen countries.
  

It uses the concepts of Classes(Superclass and subclass), methods, inheritance, and review of iterables and exception handling.
# Documentation

The application will be in 2 files: language.py and lab4.py. 
Data for the project is contained in lab3.txt file.

Lab4.py:

This is the driver file for the OOP (Object Oriented Programming ) application that runs in conjunction with another file,'language.py' It  lets the user read data from an input file and write to output file
the languages spoken by people in different countries of the database, has a method to print to file all the countries, or all the languages, or both.

The file lab4.py works with the LanguageFile and LanguageUI classes that contain code to:

 Create a LanguageFile object

 Call the method to print all countries to a file, 

 Call the same method to print all languages to a file

 Call the same method to print both countries and languages to a file
 Call the method to print most popular languages to a file
 Create the LanguageUI object
 Loop to keep calling the method to let the user compare languages between 2 countries. 

In this file we create an object for each of the subclasses,LanguageFile and LanguageUI of class Language. The objects here have been
given the user inputs in the form of arguments during method call.  

Language class does not send anything to screen or read anything from the keyboard (no user interaction).
The final method call for comparison of languages has been put inside a loop, to continue comparison 
until the caller quits.

Exceptions have been handled in the language.py file and we can see the results while calling the methods 
in this file.


language.py:

This lab serves to demonstrate OOP (Object Oriented Programming).

Description of classes

There are 3 classes in language.py: a Language superclass and 2 subclasses: LanguageFile and LanguageUI
The Language superclass contains data that are read in from the input lab3.txt file
The LanguageFile subclass writes data to a file.
The LanguageUI subclass interacts with the user and prints data to screen.

Objects of the two subclasse are created and the objects show inheritance by inheriting the methods from parent class.

Language superclass:

Creates a class attribute called DEFAULT_FILE that stores the lab3.txt filename.

Reads data from the DEFAULT_FILE and stores data. 

The Language class does not interact with the user, which means there is no user input or printing to screen.

Main aim of the program is to show

1) Object creation, inheritance and

2) Writing to files and program output the names and total number of countries in the database, their common languages spoken and their names and total number.

3) Instance variables and local variables have been chosen appropriately.

4) All static data structures have been created one time only.

Exceptions have been handled in this language.py file and we can see the results while calling the methods in lab4.py file.

Finally, a comparison of languages of countries is made based on user input.
# Acknowledgements

I must acknowledge my professor from community college, where I obtained a 3-quarter long certification in Python, for providing me the opportunity to do this lab, as a part of my coursework. 
The data source is the file "lab3.txt", provided by my professor. For the sake of anonymity and to prevent instances of plagiarism, I am keeping names confidential.
# Running Tests

To run tests, we need to run the file lab4.py. This file works in conjunction with file language.py that contains superclasses and subclasses as mentioned above. Invoking the classes to produce their instances, using inheritance and methods from these super and subclasses, along with exception handling, proper choice of instance variables and local variables are key to proper functioning of this program.

For the output, we expect 4 text files, with data from lab3.txt used to produce output  like
1) Total number and list of countries in the database.
2) Total number and list of languages in the database
3) Total number and list of countries and languages in the database
4) List of top 5 most common languages spoken, with   number of countries, in a tabular format.

The program has a private method that lets the user 

1) Enter 2 or more country languages, asking the user for a letter, then prints the list of country names starting with that letter and prints a corresponding counting number, one for each country name.
(See sample output.)
2) Asks the user to choose a number (which means the user indirectly chooses a corresponding name).
If the user doesn't enters a number within range, it keeps prompting until it gets a valid number from the user.
Hint: It&#39;s simpler to put the code of this step in a separate private method.
3) It Keeps running the previous 2 steps until it gets at least 2 valid countries and the user has pressed the Enter key to stop. 
4) Has a method that prints the common language among the chosen countries, and print all languages from the
chosen countries.

#Sample Output:

#1. If an argument for method call .readData is given:


Output :

The input file cannot be opened.Terminating program.
Process terminated with an exit code of 1

#2.

Compare languages

To stop press 'Enter'

Need at least 2 countries

Enter the first letter of country name: i

Country names starting with I
1 Iceland
2 India
3 Indonesia
4 Iran
5 Iraq
6 Ireland
7 Israel
8 Italy

Enter a number corresponding to a country name: 1

Iceland chosen

Enter the first letter of country name: w

Country names starting with W

1 Western Sahara (Proposed State)

Enter a number corresponding to a country name: 1

Western Sahara (Proposed State) chosen

Enter the first letter of country name: 

No common language

All languages: English German Hassaniya Arabic 
Icelandic Moroccan Arabic Nordic languages 

Continue to compare? y/n  n

Thank you!



#3.

Compare languages

Need at least 2 countries

Enter the first letter of country name: 3

Input must be a letter

Enter the first letter of country name: e

Country names starting with E
1 East Timor
2 Ecuador
3 Egypt
4 El Salvador
5 Equatorial Guinea
6 Eritrea
7 Estonia
8 Ethiopia

Enter a number corresponding to a country name: 8

Ethiopia chosen

Enter the first letter of country name: 5

Input must be a letter

Enter the first letter of country name: e

Country names starting with E
1 East Timor
2 Ecuador
3 Egypt
4 El Salvador
5 Equatorial Guinea
6 Eritrea
7 Estonia
8 Ethiopia

Enter a number corresponding to a country name: 1

East Timor chosen

Enter the first letter of country name: e

Country names starting with E
1 East Timor
2 Ecuador
3 Egypt
4 El Salvador
5 Equatorial Guinea
6 Eritrea
7 Estonia
8 Ethiopia

Enter a number corresponding to a country name: t

Input must be a number

Enter a number corresponding to a country name: 90

Number is not within range

Enter a number corresponding to a country name: e


Input must be a number

Enter a number corresponding to a country name: 3

Egypt chosen

Enter the first letter of country name: 

Common language(s): English 

All languages: Amharic Arabic Bahasa Indonesia English French Guaragigna Orominga Portuguese Somali Tetum Tigrigna other indigenous languages 

Continue to compare? y/n  Y


Compare languages

Need at least 2 countries

Enter the first letter of country name: r

Country names starting with R
1 Romania
2 Russia
3 Rwanda

Enter a number corresponding to a country name: 3

Rwanda chosen

Enter the first letter of country name: 
Need at least 2 countries

Enter the first letter of country name: 
Need at least 2 countries

Enter the first letter of country name: t

Country names starting with T
1 Taiwan
2 Tajikistan
3 Tanzania
4 Thailand
5 Togo
6 Tonga
7 Trinidad And Tobago
8 Tunisia
9 Turkey
10 Turkmenistan
11 Tuvalu

Enter a number corresponding to a country name: 5
Togo chosen

Enter the first letter of country name: 

No common language

All languages: Amharic Arabic Bahasa Indonesia Dagomba English Ewe French Guaragigna Kabye Kinyarwanda Mina Orominga Portuguese Somali Tetum Tigrigna many dialects other indigenous languages 

Continue to compare? y/n  n

Thank you!
