# -*- coding: utf-8 -*-
"Exercise 3.2"

def twice (f,a):
    "Defining a function twice which takes a function object 'f' and a value 'a'and run it twice"
    f(a)
    f(a)
def print_twice(bruce):
    "Defining a function print_twice which is assigned to an argument bruce to print it twice"
    print(bruce)
    print(bruce)

twice(print_twice,'spam')
"uses function twice to call print_twice with argument spam as a value"
