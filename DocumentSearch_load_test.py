# ******************************************************************************
# * PROGRAM NAME:       DocumentSearch_load_test.py                            *
# * PROGRAM AUTHOR:     Pam Weber                                              *
# * USAGE:              used to run automated tests against DocumentSearch.py  *
# * LOCATION:           https://github.com/pamweber/target                     *
# *                                                                            *
# * REQUIREMENTS:       python3                                                *
# *                     pytest                                                 *
# *                                                                            *
# * INSTRUCTIONS:       1) clone target project to local git repository        *
# *                     2) open terminal                                       *
# *                     3) navigate to the local git repository                *
# *                     4) type 'pytest -s DocumentSearch_test.py              *
# *                          --term=<term you want to search for>              *
# *                          --method=<search method you want to run>          *
# *                               use one of the following:                    *
# *                               <1> for String Match                         *
# *                               <2> for Regular Expression                   *
# *                               <3> Indexed                                  *
# *                          --times=<number of tests you want to run>         *
# *                        -s = display stdout on console                      *
# *                     7) evaluate results                                    *
# * EX:  pytest -s DocumentSearch_test.py --term=the --method=2 --times=200000 *
# ******************************************************************************

# This program will execute the CountSort method in DocumentSearch.py multiple
# times using the search string and method plus iterations specified at run time 

import pytest
from DocumentSearch import clCountSort


def test_initialize(term,method,times):
   
   # initialize the timer file 
   fi = open('timer.txt', 'w')
   # print("\nTimer file initialized!")
   fi.close()

   # get the runtime parameters
   argSearchString = term
   argSearchType = method
   argTimes = times

   # print('\nSearch Term =', argSearchString, '-- Search Method =', argSearchType, '-- Number of runs =', argTimes)

def test_clCountSort_c(term,method,times):

   # get the runtime parameters
   searchString = term
   searchType = method
   loopCount = times
   
   # run the test as many times as specified in the command line argument
   for i in range(loopCount):
      
      # read the previous timer total from the file
      fr = open('timer.txt', 'r')
      contents = fr.readline()
      if contents == "" :       # if the file is empty, start with zero
          oldTotal = float(0)
      else :
          oldTotal = float(contents)
      fr.close()
   
      # run the count and sort method with search string and search type from run time parameters
      c = clCountSort()
      fileName1, fileCount1, fileName2, fileCount2, fileName3, fileCount3, runTime = c.methCountSort(searchString,searchType)
   
      #write the new timer total back to the file
      fw = open('timer.txt', 'w')
      newTotal = oldTotal + float(runTime)
      fw.write(str(newTotal))
      fw.close()
         
      # print('Time for this execution =', runTime, 'milliseonds and Total Time = ', newTotal, 'milliseconds')

def test_final(term,method,times):

   # read the previous timer total from the file
   fr = open('timer.txt', 'r')

   # get the runtime parameters
   argSearchString = term
   argSearchType = method
   argTimes = times
 
   print('\nSearch Term =', argSearchString, '-- Search Method =', argSearchType,
         '-- Number of runs =', argTimes, '-- Total Time =', fr.readline(), 'milliseconds')
