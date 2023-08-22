# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:09:13 2023

@author: mrpot
"""

def main():
    amountBudget = float(input('Enter the amount that you have budgeted for a month: '))
    print(budgetAnalyze(amountBudget))

def budgetAnalyze(amountBudget):
    userChosen = input('Enter y to enter your expenses, n to exit: ')
    total = 0
    while userChosen == 'y':
        expenses =float(input('Enter your expends: '))
        total += expenses
        print('Your total expenses at the time:', total)
        userChosen = input('Enter y to continue, n to exit: ')
    
    if amountBudget > total:
        print('Under budget', 'Budget:', amountBudget, '> Total expenses:', total)
    else:
        print('Over budget!!! ->', 'Budget:', amountBudget, '<= Total expenses:', total)
    
    return total
main()
        