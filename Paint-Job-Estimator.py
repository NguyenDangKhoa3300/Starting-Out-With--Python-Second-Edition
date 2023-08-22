# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:01:14 2023

@author: mrpot
"""
def main():
    sqWall = int(input('Enter  the square feet of wall space to be painted: '))
    paintPrice = float(input('Enter the price of the paint per gallon: '))
    paintJobEsti(sqWall, paintPrice)

def paintJobEsti(sqWall, paintPrice):
    gallon = sqWall/115
    time = sqWall*8/115
    laborCharge = time*20.00
    total = paintPrice + laborCharge
    
    print('The number of gallons of paint required:', gallon, '(gallon)'
          '\nThe hours of labor required:', time, '(hours)'
          '\nThe cost of the paint:', paintPrice, '$',
          '\nThe labor charges:', laborCharge, '$'
          '\nThe total cost of the paint job:', total, '$')

main()