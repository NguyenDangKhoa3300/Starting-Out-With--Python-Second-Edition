# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:07:26 2023

@author: mrpot
"""

def main():
    replacementCost = float(input('Enter the replacement cost of a building: '))
    insuranceCount(replacementCost)

def insuranceCount(replacementCost):
    minimumAmt = replacementCost*0.8
    print('The minimum amount of insurance he or she should buy for the property is', minimumAmt, '$')
    
main()