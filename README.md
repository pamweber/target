# TARGET
Interview Case Study for Target

## Environment

This describes my technical environment for completing this exercise.

- Hardware
    - MacBook Pro (Retina, 13-inch, Early 2015)
    - Processor : 3.1 GHz Intel Core i7
    - Memory : 16 GB 1867 MHz DDR3
    - Operating System : macOS Mojave Version 10.14
- IDE : Komodo Edit 11 (https://www.activestate.com/products/komodo-edit/)
- Language : Python 3.7 (https://www.python.org)
- Test Framework : PyTest 4.3.1 (https://docs.pytest.org/en/latest/)
- Test Plugins
    - pytest-repeat 0.8.0 : https://pypi.org/project/pytest-repeat/
- Version Control
    - DVCS : Git version 2.15.0 for mac - https://git-scm.com/downloads
    - Git GUI : Atlassian SourceTree Version 3.1.1 (213) - https://www.atlassian.com/software/sourcetree
    - Local git repository : /Users/pam/gitrepos/Target/target
    - GitHub repository : https://github.com/pamweber/target
    - this file: https://github.com/pamweber/target/blob/master/README.md
- Personal documentation : Confluence Space running on local Confluence Server instance - http://confluence:8080

## Approach

My approach was as follows:
1. **Select case study** - I decided to do Case Study 3, Document Search, because it seemed similar to the type of scripting I might be doing within a tool
1. **Select language** - I selected Python for the language because:
    - Python is frequently used for scripting
    - I had taken a basic Python course a few years ago and wanted to learn more about the language
1. **Write basic program** - first challenge was to refresh my Python skills by writing the basic program logic
1. **Update Python** - I started with Python 2.7 which was on my MBP by default, then installed Python 3.7.2 and converted my code to Python 3
1. **Clean up the program** - then I moved on to making the program a bit more elegant by adding some exception handling and functions 
1. **Automate tests** - I looked at Python *unittest* and *pytest* and decided to use *pytest* because it seemed easier and at the same time more robust
    - this required some additional refactoring of the program, such as the use of classes and methods
1. **Performance Test** - I researched different ways to run the tests multiple times and in the process came across *pytest-repeat* which was extremely easy to implement
    - execute the program 2M times:  pytest --count=2000000 DocumentSearch_type1_test.py
1. **Timers** - Set up some timers around the multiple tests
1. **Input runtime variables** - in preparation for randomizing the test input, I created a new test module that accepts command line parameters and eliminated pytest-repeat
1. **Random values** - I did not complete the portion of the exercise that would feed random search terms into the program

## Files

- **DocumentSearch.py** - the main program logic
- **DocumentSearch_run.py** - used to run the main program
    >python3 DocumentSearch_run.py
- **DocumentSearch_test.py** - used to run three tests against the main program using PyTest
    >pytest DocumentSearch_test.py -s
- **DocumentSearch_load_test.py** - used to run multiple tests of the main program with command line arguments
    >pytest DocumentSearch_load_test.py --term=<search term> --method=<search method> --times=<# of times to run> -s
- **timer.txt** - used by DocumentSearch_load_test.py to accumulate the total run time in milliseconds
- **conftest.py** - pytest configuration file used by DocumentSearch_load_test.py to capture command line arguments
- **data folder** - contains the text files provided with the case study
- **Output folder** - contains sample results from running DocumentSearch_load_test.py 

## Executing Volumne Tests

This provides more details on running the volume tests using DocumentSearch_load_test.py.

### Pre-requisites:
1. Install Python 3
1. Install pytest
1. Install pytest-repeat
1. Install Git
1. Clone GitHub repository to local repository

### Running the program

1. To run the program stand-alone and enter search string and type:
    >python3 DocumentSearch_run.py
1. To run three tests against predicted results:
    >pytest DocumentSearch_test.py
1. To run a test with verbose output
    >pytest -v DocumentSearch_test.py
1. To run a test with verbose output and print stdout 
    >pytest -v -s DocumentSearch_test.py
1. To count and sort occurances of "the" using search method 1 repeated 500 times:
    >pytest DocumentSearch_load_test.py --term=the --method=1 --times=500 -s
1. To count and sort occurances of "an" using search method 2 repeated 10,000 times:
    >pytest DocumentSearch_load_test.py --term=an --method=2 --times=10000 -s
1. To count and sort occurances of "a" using search method 3 repeated 50,000 times:
    >pytest DocumentSearch_load_test.py --term=a --method=3 --times=50000 -s

## Potential improvements
1. Write volumne test output to a data structure for reporting
1. Randomize search term for volume tests 
1. Containerize the python environment for better metrics

## Description of the Problem Assignment

### Technical Assessment Case Studies
The purpose of the Case Study is not only to gauge your technical ability, but also to see how you think.  We will talk through your results here and your logic.  The Case Study is not a make or break your candidacy for the role, but serve as a single data-point among your overall qualifications.  
___
Please complete one of following case studies:
1.	myRetail RESTful service
1.	Barren Land Analysis
1.	Search (SELECTED)
___
For the case study you choose please meet the following requirements:
- Complete the exercise in the technical stack of your choice.
    - When appropriate use a data store of your choice.
    - Use any external frameworks you desire
    - Be ready to discuss your recommendations to make your solution suitable for use in a production environment 

- Provide evidence of the result to the interviewers (choose one)
    - Unit test results or other documented output
    - Hosted instance of the implementation
    - Runnable instance of the implementation on your computer

- The end result should be a functional implementation of the problem preferably with associated tests
    - Provide the working code either in a publicly accessible hosted repository or a zip file containing all necessary build steps and dependencies
    - Rename .js files to .js.txt if emailing code
    - Provide a README.md file with instructions for testing, running and interacting with your application and any details you feel are relevant to share

### Document Search Specifications

The goal of this exercise is to create a working program to search a set of documents for the given search term or phrase (single token), and return results in order of relevance. 
Relevancy is defined as number of times the exact term or phrase appears in the document. 

Create three methods for searching the documents: 
- Simple string matching
- Text search using regular expressions
- Preprocess the content and then search the index

Prompt the user to enter a search term and search method, execute the search, and return results.

For instance:

![Output Example](/ExampleOutput.jpg "Output Example")

Three files have been provided for you to read and use as sample search content.

Run a performance test that does 2M searches with random search terms, and measures execution time. Which approach is fastest? Why?

Provide some thoughts on what you would do on the software or hardware side to make this program scale to handle massive content and/or very large request volume (5000 requests/second or more). 


# RESOURCES

Because this was a large learning effort for me, I made use of many online resources to refresh my knowledge of python and learn new skills.

- python
    - PYTHON FOR INFORMATICS (course book) - https://d28rh4a8wq0iu5.cloudfront.net/pythonlearn/book/book_270.pdf
    - general reference - http://anh.cs.luc.edu/handsonPythonTutorial/index.html
    - read entire file - https://docs.python.org/2/library/functions.html#open
    - timer - https://stackoverflow.com/questions/7421641/measuring-elapsed-time-in-python/13261556
    - input loop - https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
    - if-elif-else - https://www.w3schools.com/python/python_conditions.asp
    - count elements
        - https://www.lucidar.me/en/python/count-elements/
        - https://stackoverflow.com/questions/8899905/count-number-of-occurrences-of-a-given-substring-in-a-string/8900059
    - regular expressions
        - https://docs.python.org/2.7/library/re.html
        - https://blog.teamtreehouse.com/regular-expressions-10-languages
        - https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
    - run time arguments with pytest
        - https://docs.python.org/2/howto/argparse.html
    - python testing
        - https://realpython.com/python-testing/
        - https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
    - classes, methods, and objects
        - https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/
        - https://docs.python.org/2/tutorial/classes.html
    - installation of python 3 on a mac
        - http://osxdaily.com/2018/06/13/how-install-update-python-3x-mac/
    - Return multiple values from a function
        - https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
        
- markdown syntax
    - https://www.markdownguide.org/basic-syntax/
    - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

