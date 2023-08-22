# -*- coding: utf-8 -*-
"""
Created on Fri May 26 11:39:26 2023

@author: mrpot
"""

row = int(input('Enter the number of row: '))
emptyString = ''

for i in range(row):
    for c in range(i+1):
        print('*', end='')
    print()