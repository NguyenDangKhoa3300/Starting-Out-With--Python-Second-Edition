# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:36:19 2023

@author: mrpot
"""

def main():
    days = int(input('Enter number of days: '))
    print('The total of bug collected in', days, 'days are', bugCollector(days) )

def bugCollector(days):
    numBug = 0
    for weekdays in range(days):
        print('....Day', weekdays+1, 'collected....')
        bugCollected = int(input('Enter the number of bug collected: '))
        numBug += bugCollected
    
    return numBug

main()

        