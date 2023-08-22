# -*- coding: utf-8 -*-
"""
Created on Fri May 26 09:28:54 2023

@author: mrpot
"""

def main():
    print(averageRainFall())

def averageRainFall():
    inchesOfRain = 0
    totalMonth = 0
    y = int(input('Enter the number of year: ')) 
    
    for year in range(1,y+1):
        for month in range(1, 13):
            rainFall = float(input('Enter the inches of rain: '))
            inchesOfRain += rainFall
            totalMonth += 12
    
    average = inchesOfRain/totalMonth
    return 'Number of month: ' + str(totalMonth) + '\nTotal inches of rain fall: ' + str(inchesOfRain) + '\nAverage rain fall per month: ' + str(average)

main()