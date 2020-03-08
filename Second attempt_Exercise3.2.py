#!/usr/bin/env python3
# -*- coding: utf-8 -*-#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-01-16 by Asmita Gautam
Assignment 01: Python - Learning the Basics
Think Python Chapter 3: Exercises 3.2
Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
Modified to add header and comments for resubmission on 2020-03-04
"""

"""
This function takes two arguments: a function object'f' and value'a'
Calls the function twice by passing the value argument in the first funtion
as the argument for the function called
"""
#Defining a function "twice" which takes a function object 'f' and a value 'a'and run it twice
def twice(f,a):
    f(a)
    f(a)

"""
This function prints the argument value twice
"""
#Defining a function print_twice which is assigned to an argument bruce to print it twice"
def print_twice(bruce):
    print(bruce)
    print(bruce)

#Using function twice to call print_twice with argument spam as a value
twice(print_twice,'spam')




