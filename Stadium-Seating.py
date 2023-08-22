# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:48:52 2023

@author: mrpot
"""

def main():
    ticketASold = int(input('Enter the number of ticket A sold: '))
    ticketBSold = int(input('Enter the number of ticket B sold: ')) 
    ticketCSold = int(input('Enter the number of ticket C sold: ')) 
    
    incomeCount(ticketASold, ticketBSold, ticketCSold)
    
def incomeCount(classA, classB, classC):
    incomeA = classA * 15
    incomeB = classB * 12
    incomeC = classC * 9
    
    print('Income from seat A =', incomeA, '$',
          '\nIncome from seat B =', incomeB, '$',
          '\nIncome from seat C =', incomeC, '$')

main()