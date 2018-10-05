# PYTHON FOR EVERYBODY - SPECIALIZATION
## Offered by UNIVERSITY OF MICHIGAN
## on COURSERA


There are 5 courses in this specialization.

Course 1: Programming for Everybody (Getting Started with Python)

Course 2: Python Data Structures

Course 3: Using Python to Access Web Data

Course 4: Using Databases with Python

Course 5: Capstone: Retrieving, Processing, and Visualizing Data with Python


## Course 1: Programming for Everybody (Getting Started with Python)

These exercises covers Chapters 1 to 5 of the textbook "Python For Everybody - Exploring Data in Python 3" by Charles Severance.

The solutions are available in the folder "getting_started_with_python"


#### Exercise 2.2

Write a program that uses "input" to prompt a user for their name and then welcomes them


#### Exercise 2.3

Write a program to prompt the user for hours and rate per hour using input to compute gross pay. You should use input to read a string and float() to convert the string to a number.


#### Exercise 3.1

Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.


#### Exercise 3.3

Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using a given table. If the user enters a value out of range, print a suitable error message and exit.


#### Exercise 4.6

Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value.


#### Exercise 5.2

Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.


## Course 2: Python Data Structures

These exercises covers Chapters 6 to 10 of the textbook "Python For Everybody - Exploring Data in Python 3" by Charles Severance.

The solutions are available in the folder "python_data_structures"


#### Exercise 6.5:

Write code using find() and string slicing to extract the number at the end of the line below.

text = "X-DSPAM-Confidence:    0.8475"

Convert the extracted value to a floating point number and print it out.


#### Exercise 7.1:

Write a program that prompts for a file name then opens that file and reads through the file and print the contents of the file in upper case.


#### Exercise 7.2:

Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values. Do not use the sum() function or a variable named sum in your solution.


#### Exercise 8.4:

Open a file and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.


#### Exercise 8.5:

Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. Hint: make sure not to include the lines that start with 'From:'.


#### Exercise 9.4:

Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


#### Exercise 10.2:

Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon. 

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour.
