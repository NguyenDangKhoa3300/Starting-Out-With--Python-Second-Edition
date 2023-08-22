# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:40:52 2023

@author: mrpot
"""

def main():
    day = int(input('Enter the day: '))
    month = int(input('Enter the month: '))
    year = int(input('Enter the year: '))
    
    magicDates(day, month, year)

def magicDates(day, month, year):
    if year >= 10 and year <= 99:
        if day*month == year:
            print('The date is magic')
        else:
            print('The date is not magic')
    else:
        print('Please enter 2 digits for the year!')
main()