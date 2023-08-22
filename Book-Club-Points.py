# -*- coding: utf-8 -*-
"""
Created on Thu May 25 08:48:31 2023

@author: mrpot
"""

def main():
    numBook = int(input('Enter the number of book you have bought this month: '))
    print(clubPointsCount(numBook))

def clubPointsCount(numBook):
    clubPoint = 0
    if numBook == 0:
        clubPoint += 0 
    elif numBook == 1:
        clubPoint += 5
    elif numBook == 2:
        clubPoint += 15
    elif numBook == 3:
        clubPoint += 30
    else:
        clubPoint += 60
    
    return 'Your club point this month = ' + str(clubPoint)

main()