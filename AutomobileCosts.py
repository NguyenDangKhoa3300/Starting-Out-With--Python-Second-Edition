# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:22:47 2023

@author: mrpot
"""

def main():
    loan = float(input('Enter the loan: '))
    insurance = float(input('Enter the insurance: '))
    gas = float(input('Enter the gas: '))
    oil = float(input('Enter the oil: '))
    tires = float(input('Enter the tires: '))
    maintenance = float(input('Enter the maintenance: '))
    automobileCost(loan, insurance, gas, oil, tires, maintenance)

def automobileCost(loan, insurance, gas, oil, tires, maintenance):
    total_monthly_cost =  loan + insurance + gas + oil + tires + maintenance
    total_annual_cost = total_monthly_cost*12
    print('The total monthly cost of these expenses =', total_monthly_cost, '$',
          '\nThe total annual cost of these expenses =', total_annual_cost, '$')

main()