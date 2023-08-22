# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:01:26 2023

@author: mrpot
"""

def main():
    numPurchase = int(input('Enter the number of package purchased: '))
    print(softwareSale(numPurchase))

def softwareSale(numPurchase):
    packagePrice = 99
    total = numPurchase*packagePrice
    discount = 0
    
    if numPurchase >= 10 and numPurchase <= 19:
        discount += total*0.2
    elif numPurchase >= 20 and numPurchase <= 49:
        discount += total*0.3
    elif numPurchase >= 50 and numPurchase <= 99:
        discount += total*0.4
    elif numPurchase >= 100:
        discount += total*0.5
    else:
        return discount
    
    
    totalAfterDiscount = total-discount 
    
    return 'Your total = ' + str(total) + '$' + '\nYour discount = ' + str(discount) + '$' + '\nYour total amount of purchase after discount = ' + str(totalAfterDiscount) + '$'

main()