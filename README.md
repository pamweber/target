# TARGET
Interview Case Study for Target

## Technical Assessment Case Studies
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

## Document Search Specifications

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
- GitHub - https://github.com/pamweber/target/blob/master/README.md

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
        
- markdown syntax
    - https://www.markdownguide.org/basic-syntax/
    - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

