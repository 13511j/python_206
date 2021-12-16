#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:57:09 2021

"""

#using the above class (class from question 2d) write code that creates a new BankAccount
#object and calls Check on both a correct and incorrect accountnumber

#imports my masterpiece
from weaver_q2d import BankAccount 

#makes a new little banking account 
checkurself = BankAccount(1234, 47, 5) #i chose an account balance that accurately represents mine
#to check it with the correct account number enter 1234
checkurself.Check()
#to check it with the incorrect account number enter anything else
checkurself.Check()
