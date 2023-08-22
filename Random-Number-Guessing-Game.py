# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:32:24 2023

@author: mrpot
"""
import random

def main():
    userInput = int(input('Enter the number: '))
    guessingGame(userInput)

def guessingGame(userInput):
    number = random.randint(0, 100)
    print('The random number is:', number)
    count = 0
    while userInput != '':
        if userInput > number:
            print('Too high, try again')
        elif userInput == number:
            print('Congratulations')
            break
        else:
            print('Too low, try again')
        
        count += 1
        userInput = int(input('Enter the number: '))
    
    print('The number of guessing:', count + 1)
    
main()