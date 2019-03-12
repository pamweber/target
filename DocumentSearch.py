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

# give the user 3 tries to enter a search string of at least one character
searchStringTries = 0
while True:
    searchString = raw_input("Enter the search term: ")       # ask user for the search string
    if len(searchString) < 1 :                                # if user didn't enter anything, give them another try
        print "Enter at least one character for your search. Please try again."
        searchStringTries = searchStringTries + 1             # increment the number of tries
        if searchStringTries > 2 :                            # if the user misses 3 times, exit the program
            print "3 STRIKES AND YOU'RE OUT!  Good bye."
            exit()
        continue
    else:
        print "SearchString =", searchString
        break

# ask user for the search method
searchMethod = raw_input("Enter the number for the desired search method - 1 (String Match), 2 (Regular Expression), or 3 (Indexed): ")

# verify that user entered a valid search method value
if searchMethod == "1" :
    searchType = "StringMatch"
elif searchMethod == "2" :
    searchType = "RegularExpression"
elif searchMethod == "3" :
    searchType = "Indexed"
else:
    print "You were supposed to enter 1, 2, or 3 for search method.  Bye!"
    exit()

print "Search Method = ", searchMethod
print "Search Type = ", searchType

# process the first file
# **** initially, just reading and printing the file ****
print "\n** PROCESSING 1ST FILE **\n"
try:
    fhandA = open(fileA,"r")
    print fhandA.read(), "\n"
    fhandA.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: First file (" + fileA + ") can't be opened.  Stopping program!\n"
    exit()

# process the second file
# **** initially, just reading and printing the file ****
print "\n** PROCESSING 2ND FILE **\n"
try:
    fhandB = open(fileB)
    print fhandB.read(), "\n"
    fhandA.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: Second file (" + fileB + ") can't be opened.  Stopping program!\n"
    exit()

# process the third file
# **** initially, just reading and printing the file ****
print "\n** PROCESSING 3RD FILE**\n"
try:
    fhandC = open(fileC)
    print fhandC.read(), "\n"
    fhandC.close()
except:  # print an error message and exit the program if the file can't be opened
    print "ERROR: Third file (" + fileC + ") can't be opened.  Stopping program!\n"
    exit()

# order file matches in descending order  
# **** using dummy assignments until coding is done ****
file1 = fileB
file2 = fileA
file3 = fileC

# print results
print file1, " - ", file1Matches, "matches"
print file2, " - ", file2Matches, "matches"
print file3, " - ", file3Matches, "matches"

# calculate and print run time in milliseconds
timerStop = dt.datetime.now()
timerTotal = (timerStop-timerStart).microseconds
print "Elapshed Time: ", timerTotal, "ms"

quit()