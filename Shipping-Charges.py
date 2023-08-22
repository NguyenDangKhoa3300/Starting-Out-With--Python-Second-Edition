# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:23:36 2023

@author: mrpot
"""

def main():
    weight = float(input('Enter the weight of a package: '))
    print(shippingCharges(weight))

def shippingCharges(weight):
    shipping = 0
    if weight <= 2:
        shipping += weight * 1.1
    elif weight > 2 and weight < 6:
        shipping += weight * 2.2
    elif weight >= 6 and weight < 10:
        shipping += weight * 3.7
    else:
        shipping += weight * 3.8
    
    return 'Your shipping charge = ' + str(shipping) + '$'

main()