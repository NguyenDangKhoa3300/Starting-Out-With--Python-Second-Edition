# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:31:18 2023

@author: mrpot
"""

def main():
    weight = float(input('Enter your weight (kg): '))
    lbs = weight*2.20462262
    height = float(input('Enter your height (cm): '))
    inch = height*0.39370079
    
    bmiCal(lbs, inch)

def bmiCal(weight, height):
    bmi = (weight*703)/pow(height, 2)
    
    print('Your body mass index =', bmi)
    
    if bmi < 18.5:
        print('Thin')
    elif bmi >= 18.5 and bmi <= 24.9:
        print('Normal')
    elif bmi >= 25 and bmi <= 29.9:
        print('Fat')
    elif bmi >= 30 and bmi <= 34.9:
        print('Very fat')
    else:
        print('DANGEROUS')
    
    
main()