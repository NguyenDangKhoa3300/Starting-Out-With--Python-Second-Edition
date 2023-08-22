# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:50:34 2023

@author: mrpot
"""
# The amount of money Joe paid for the stock.
# The amount of commission Joe paid his broker when he bought the stock.
# The amount that Joe sold the stock for.
# The amount of commission Joe paid his broker when he sold the stock.
# Display the amount of money that Joe had left when he sold the stock and paid his
# broker (both times). If this amount is positive, then Joe made a profit. If the amount is
# negative, then Joe lost money.

num_shares_purchased = int(input('Enter the number of shares purchased: '))
shares_price_purchased = float(input('Enter the shares price purchased: '))
stock_purchased_prices = num_shares_purchased*shares_price_purchased
stockbroker_purchased_paid = stock_purchased_prices*0.02
total_paid = stock_purchased_prices + stockbroker_purchased_paid

num_shares_sold = int(input('Enter the number of shares sold: '))
if num_shares_sold > num_shares_purchased:
    print('Insufficient shares')
else:
    shares_price_sold = float(input('Enter the shares price sold: '))
    stock_sold_prices = num_shares_sold*shares_price_sold
    stockbroker_sold_paid = stock_sold_prices*0.02

total_get = stock_sold_prices - stockbroker_sold_paid

print('The amount of money Joe paid for the stock =', stock_purchased_prices,
      '\nThe amount of commission Joe paid his broker when he bought the stock. =', stockbroker_purchased_paid,
      '\nThe amount that Joe sold the stock for. =', stock_sold_prices,
      '\nThe amount of commission Joe paid his broker when he sold the stock. =', stockbroker_sold_paid)

if total_get > total_paid:
    print('Profitable!!!')
else:
    print('Lost money!!!')

