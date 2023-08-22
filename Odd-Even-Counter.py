# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:53:29 2023

@author: mrpot
"""
import random

def main():
    print(countOddEvenNum())

def countOddEvenNum():
    oddCount = 0
    evenCount = 0
    for i in range(0, 100):
        number = random.randint(0, 100)
        if number % 2 == 0:
            #print('Odd number')
            oddCount += 1
        else:
            #print('Even number')
            evenCount += 1
    
    return 'Count of odd number', oddCount, 'Count of even number', evenCount 

main()