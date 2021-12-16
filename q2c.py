#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:10:22 2021
"""

#write code that randomly generates a number, then loops that many times while
#asking the user to input numbers into a list.
#once done, ask the user if they want the sum of the list, mean of the list, or to sort the list
#then print out the result. 

#importing my faves
import random
import numpy

#making a list to store the user input
userlist = []

#i made the range for this short while i was double checking my work but if you want
#to risk a huge random number then go for it
for i in range(random.randint(1,5)):
    userlist.append(int(input('add a number to the list:  ')))

#asks the user what they want to do
question = input('do you want to \n 1. get the sum of the list? \n 2. get the mean of the list? \n 3. sort the list? \n enter here: ')

#does what the user says and prints the result. also prints an error message
#if the user types something besides 1, 2, or 3
if question == '1': 
    print('the sum of your list is:  ', (sum(userlist)))
elif question == '2':
    print('the mean of your list is:  ', (numpy.mean(userlist)))
elif question == '3':
    print('the order of your list from smallest to largest is: ', (numpy.sort(userlist)))
else:
    print('that is not an option')
