# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:52:32 2023

@author: mrpot
"""

import random

def main():
    print(plusMathQuizes())

def plusMathQuizes():
    number1 = random.randint(0, 999)
    number2 = random.randint(0, 999)
    print(number1, '\n+\n', number2, '\n-----------')
    numSum = number1 + number2
    userAnswer = int(input('Enter the answer: '))
    
    if userAnswer == numSum:
        return 'Congratulations!!!'
    else:
        return 'Wrong answer'

main()
