# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:46:41 2023

@author: mrpot
"""

def main():
    feet = float(input('Enter the number of feet: '))
    print(feet_to_inches(feet))

def feet_to_inches(numFeet):
    numInches = numFeet*12
    return str(numFeet) + ' feet equals ' + str(numInches) + ' inches'

main()