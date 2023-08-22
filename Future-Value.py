# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:24:43 2023

@author: mrpot
"""

def main():
    presentVal = float(input('Enter the present value: '))
    monthlyInterestRate = float(input('Enter the monthly interest rate: '))
    numMonth = int(input('Enter the number of month: '))
    print(futureVal(presentVal, monthlyInterestRate, numMonth))

def futureVal(p, i, t):
    f = p * pow(1+i, t)
    return f

main()