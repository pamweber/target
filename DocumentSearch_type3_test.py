# ******************************************************************************
# * PROGRAM NAME:       DocumentSearch_type3_test.py                           *
# * PROGRAM AUTHOR:     Pam Weber                                              *
# * USAGE:              used to run automated tests against DocumentSearch.py  *
# * LOCATION:           https://github.com/pamweber/target                     *
# * REQUIREMENTS:       python3                                                *
# *                     pytest                                                 *
# *                     pytest-repeat                                          *
# *                                                                            *
# * INSTRUCTIONS:                                                              *
# *     MacOS           1) copy program file to location of AUT                *
# *                     2) open terminal                                       *
# *                     3) navigate to folder with program files               *
# *                     4) type 'pytest -v DocumentSearch_test.py'             *
# *                        -v = verbose                                        *
# *                          add '--count=x' to run x times                    *
# *                     5) evaluate results                                    *
# ******************************************************************************

# This program will test search type 3 of DocumentSearch.py

import pytest
from DocumentSearch import clCountSort


# test with search string = "the" and search type 3
def test_clCountSort_c():
    searchString = "the"
    searchType = "3"
    c = clCountSort()
    fileName1, fileCount1, fileName2, fileCount2, fileName3, fileCount3, totalTime = c.methCountSort(searchString,searchType)

    assert fileName1 == "french_armed_forces.txt"
    assert fileCount1 == 59
    assert fileName2 == "hitchhikers.txt"
    assert fileCount2 == 24
    assert fileName3 == "warp_drive.txt"
    assert fileCount3 == 9 
