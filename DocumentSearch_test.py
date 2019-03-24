# ******************************************************************************
# * PROGRAM NAME:       DocumentSearch_test.py                                 *
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
# *                     4) type 'pytest -v -s DocumentSearch_test.py'          *
# *                        -v = verbose                                        *
# *                        -s = print stndout to console                       *
# *                     5) evaluate results                                    *
# ******************************************************************************

# This program will test DocumentSearch.py by providing three sets of inputs

import pytest
from DocumentSearch import clCountSort

# test with search string = "the" and search type 1
def test_clCountSort_a():
    searchString = "the"
    searchType = "1"
    a = clCountSort()
    fileName1, fileCount1, fileName2, fileCount2, fileName3, fileCount3, totalTime = a.methCountSort(searchString,searchType)

    assert fileName1 == "french_armed_forces.txt"
    assert fileCount1 == 59
    assert fileName2 == "hitchhikers.txt"
    assert fileCount2 == 24
    assert fileName3 == "warp_drive.txt"
    assert fileCount3 == 9
    print("\nTotal Time test test_clCountSort_a:", totalTime)

# test with search string = "an" and search type 2
def test_clCountSort_b():
    searchString = "an"
    searchType = "2"
    b = clCountSort()
    fileName1, fileCount1, fileName2, fileCount2, fileName3, fileCount3, totalTime = b.methCountSort(searchString,searchType)

    assert fileName1 == "french_armed_forces.txt"
    assert fileCount1 == 88
    assert fileName2 == "hitchhikers.txt"
    assert fileCount2 == 23
    assert fileName3 == "warp_drive.txt"
    assert fileCount3 == 14
    print("\nTotal Time test test_clCountSort_b:", totalTime)

# test with search string = "and" and search type 3
def test_clCountSort_c():
    searchString = "and"
    searchType = "3"
    c = clCountSort()
    fileName1, fileCount1, fileName2, fileCount2, fileName3, fileCount3, totalTime = c.methCountSort(searchString,searchType)

    assert fileName1 == "french_armed_forces.txt"
    assert fileCount1 == 30
    assert fileName2 == "hitchhikers.txt"
    assert fileCount2 == 11
    assert fileName3 == "warp_drive.txt"
    assert fileCount3 == 3
    print("\nTotal Time test test_clCountSort_c:", totalTime)
