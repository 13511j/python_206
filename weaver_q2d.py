#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:22:20 2021

@author: janweaver
"""

#make a class called "BankAccount" that has 3 properties
#      account number, balance, and fees
#when a BankAccount object is initialized, it should take parameters for accountnumber
#and balance and fees and set fees to 0. 
#create a function 'Check' in the class that asks for the accountnumber and if they 
#type it in correctly print the balance and current fees. otherwise, print 'Wrong Number.'


#i didn't really understand the part about setting the account fees to zero
#so i just... kind of made that up. the user can basically put in whatever they want and
#it'll reset the fees to zero on its own. hopefully that was the goal. 
class BankAccount:
    def __init__(self, accountnumber, balance, fees):
        self.accountnumber = accountnumber
        self.balance = balance
        self.fees = 0
    def Check(self):
        accountnumber = int(input('enter your account number:   '))
        if accountnumber == self.accountnumber:
            print('your balance is: $' , self.balance, '\nyour fees are: $', self.fees)
            
        else:
            print('Wrong Number')
            
        