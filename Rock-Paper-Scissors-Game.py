# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:20:26 2023

@author: mrpot
"""
import random

rock = 1
paper = 2
scissors = 3

def main():
    userInput = int(input('Enter a number\n1) rock\n2) paper\n3) scissors\n..........\n'))
    game(userInput)

def game(userInput):
    machineInput = random.randint(1, 3)
    if userInput == rock and machineInput == scissors or userInput == scissors and machineInput == paper or userInput == paper and machineInput == rock:
        print('User win', machineInput)
    elif userInput == machineInput:
        print('Draw', machineInput)
    else:
        print('Machine win', machineInput)
    
main()        