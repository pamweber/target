# initialize and start timer
import datetime as dt
timerStart = dt.datetime.now()

# specify names of the files to be read
fileA = "french_armed_forces.txt"
fileB = "hitchhikers.txt"
fileC = "warp_drive.txt"

# initialize fields
searchMethod = "" 
searchString = ""
file1Matches = 0
file2Matches = 0
file3Matches = 0
file1 = ""
file2 = ""
file3 = ""

# give the user up to 3 tries to enter a search string of at least one character
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
print "    You entered the following term for your search: ", searchString, "\n"

# give the user 3 tries to select a valid search method
searchMethodTries = 1
while True :
    if searchMethodTries > 3 :                                  # kick the user out of the program after 3 tries                                
        print "3 STRIKES AND YOU'RE OUT!  Good bye.\n"
        exit()
    else :
        # print "Method Try Number", searchMethodTries
        searchMethod = raw_input("Enter the number for the desired search method - 1 (String Match), 2 (Regular Expression), or 3 (Indexed): ")  # ask user for the search method
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
            print "    You selected the following search method: " + searchMethod + " (" + searchType + ")"
            break  

# process the first file
# **** initially, just reading and printing the file ****
print "\n** PROCESSING 1ST FILE **"
try:
    fhandA = open(fileA,"r")
    print fhandA.read()
    fhandA.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: First file (" + fileA + ") can't be opened.  Stopping program!\n"
    exit()

# process the second file
# **** initially, just reading and printing the file ****
print "** PROCESSING 2ND FILE **"
try:
    fhandB = open(fileB)
    print fhandB.read()
    fhandA.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: Second file (" + fileB + ") can't be opened.  Stopping program!\n"
    exit()

# process the third file
# **** initially, just reading and printing the file ****
print "** PROCESSING 3RD FILE**"
try:
    fhandC = open(fileC)
    print fhandC.read()
    fhandC.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: Third file (" + fileC + ") can't be opened.  Stopping program!\n"
    exit()

# order file matches in descending order  
# **** START using dummy assignments until coding is done ****
file1 = fileB
file2 = fileA
file3 = fileC
file1Matches = 10
file2Matches = 7
file3Matches = 2
# **** END using dummy assignments until coding is done ****

# print results
print "** RESULTS LISTED IN DESCENDING ORDER **"
print "  ", file1, " - ", file1Matches, "matches"
print "  ", file2, " - ", file2Matches, "matches"
print "  ", file3, " - ", file3Matches, "matches"

# calculate and print run time in milliseconds
timerStop = dt.datetime.now()
timerTotal = (timerStop-timerStart).microseconds
print "\nElapsed Time: ", timerTotal, "ms\n"

quit()

