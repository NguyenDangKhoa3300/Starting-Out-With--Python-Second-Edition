# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:38:15 2023

@author: mrpot
"""

def main():
    pieceOfPropertyValue = float(input('Enter the actual value of a piece of property: '))
    propertyTaxCount(pieceOfPropertyValue)

def propertyTaxCount(pieceOfPropertyValue):
    accessmentVal = pieceOfPropertyValue*0.6
    propertyTax = accessmentVal*0.0064
    
    print('Accessment value =', accessmentVal, '$',
          '\nProperty tax =', propertyTax, '$')
    
main()