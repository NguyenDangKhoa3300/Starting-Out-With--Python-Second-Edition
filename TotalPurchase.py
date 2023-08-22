# -*- coding: utf-8 -*-
"""
Created on Tue May 23 10:48:20 2023

@author: mrpot
"""

first_item = float(input('Enter the price of the 1st item: '))
second_item = float(input('Enter the price of the 2nd item: '))
third_item = float(input('Enter the price of the 3rd item: '))
fourth_item = float(input('Enter the price of the 4th item: '))
fifth_item = float(input('Enter the price of the 5th item: '))

sales_tax = 0.06

subtotal = first_item + second_item + third_item + fourth_item + fifth_item
sales_tax_amount = subtotal * sales_tax
total_prices = subtotal + sales_tax_amount

print('Subtotal:', subtotal, '\nSales tax amount:', sales_tax_amount, '\nTotal prices:', total_prices)