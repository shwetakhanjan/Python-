
#CIS_41A Shweta_Shroff Lab4 Assignment

"""
This is the driver file for the OOP (Object Oriented Programming ),Lab 4 Assignment.This is the driver file to run an application
in conjunction with another file,'language.py' that lets the user read data from an input file and write to output file
1)The languages spoken by people in different countries of the database.

The previous assignment lab3, was an exercise in "Structural Programming" and the functions of Lab3 have been converted to methods of
subclasses in Lab4 here. 

In this file we create an object for each of the subclasses,LanguageFile and LanguageUI of 
class Language. The objects here have been given the user inputs in the form of arguments during
method call.

The final method call for comparison of languages has been put inside a loop, to continue comparison 
until the caller quits.

Exceptions have been handled in the language.py file and we can see the results while calling the methods 
in this file.

"""


from language import  Language,LanguageFile,LanguageUI 

language1 = LanguageFile() #Creates the LanguageFile object

language1.readData()   # With no argument given,the class attribute 'DEFAULTFILE' is the input
                       # argument.If a different file name is given as argument,
                       # system shuts down.
                       
                       # It is necessary to call it before other methods because it will open the fie 
                       # and read data so that other methods can work.

language1.allNames("1.txt","country")   # Calls the public method .allNames() 
                                        #  for LanguageFile object

language1.allNames("2.txt","language")

language1.allNames("3.txt")

language1.topLang("4.txt")


language2 = LanguageUI() # Creates the object of LanguageUI subclass.

language2.readData()

response = "y"

while response == "y" :   #Looping till the user quits
    language2.compareLanguage()
    response = input("Continue to compare? y/n  ").lower()


# SAMPLE OUTPUT #

'''
If an argument for method call .readData is given:
Output :

The input file cannot be opened.Terminating program.
Process terminated with an exit code of 1

'''
'''
Output from above :


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

'''
"""
Other files are submitted separately
"""