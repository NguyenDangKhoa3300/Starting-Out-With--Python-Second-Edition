# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:08:07 2023

@author: mrpot
"""

def main():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    print(maximum(num1, num2))

def maximum(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return 'The same'
    else:
        return num2
main()