# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:38:42 2023

@author: mrpot
"""

food_prices = float(input('Enter the charge for the food: '))
tips = food_prices*0.15
sales_tax = food_prices*0.07
total_payment = food_prices + tips + sales_tax

print('Food charge =', food_prices,
      '\nTips =', tips,
      '\nSales tax =', sales_tax,
      '\nTotal payment =', total_payment)