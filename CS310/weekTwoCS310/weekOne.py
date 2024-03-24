print("Hello World")

"""
   A longer comment uses 3 quotes     Change package to add ipython and run in python console
        """

# A short quote uses a simple '#' sign

# float
b = 3.13
# Int
a = 5

# dynamic typing, a variable does not have a fixed type

# explicit coercions

c = "4"

# an empty list

# String in double quotes

name = "clemens"

empty = []

listexample = ["Hell world", 100, True]

listname = list(name)


# Slicing
# name[-1]
# name [1:-1]

# create a copy of the list name3 = name2.copy()

# Generator

nlist = [x for x in range(0,20)]

name2 = list("Clemens")

namecopy = name[:]

# arrays external feature


import numpy as np

#n = np.array(range(1.11))

# array can only have elements of the SAME TYPE

test = np.array(["Hello", 26])

# Dictionaries
adict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
salaries = {'Fred': 34569, 'Jeff': 23445, 'Catrina': 36213}
items = adict.items()
adict2 = adict

""" Print the dicitonary in iPython 
for key in adict: 
    print(key)
    
color
fruit
pet

for key in adict:
    print(adict[key])
    
blue
apple
dog

for key in adict.items():
    print(key)
    
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')

Adding:

adict['city'] = 'Glasgow'
adict
Out[9]: {'color': 'blue', 'fruit': 'apple', 'pet': 'dog', 'city': 'Glasgow'}

adict2 = adict.copy()
adict2
Out[11]: {'color': 'blue', 'fruit': 'apple', 'pet': 'dog', 'city': 'Glasgow'}

Keys in dictionaries have to be simple, if you have a complicated key make it simple,

I.e if your key is for instance a list them store it as a string first then wrok around it later...

refer to week 1 lecture video python dictionaries

"""

# Functions in Python

# simple functions

# Fibonacci sequence: 1,1,2,3,5,8,13,...

def fib(n): # generating the Fibonacci Sequence until n
    result = []
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n): # Generating the Fibonacci sequence until n
    result = []
    a, b = 0,1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def fib3(n): # Generating the first n elements of the Fibonacci sequence
    result = []
    a, b = 0,1
    for n in range (0,n):
        result.append(b)
        a,b = b, a+b
    return result
# making actual methods
def hello():
    """ hello world"""
    print("Hello" +" World!")

