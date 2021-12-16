#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:02:27 2021

@author: janweaver
"""

#write a function that has three parameters, x y, and z, and returns a list
#of all numbers between x and y except for those divisible by z.
#then call this function on the numbers 10, 20, and 4 and print out all of the numbers
#in the list one at a time. 

#making some lists to save the divisible and non-divisible numbers
listylist = []
trashlist = []

#i really couldn't think of a name for this function that made sense that wouldn't
#soverlap with a real function i've made that i use so... sorry for the name. 
def CouldntThinkOfAName(x, y, z):
    for i in range(x, y):   #for loops, forever
        if i % z == 0:
            trashlist.append(i) #puts the divisible numbers in a list
        else: 
            listylist.append(i) #puts the non-divisible numbers in a list
               
CouldntThinkOfAName(10, 20, 4) #calls the function for the numbers given in the instructions
print(*listylist, sep='\n') #prints the non-divisible numbers one at a time 

#sorry i never put comments on any of my homework or quizzes i just really want to maintain
#my A in this class and comments explaining my logic on the final seemed helpful in my mission 
#to do that