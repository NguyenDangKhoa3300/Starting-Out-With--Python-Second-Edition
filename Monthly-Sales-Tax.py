# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:22:38 2023

@author: mrpot
"""

def main():
    totalSales = float(input('Enter the total sales: '))
    taxCount(totalSales)

def taxCount(totalSales):
    countyTax = totalSales*0.02
    stateTax = totalSales*0.04
    
    totalTax = countyTax+stateTax
    
    print('The amount of county sales tax', countyTax, '$'
          '\nThe amount of state sales tax', stateTax, '$',
          '\nThe total sales tax (county plus state)', totalTax, '$')

main()