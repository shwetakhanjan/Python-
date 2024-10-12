# CIS_41_A Shweta_Shroff lab4 Assignment

"""
This lab serves to demonstrate OOP (Object Oriented Programming).

A Language class is created and two subclasses LanguageFile and LanguageUI are created
to :
1) Read data from an input file and
2) Write to output file the languages spoken by people in different countries of the database.

Objects of the two subclasse are created and the objects show inheritance by inheriting the methods from parent class.

Main aim of the program is to show

1) Object creation, inheritance and
2) Writing to files and program output the names and total number of countries in the database, their common languages
spoken and their names and total number.

Exceptions have been handled in this language.py file and we can see the results while calling the methods 
in lab4.py file.

Finally, a comparison of languages of countries is made based on user input.

"""

import collections



class Language:
    
    """A superclass that contains data that are read in from the input
    lab3.txt file.Contains subclasses LanguageFile and LanguageUI."""
    
    
    
    DEFAULT_FILE = "lab3.txt" # Class attribute, remains constant 
    
    
    # Initialising instance variables using special method of Language class
    
    def __init__(self,countryNames = {},languageNames = collections.defaultdict(int)):
        
        self._countryNames = countryNames
        self._languageNames = languageNames
        
    
    
    
    #Method of the Language superclass available to all instance variables of the class.
    def readData(self,fileName = DEFAULT_FILE) :
        
        
        """A method of Language superclass that reads the data from
        default file and stores it for subclasses."""
        try:
            with open (fileName) as self._infile:  #Opening input file
                
                for self._line in self._infile:
                    self._names = self._line.rstrip().split(',')  
                    self._countryNames[self._names[0]] = tuple(self._names[1:])  # Saving each line of file in a list
                    for self._lang in self._names[1:] :
                        self._languageNames[self._lang]  += 1        
        except FileNotFoundError :
            raise SystemExit       #The system cannot proceed without the data, system must shut down
    
        
        
        

class LanguageFile(Language): #Definig  a subclass of Language superclass
    
    """A subclass of Language superclass that writes data from Language superclass
    onto a file."""
    
    
    
    #@@ required argument fileName1 
    # Public method that prints to a file
    def topLang(self,fileName1):
        
        """A method of subclass LanguageFile that writes to a file the names of most popular
        languages, spoken in countries in the database."""
        
        
        
        #List comprehension
        comLang = [(v,k) for k,v in self._languageNames.items() if v >=10 and k!= "other"]
        outFile = open(fileName1, "w")
        outFile.write("The most common languages\n")
        outFile.write(f'{"Language":13s} {"Num of countries":s}')
        for tup in sorted(comLang,reverse=True):
            outFile.write("\n")
            outFile.write(f'{tup[1]:12s} {tup[0]:10d}')
        
        outFile.close()
        
        
    #@@ Required argument fileName2 and optional argument userChoice               
    def allNames(self,fileName2,userChoice ="") :
        
        """A method of subclass LanguageFile that writes to a file the names of either countries, languages
        or both to a file based on the user input."""
        
        
        
        
        countryList = sorted(list(self._countryNames.keys()))
        
        langList = sorted(list(self._languageNames.keys()))
         
        
        
        # Writes  to a file the required output in the required format based on the user choice.
        # Catches the exception if an incorrect input is given for choice.
        try:
            if userChoice == "country":
                with open(fileName2, "w") as outFile:
                    outFile.write("There are "+ str(len(countryList)) +" countries in the database.\n")
                    
                    for i in range(1,len(countryList)):
                        if countryList[i][0] == countryList[i-1][0] :
                            outFile.write(countryList[i-1]+",")
                        else:
                            outFile.write(countryList[i-1]+"\n")
                            outFile.write("\n")
                    outFile.write(countryList[-1])                  
            elif userChoice == "language" :
                with open(fileName2, "w") as outFile:
                    outFile.write("There are "+ str(len(langList)) +" languages in the database.\n")
                    for i in range(1,len(langList)):
                        if langList[i][0] == langList[i-1][0] :
                            outFile.write(langList[i-1]+",")
                        else:
                            outFile.write(langList[i-1]+"\n")
                            outFile.write("\n")
                    outFile.write(langList[-1])                     
                    
                    
                    
        # This is the default choice.
        
            elif userChoice == "" : 
                with open(fileName2, "w") as outFile:
                    outFile.write("There are "+ str(len(countryList)) +" countries in the database.\n")
                     
                    for i in range(1,len(countryList)):
                        if countryList[i][0] == countryList[i-1][0] :
                            outFile.write(countryList[i-1]+",")
                        else:
                            outFile.write(countryList[i-1]+"\n")
                            outFile.write("\n")
                    outFile.write(countryList[-1])                             
                    
                    outFile.write("\n")
                    outFile.write("\nThere are "+ str(len(langList)) +" languages in the database.\n")
                    for i in range(1,len(langList)):
                        if langList[i][0] == langList[i-1][0] :
                            outFile.write(langList[i-1]+",")
                        else:
                            outFile.write(langList[i-1]+"\n")
                            outFile.write("\n")
                    outFile.write(langList[-1])                     
                    
        
        except ValueError :
            print("Invalid input")         
    
