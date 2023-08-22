# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:51:56 2023

@author: mrpot
"""

def main():
    min1 = int(input('Enter minutes 1: '))
    min2 = int(input('Enter minutes 2: '))
    step = int(input('Enter the step: '))
    print(caloriesBurnedCount(min1, min2, step))

def caloriesBurnedCount(min1, min2, step):
    totalCal = 0
    for minutes in range(min1, min2, step):
        caloBurned = minutes*3.9
        totalCal += caloBurned
        print('Return calo burned in', minutes, 'minutes =', caloBurned, 'calc')
    
    return 'The total calories you have burned = ' + str(totalCal) + ' calc'

main()