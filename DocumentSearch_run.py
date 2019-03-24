# ******************************************************************************
# * PROGRAM NAME:       DocumentSearch_run.py                                  *
# * PROGRAM AUTHOR:     Pam Weber                                              *
# * LOCATION:           https://github.com/pamweber/target                     *
# * USAGE:              used to run DocumentSearch.py                          *
# * REQUIREMENTS:       python3                                                *
# *                                                                            *
# * INSTRUCTIONS:                                                              *
# *     MacOS           1) copy program files to local folder                  *
# *                     2) copy input files to /data subfolder                 *
# *                     3) open terminal                                       *
# *                     4) navigate to folder with program file                *
# *                     5) type 'python3 DocumentSearch_run.py'                *
# *                     6) respond to prompts                                  *
# *                     7) evaluate results                                    *
# ******************************************************************************

# This program will run the DocumentSearch.py program by calling the three methods.

import pytest
from DocumentSearch import clSearchString, clSearchType, clCountSort


# RUN the methSearchString and methSearchType methods,
#   then pass the results to the methCountSort method

s=clSearchString()                  #instantiate the Search String class
searchString=s.methSearchString()   #get the search string

t=clSearchType()                    #instantiate the Search Type class
searchType=t.methSearchType()       #get the search type

u=clCountSort()                     #instantiate the Count Sort class
#count occurrences and and sort the results
fileName1, fileCount1, fileName2, fileCount2, fileName3, fileCount3, timerResult = u.methCountSort(searchString,searchType)

# PRINT the results
print("\nSearch Results")
print("  ", fileName1, " - ", fileCount1, "matches")
print("  ", fileName2, " - ", fileCount2, "matches")
print("  ", fileName3, " - ", fileCount3, "matches")

print("\nElapsed Time: ", timerResult, "ms\n")
