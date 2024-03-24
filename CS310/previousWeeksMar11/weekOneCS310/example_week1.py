#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:57:33 2020

@author: clemens
"""
import random




#Hello World in Python

def hello():
    """ Hello World """
    print("Hello" +  " World!")


#example of a simple game
    
def game(n):
    """ start game where computer thinks of a number between 0 and n,
    the user has to guess the number"""
    if type(n)!=int or n <= 0:
        print("Argument of game has to be a positive integer")
    else:
        number = random.randint(1,n)
        count = 0
        guessed = False
        while (guessed == False):
            guessed = guess(number)
            count = count + 1
        print ("It took you {} guesses".format(count))
            
        
def guess(n):
    """ function that prompts for user guesses """
    ourinput = "dummy"
    while (type(ourinput)!=int):
        try:
            ourinput = int(input("Make a guess!"))
        except ValueError:
            print("Enter a number!")
    if (ourinput < n):
        print ("My number is bigger!")
        return False
    elif (ourinput > n):
        print ("My number is smaller!")
        return False
    else:
        print ("You've guessed my number!")
        return True
    

        
#another example         
def rev(s):
    """ reversing a string """
    r = ""
    for i in range(len(s)):
        r= r + s[(-1)*i - 1]
    return r


if __name__ == "__main__":
    #hello()
    print(rev("Clemens"))
    #game('wow')
        



