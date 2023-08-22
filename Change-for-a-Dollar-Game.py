# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:10:00 2023

@author: mrpot
"""

def main():
    pennies = float(input('Input the number: '))
    nickels = float(input('Input the number: '))
    dimes = float(input('Input the number: '))
    quarters = float(input('Input the number: '))
    
    dollarGame(pennies, nickels, dimes, quarters)

def dollarGame(pennies, nickels, dimes, quarters):
    total = pennies*0.01+nickels*0.05+dimes*0.1+quarters*0.25
    if total == 1:
        print('Congratulation you win the game!')
    else:
        print('You loss')

main()
    