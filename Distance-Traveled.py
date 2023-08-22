# -*- coding: utf-8 -*-
"""
Created on Fri May 26 09:15:54 2023

@author: mrpot
"""

def main():
    speed = float(input('Enter the vehicle speed: '))
    time = int(input('Enter the time the vehicle has traveled: '))
    distanceCount(speed, time)

def distanceCount(speed, time):
    print('Hour\tDistance Traveled\n.........................')
    for timeTravel in range(1,time+1):
        distance = speed * timeTravel
        print(timeTravel , '\t\t', distance)
        
    

main()