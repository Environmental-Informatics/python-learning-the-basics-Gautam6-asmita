"""Created on 2020-01-16 by Asmita Gautam
Assignment 01: Python - Learning the Basics
Think Python Chapter 3: Exercise 3.3
Modified to add header and comments for resubmission on 2020-03-04
"""

"""
While considering th each rows of the grid we can see 2 patters of the rows
The first pattern is +----+----+ and the second is |    |    |
"""

##Defining a function first to print a first row of matrix
def first():
    print('+----+----+')
    
##Defining a function second to print a second row of matrix
def second():
    print('|    |    |')

##Defining a function grid to call a mixture of first and second function so it appears like a matrix"
def grid():
    first()
    second()
    second()
    second()
    second()
    first()
    second()
    second()
    second()
    second()
    first()

#Displaying the function "grid"
grid()

"""
Here the functions used are def: used to define a function, 
print: will print everything as indicated within the ' ' 
"""
