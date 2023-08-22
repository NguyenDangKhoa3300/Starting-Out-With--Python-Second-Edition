# -*- coding: utf-8 -*-
"""
Created on Fri May 26 10:43:49 2023

@author: mrpot
"""

def main():
    penniesPay()

def penniesPay():
    dollars = 0
    pennies = 0
    total_pay = 0
    d = int(input('Enter the number of days: '))
    
    print('Days\tPennies\n..........................')
    for days in range(1, d+1):
        if days == 1:
            pennies += 1
            dollars += pennies*0.01
        else:
            pennies *= 2
            dollars += pennies*0.01
        
        total_pay += dollars
        print(days, '\t\t', dollars, '$')
    
    print('..........................\nTotal pay =', total_pay, '$')
    
main()