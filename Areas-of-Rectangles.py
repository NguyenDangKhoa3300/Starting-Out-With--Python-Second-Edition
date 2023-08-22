# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:26:08 2023

@author: mrpot
"""

def main():
    h1 = float(input('Enter the height of the 1st regtangle: '))
    w1 = float(input('Enter the width of the 1st regtangle: '))
    h2 = float(input('Enter the height of the 2nd regtangle: '))
    w2 = float(input('Enter the width of the 2nd regtangle: '))
    
    regtangle(h1, w1, h2, w2)
    
def regtangle(height1, width1, height2, width2):
    area1 = height1*width1
    area2 = height2*width2
    
    if area1 > area2:
        print('The first regtangle is greater than the second regtangle:', area1, '>', area2 )
    elif area1 == area2:
        print('Those regtangle are the same', area1, '=', area2 )
    else:
        print('The second regtangle is greater than the first regtangle', area1, '<', area2 )
        
main()