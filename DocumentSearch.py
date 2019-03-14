# ******************************************************************************
# * PROGRAM NAME:       DocumentSearch.py                                      *
# * PROGRAM AUTHOR:     Pam Weber                                              *
# * LOCATION:           https://github.com/pamweber/target                     *
# * INSTRUCTIONS:                                                              *
# *     MacOS           1) open terminal                                       *
# *                     2) navigate to folder with program and text files      *
# *                     3) type 'python DocumentSearch.py' to run program      *
# *                     4) respond to prompts                                  *
# *                     5) evaluate results                                    *
# ******************************************************************************

# IMPORT functions
import datetime as dt

# SPECIFY names of the files to be read
fileA = "french_armed_forces.txt"
fileB = "hitchhikers.txt"
fileC = "warp_drive.txt"

# INITIALIZE fields
searchMethod = "" 
searchString = ""
fileCountA = 0
fileCountB = 0
fileCountC = 0
fileContentsA = ""
fileContentsB = ""
fileContentsC = ""

# GET search string
searchStringTries = 1
print ""                                                         # print a blank line for readability
while True :
    if searchStringTries > 3 :                                   # kick the user out of the program after 3 tries
        print "3 STRIKES AND YOU'RE OUT!  Good bye.\n"
        exit()        
    else :
        # print "String Try Number", searchStringTries
        searchString = raw_input("Enter the search term: ")     # ask user for the search string
        if len(searchString) < 1 :                              # if user didn't enter anything, give them another try
            searchStringTries = searchStringTries + 1           # increment the number of tries   
            if searchStringTries < 4 :
                print "Enter at least one character for your search. Please try again."
        else :
            break
# print "    You entered the following term for your search: ", searchString, "\n"

# GET search method
searchMethodTries = 1
while True :
    if searchMethodTries > 3 :                                  # kick the user out of the program after 3 tries                                
        print "3 STRIKES AND YOU'RE OUT!  Good bye.\n"
        exit()
    else :
        # print "Method Try Number", searchMethodTries
        searchMethod = raw_input("Search Method: 1) String Match 2) Regular Expression 3) Indexed: ")  # ask user for the search method
        if len(searchMethod) < 1 :                                 
            searchMethodTries = searchMethodTries + 1           # increment the number of tries
            if searchMethodTries < 4 :
                print "You didn't enter a value.  Please try again."
        elif searchMethod < "1" or searchMethod > "3" :
            searchMethodTries = searchMethodTries + 1           # increment the number of tries
            if searchMethodTries < 4 :
                print "You were supposed to enter 1, 2, or 3 for search method.  Please try again."
        else :
             # print the Search Method description
            if searchMethod == "1" :
                searchType = "StringMatch"
            elif searchMethod == "2" :
                searchType = "RegularExpression"
            else :
                searchType = "Indexed" 
            # print "    Search Method Description = ", searchType
            # print "    You selected the following search method: " + searchMethod + " (" + searchType + ")"
            break  

# START timer now that user has entered their responses - this eliminates user response time variable from the time measurement
timerStart = dt.datetime.now()

# READ the first file
try:
    fhandA = open(fileA,"r")
    fileContentsA = fhandA.read()
    fhandA.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: First file (" + fileA + ") can't be opened.  Stopping program!\n"
    exit()

# READ the second file
try:
    fhandB = open(fileB,"r")
    fileContentsB = fhandB.read()
    fhandA.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: Second file (" + fileB + ") can't be opened.  Stopping program!\n"
    exit()

# READ the third file
try:
    fhandC = open(fileC,"r")
    fileContentsC = fhandC.read()
    fhandC.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: Third file (" + fileC + ") can't be opened.  Stopping program!\n"
    exit()

# COUNT occurrences of search string in each file based on selected search method
if searchMethod == "1" :
    # print "Using Search Method 1"
    fileCountA = fileContentsA.count(searchString)
    fileCountB = fileContentsB.count(searchString)
    fileCountC = fileContentsC.count(searchString)
elif searchMethod == "2" :
    # print "Using Search Method 2"
    import re
    fileCountA = len(re.findall(searchString,fileContentsA))
    fileCountB = len(re.findall(searchString,fileContentsB))
    fileCountC = len(re.findall(searchString,fileContentsC))
else :
    print "Using Search Method 3"

# SORT the search string counts in descending order
def takeSecond(elem):                                                       # little function to use second column
    return elem[1]
counts = [(fileA, fileCountA), (fileB, fileCountB), (fileC, fileCountC)]    # fill the list (a.k.a., array)
counts.sort(key=takeSecond,reverse=True)                                   # sort list by second column in descending order
# print "Sorted list:", counts                                                # print list

# PRINT the results
print "\nSearch Results"
print "  ", counts[0][0], " - ", counts[0][1], "matches"
print "  ", counts[1][0], " - ", counts[1][1], "matches"
print "  ", counts[2][0], " - ", counts[2][1], "matches"

# CALCULATE and print run time in milliseconds
timerStop = dt.datetime.now()
timerTotal = (timerStop-timerStart).microseconds
print "\nElapsed Time: ", timerTotal, "ms\n"

quit()

