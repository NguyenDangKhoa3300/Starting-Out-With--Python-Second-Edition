# -*- coding: utf-8 -*-
"""
Created on Fri May 26 10:24:23 2023

@author: mrpot
"""

def main():
    print(cToFCal())

def cToFCal():
    print('Celsius\t\tFahrenheit\n......................')
    for celsius in range(21):
        fahrenheit = (9/5)*celsius + 32
        if celsius < 10:    
            print(celsius, '℃\t\t\t', fahrenheit , '℉') 
        else:
            print(celsius, '℃\t\t', fahrenheit , '℉') 
        #str(celsius) + '℃\t\t' + str(fahrenheit) + '℉'
        
    

main()