#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:11:53 2021

"""

#write a function called EvensAndOdds that takes a list as a parameter.
#the function should print 'Evens:' followed by all of the even numbers
#then 'Odds:' followed by all of the odd numbers. 
  
#making some empty lists for later  
evennumbies = []
oddnumbies = []

#making the function
def EvensAndOdds(list):
#the for loop does the sorting. the +1 is to make sure it gets the last number in the list. 
    for i in range(1, len(list)+1):
        if i % 2 == 0: 
            evennumbies.append(i)
        else:
            oddnumbies.append(i)

    print('Evens:', evennumbies)
    print('Odds:', oddnumbies)          

#i had a version of this that used user input that was cooler. 
#i wrote it to not include 0 as an even number because i just don't think 0 is an even number. 

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
EvensAndOdds(L)

