#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 23:21:51 2021
"""

#pretend you have a file called 'file.txt'.
#check to see if the file exists, if so print out the contents of this file, 
#then add the string 'Hello, Final!' to the bottom of the file, then
#print the file out again. 

#importing the necessary thing
import os

if os.path.exists('file.txt'):
    #there was probably a more sophisticated way to do this but everything i tried
    #kept throwing a ton of errors so i went very basic
    file = open('file.txt', 'r') #opens the file to read it
    print('original text:', file.read()) #prints what it finds
    file.close()
    file = open('file.txt', 'a') #opens the file to add a line
    file.write('\nHello, Final!') #adds the line
    file.close()
    file = open('file.txt', 'r') #opens the file to read it again
    print('new text:', file.read()) #prints what it finds
    file.close()
else:
    print('no file found') #i tested this and it does actually work
    

#i put "original text" and "new text" labels on so i could figure out what was printing out
#it was getting confusing without them
