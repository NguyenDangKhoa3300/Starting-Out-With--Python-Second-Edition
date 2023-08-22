# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:26:50 2023

@author: mrpot
"""

def main():
    kilometers = float(input('Enter a distance in km: '))
    kmConverter(kilometers)
    
def kmConverter(km):
    miles = km * 0.6214
    print(km, 'km =', miles, ' miles')
    
main()
    
    