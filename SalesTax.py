# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:21:36 2023

@author: mrpot
"""

amount_of_purchase = float(input('Enter the amount of purchase: '))
state_sales_tax = amount_of_purchase*0.04
country_sales_tax = amount_of_purchase*0.02
total_tax = state_sales_tax + country_sales_tax
total_sales = amount_of_purchase + total_tax
print('The amount of the purchase:', amount_of_purchase, 
      '\nState sales tax:', state_sales_tax, 
      '\nCountry sales tax:', country_sales_tax,
      '\nTotal sales tax:', total_tax,
      '\nTotal sales:', total_sales)