# -*- coding: utf-8 -*-
"""
Created on Wed May 24 08:55:32 2023

@author: mrpot
"""

def main():
    amtPurchase = float(input('Enter the amount of a purchase:' ))
    purchaseCount(amtPurchase)

def purchaseCount(amountPurchase):
    state_tax = amountPurchase*0.04
    city_tax = amountPurchase*0.02
    total_tax = state_tax + city_tax
    total_sale = amountPurchase + total_tax
    
    print('The amount of the purchase =', amountPurchase, '$', 
          '\nThe state sales tax =', state_tax, '$',
          '\nThe country sales tax =', city_tax, '$',
          '\nThe total sales tax =', total_tax, '$'
          '\nThe total of the sale =', total_sale, '$')

main()