class LanguageUI(Language):   # Defining a subclass of Language superclass
    
    """A subclass of Language class that lets the user enter 2 or more country names and compares the languages
    spoken therein by printing out common languages and all languages spoken. """
    
    def __init__(self,userList=[]):
        
        super().__init__()  #Inheritance from superclass
        self._userList = userList
        
    def __userChoice(self):  #Private method
        
        
        
        newList = []
               
        newUserList = [(0," ")]     #Defining local variables   
        
        count = 0
        print("\nCompare languages"+"\nTo stop press 'Enter'"+"\nNeed at least 2 countries")
        
        Flag = True   #Looping for at least 2 country names
        while Flag:
        
            userInput = input("Enter the first letter of country name: ")
            while userInput !="" :
                if userInput.isalpha() and len(userInput) == 1  :  # looping for user input validation 
                    for country in  self._countryNames :           # of  country letter 
                        if country[0] == userInput.upper() :
                            newList.append(country)        
        
                            
        
        
        
                    for i in range(0,len(newList)):
                        newUserList.append((i+1,newList[i]))
        
                    myDict = {k:v for k,v in newUserList if k!=0}   # Dictionary comprehension
                    print("Country names starting with",userInput.upper())
                    for key in myDict :
                        print(key,myDict[key])
        
                    isNum = False             # Input validation for number
                    while  not isNum :
        
                        try:
                            userNum = input("Enter a number corresponding to a country name: ")
                            if 1 <= int(userNum) <= len(newList):
                                print(myDict[int(userNum)], "chosen")
                                count += 1
                                
                                
                                
                                self._userList.append(myDict[int(userNum)])
                                
                                newList.clear()
                                newUserList.clear()
                                myDict.clear()                                
                                
                                
                                
                                isNum = True
                            else: 
                                print("Number is not within range")  
        
        
                        except :
                            print("Input must be a number")  
        
                else:
                    print("Input must be a letter")                                
                newList.clear()
                newUserList.clear()  
                
                userInput = input("Enter the first letter of country name: ")
            if userInput == "" and count <= 1:  # Ensuring the input of at least 2 country names.
                print("Need at least 2 countries")  
                continue
        
            Flag = False        
        
    #@@ Public method which calls a private method.
    def compareLanguage(self):
        
        '''Prints the languages common among countries chosen by the user and all languages spoken therein.'''
            
        self.__userChoice()  # Private method called by a public method
        setList = [set(self._countryNames[name]) for  name in self._userList] # Set comprehension
        set1 = setList.pop()
        set2 = setList.pop()
        common = set1 & set2  # Intersection of set for common languages
        total = set1 | set2   # Union of set for all languages
        for elements in setList :
            common = common & elements
            total = total | elements
        if len(common) == 0:
            print("No common language")
        else:
            print("Common language(s): ",end ="") #Iteration over a set
            for lang1 in common :
                print (lang1,end =" ")
            print()
        print("All languages: ",end="")
        
        for lang2 in sorted(total):
            print(lang2,end=" ")
        print()
