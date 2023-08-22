# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:35:58 2023

@author: mrpot
"""

def main():
    mass = float(input('Enter the mass: '))
    weightCount(mass)

def weightCount(mass):
    weight = mass*9.8
    
    if weight > 1000:
        print('Too heavy')
    elif weight < 10:
        print('Too light')
    else:
        print('Normal')

main()