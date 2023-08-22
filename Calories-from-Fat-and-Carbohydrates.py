# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:31:28 2023

@author: mrpot
"""

def main():
    f_gram = float(input('Enter the number of fat grams: '))
    c_gram = float(input('Enter the number of carb grams: '))
    
    print(caloriesCal(f_gram, c_gram))
    
def caloriesCal(f_gram, c_gram):
    calFromFat = f_gram*9
    calFromCarb = c_gram*4
    
    return calFromFat, calFromCarb

main()