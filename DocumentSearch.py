# ******************************************************************************
# * PROGRAM NAME:       DocumentSearch.py                                      *
# * PROGRAM AUTHOR:     Pam Weber                                              *
# * LOCATION:           https://github.com/pamweber/target                     *
# * INSTRUCTIONS:                                                              *
# *     MacOS           1) copy program and text files to local drive          *
# *                     2) open terminal                                       *
# *                     3) navigate to folder with program and text files      *
# *                     4) type 'python DocumentSearch.py' to run program      *
# *                     5) respond to prompts                                  *
# *                     6) evaluate results                                    *
# ******************************************************************************

# ******************************************************************************
# IMPORT some handy Python functions
# ******************************************************************************

import datetime as dt                               # date time 
import re                                           # regular expressions


# ******************************************************************************
# DEFINE some functions to streamline the code
# ******************************************************************************

# FUNCTION fileContents - read the contents of a file into a string
def fileContents(fileName) :
    try :
        fhandA = open(fileName,"r")
        fileContents = fhandA.read()
        fhandA.close()
        return fileContents
    except :  # if the file can't be opened, print an error message and exit the program
        print "ERROR: First file (" + fileName + ") can't be opened.  Stopping program!\n"
        exit()

# FUNCTION indexSearch - search for the search string using an index search
def indexSearch(fileContents, searchString) :
    fileCount = 0
    sub_len = len(searchString)
    for i in range(len(fileContents)) :
        if fileContents[i:i+sub_len] == searchString :
            fileCount += 1
    indexSearch = fileCount
    return indexSearch
    
# FUNCTION takeSecond - retrieve the second column of a 2 dimensional list
def takeSecond(elem) :                                                      
    return elem[1]


# ******************************************************************************
# SPECIFY names of the files to be read                                        *
# ******************************************************************************

fileA = "french_armed_forces.txt"
fileB = "hitchhikers.txt"
fileC = "warp_drive.txt"


# ******************************************************************************
# INITIALIZE fields                                                            *
# ******************************************************************************

searchMethod = "" 
searchString = ""
fileCountA = 0
fileCountB = 0
fileCountC = 0
fileContentsA = ""
fileContentsB = ""
fileContentsC = ""


# ******************************************************************************
# Now for the program logic                                                    *
# ******************************************************************************

# ASK user for search string
searchStringTries = 1
print ""                                                         # print a blank line for readability
while True :
    if searchStringTries > 3 :                                   # kick the user out of the program after 3 tries
        print "3 STRIKES AND YOU'RE OUT!  Good bye.\n"
        exit()        
    else :
        # ask user for the search string
        searchString = raw_input("Enter the search term: ")
        if len(searchString) < 1 :                              # if user didn't enter anything, give them another try
            searchStringTries = searchStringTries + 1           # increment the number of tries   
            if searchStringTries < 4 :
                print "Enter at least one character for your search. Please try again."
        else :
             # got the search string so break out of while loop
             break

# ASK user for search method
searchMethodTries = 1
while True :
    if searchMethodTries > 3 :                                  # kick the user out of the program after 3 tries                                
        print "3 STRIKES AND YOU'RE OUT!  Good bye.\n"
        exit()
    else :
        # ask user for the search method
        searchMethod = raw_input("Search Method: 1) String Match 2) Regular Expression 3) Indexed: ")
        if len(searchMethod) < 1 :                                 
            searchMethodTries = searchMethodTries + 1           # increment the number of tries
            if searchMethodTries < 4 :
                print "You didn't enter a value.  Please try again."
        elif searchMethod < "1" or searchMethod > "3" :
            searchMethodTries = searchMethodTries + 1           # increment the number of tries
            if searchMethodTries < 4 :
                print "You were supposed to enter 1, 2, or 3 for search method.  Please try again."
        else :
             # got the search method so break out of while loop
            break  

# Read all three files (using my fileContents function)
fileContentsA = fileContents (fileA)
fileContentsB = fileContents (fileB)
fileContentsC = fileContents (fileC)

# START timer here - eliminates variables in user response and file read times
timerStart = dt.datetime.now()

# COUNT occurrences of search string in each file based on selected search method
if searchMethod == "1" :
    # do a string match search
    fileCountA = fileContentsA.count(searchString)
    fileCountB = fileContentsB.count(searchString)
    fileCountC = fileContentsC.count(searchString)
elif searchMethod == "2" :
    # do a regex search
    fileCountA = len(re.findall(searchString,fileContentsA))
    fileCountB = len(re.findall(searchString,fileContentsB))
    fileCountC = len(re.findall(searchString,fileContentsC))
else :
    # do an index search (using my indexSearch function)
    fileCountA = indexSearch(fileContentsA, searchString)
    fileCountB = indexSearch(fileContentsB, searchString)
    fileCountC = indexSearch(fileContentsC, searchString)

# SORT the search string counts in descending order
counts = [(fileA, fileCountA), (fileB, fileCountB), (fileC, fileCountC)]    # fill the 2 dimensional list (a.k.a., array)
counts.sort(key=takeSecond,reverse=True)                                    # sort list by second column in descending order

# PRINT the results
print "\nSearch Results"
print "  ", counts[0][0], " - ", counts[0][1], "matches"
print "  ", counts[1][0], " - ", counts[1][1], "matches"
print "  ", counts[2][0], " - ", counts[2][1], "matches"

# CALCULATE and print runtime in milliseconds
timerStop = dt.datetime.now()
timerTotal = (timerStop-timerStart).microseconds
print "\nElapsed Time: ", timerTotal, "ms\n"

quit()
