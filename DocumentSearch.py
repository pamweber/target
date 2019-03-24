# ******************************************************************************
# * PROGRAM NAME:       DocumentSearchClass.py                                 *
# * PROGRAM AUTHOR:     Pam Weber                                              *
# * LOCATION:           https://github.com/pamweber/target                     *
# *                                                                            *
# * INSTRUCTIONS:       Use DocumentSearch_run.py to execute the program       *
# ******************************************************************************

# ****************************************************************************** 
# IMPORT some handy Python functions
# ******************************************************************************

import datetime as dt                               # date time 
import re                                           # regular expressions


# ******************************************************************************
# DEFINE some functions to streamline the code
# ******************************************************************************

# FUNCTION ReadFile - read the contents of a file into a string
def funcReadFile(fileName) :
    try :
        fhandA = open("data/"+fileName,"r")
        funcReadFile = fhandA.read()
        fhandA.close()
        return funcReadFile
    except :  # if the file can't be opened, print an error message and exit the program
        print("ERROR: First file " + fileName + " can't be opened.  Stopping program!\n")
        exit()

# FUNCTION IndexSearch - search for the search string using an index search
def funcIndexSearch(fileContents, searchTerm) :
    fileCount = 0
    sub_len = len(searchTerm)
    for i in range(len(fileContents)) :
        if fileContents[i:i+sub_len] == searchTerm :
            fileCount += 1
    funcIndexSearch = fileCount
    return funcIndexSearch
    
# FUNCTION TakeSecond - retrieve the second column of a 2 dimensional list
def funcTakeSecond(elem) :                                                      
    return elem[1]


# ******************************************************************************
# Now for the program logic set up as Methods within Classes
#   Class:  clSearchString
#       Method: methSearchString - ask user for a search string
#   Class:  clSearchType
#       Method: methSearchType - ask user for the search type
#   Class:  clCountSort
#       Method: methCountSort - use search string and type to count search string
#           by selected type and then sort files into descending order
# ******************************************************************************

# ******************************************************************************
# * Asks the user for the string that they want to count                       *
# ******************************************************************************

class clSearchString(object):
    
    # SEARCH STRING METHOD
    def methSearchString (self) :
        
        # INITIALIZE fields
        self.searchString = ""
        
        # GET search string from user
        searchStringTries = 1
        while True :
            if searchStringTries > 3 :                                  # kick the user out of the program after 3 tries
                print("3 STRIKES AND YOU'RE OUT!  Good bye.\n")
                exit()        
            else :
                # ask user for the search string
                self.searchString = input("Enter the search term: ")
                if len(self.searchString) < 1 :                         # if user didn't enter anything, give them another try
                    searchStringTries = searchStringTries + 1           # increment the number of tries   
                    if searchStringTries < 4 :
                        print("Enter at least one character for your search. Please try again.")
                else :
                     # got the search string so break out of while loop
                     break
        
        # RETURN the result
        return self.searchString

# ******************************************************************************
# * Asks the user for the search type that they want to run                    *
# ******************************************************************************
class clSearchType(object):
    
    # SEARCH TYPE METHOD
    def methSearchType(self) :  

        # INITIALIZE fields
        self.searchType = "" 

        # GET search type from user
        searchTypeTries = 1
        while True :
            if searchTypeTries > 3 :                                    # kick the user out of the program after 3 tries                                
                print("3 STRIKES AND YOU'RE OUT!  Good bye.\n")
                exit()
            else :
                # ask user for the search type
                self.searchType = input("Search Method: 1) String Match 2) Regular Expression 3) Indexed: ")
                if len(self.searchType) < 1 :                                 
                    searchTypeTries = searchTypeTries + 1               # increment the number of tries
                    if searchTypeTries < 4 :
                        print("You didn't enter a value.  Please try again.")
                elif self.searchType not in ("1", "2", "3") :
                    searchTypeTries = searchTypeTries + 1               # increment the number of tries
                    if searchTypeTries < 4 :
                        print("You were supposed to enter 1, 2, or 3 for search type.  Please try again.")
                else :
                     # got the search type so break out of while loop
                    break
        
        # RETURN the result
        return self.searchType					

# ******************************************************************************
# * Count the number of times the search string occurs in each file,           *
# * then sort the files based on the counts in descending order                *
# ******************************************************************************
class clCountSort(object):

    # COUNT AND SORT METHOD
    def methCountSort(self,searchString, searchType) : 

        # INITIALIZE fields
        self.searchString = searchString
        self.searchType = searchType
        fileCountA = 0
        fileCountB = 0
        fileCountC = 0
        fileContentsA = ""
        fileContentsB = ""
        fileContentsC = ""
                
         # READ all three files
        fileA = "french_armed_forces.txt"
        fileB = "hitchhikers.txt"
        fileC = "warp_drive.txt"
        
        fileContentsA = funcReadFile (fileA)
        fileContentsB = funcReadFile (fileB)
        fileContentsC = funcReadFile (fileC)
        
        # START timer here - eliminates variables in user response and file read times
        timerStart = dt.datetime.now()
        
        # COUNT occurrences of search string in each file based on selected search type
        if self.searchType == "1" :
            # do a string match search
            fileCountA = fileContentsA.count(self.searchString)
            fileCountB = fileContentsB.count(self.searchString)
            fileCountC = fileContentsC.count(self.searchString)
        elif self.searchType == "2" :
            # do a regex search
            fileCountA = len(re.findall(self.searchString,fileContentsA))
            fileCountB = len(re.findall(self.searchString,fileContentsB))
            fileCountC = len(re.findall(self.searchString,fileContentsC))
        else :
            # do an index search (using the IndexSearch function)
            fileCountA = funcIndexSearch(fileContentsA, self.searchString)
            fileCountB = funcIndexSearch(fileContentsB, self.searchString)
            fileCountC = funcIndexSearch(fileContentsC, self.searchString)
        
        # FILL a 2 dimensional list (a.k.a., array) with the count results
        counts = [(fileA, fileCountA), (fileB, fileCountB), (fileC, fileCountC)]
        
        # SORT the list by second column in descending order
        counts.sort(key=funcTakeSecond,reverse=True)

        # GATHER the search and sort results to be returned by method
        self.fileName1 = counts[0][0]
        self.fileCount1 = counts[0][1]
        self.fileName2 = counts[1][0]
        self.fileCount2 = counts[1][1]
        self.fileName3 = counts[2][0]
        self.fileCount3 = counts[2][1]
  
        # CALCULATE run time in microseconds then convert to milliseconds
        timerStop = dt.datetime.now()
        self.timerTotal = (timerStop - timerStart).microseconds / float(1000) 
        
        # RETURN the results as a tuple
        return self.fileName1,self.fileCount1,self.fileName2,self.fileCount2,self.fileName3,self.fileCount3,self.timerTotal
