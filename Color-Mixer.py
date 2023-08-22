# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:55:32 2023

@author: mrpot
"""

def main():
    color1 = input('Enter a color: ')
    color2 = input('Enter a color: ')
    print('Mixing color.....')
    
    colorMixer(color1, color2)
    
def colorMixer(color1, color2):
    if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
        print('purple')
    elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
        print('orange')
    elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
        print('green')
    else:
        print('Please enter red, yellow or blue')
    
main()