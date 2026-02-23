import numpy as np
from decimal import Decimal

np.random.seed(123)
days = 10

opening_prices = np.random.normal(loc = 170, scale = 10, size = days) #np.random.normal(loc = mean, scale = std dev, size = number of values)
opening_prices_decimal = np.array([round(Decimal(str(price)), 2) for price in opening_prices])

closing_prices = np.random.normal(loc = 175, scale = 15, size = days) 
closing_prices_decimal = np.array([round(Decimal(str(price)), 2) for price in closing_prices])

buy_or_sell = [] #Should rather be a np array. Look at np.where


for i in range(len(opening_prices)):
    
    if opening_prices_decimal[i] > closing_prices_decimal[i]:
        buy_or_sell.append('Sell')
        
    elif opening_prices_decimal[i] < closing_prices_decimal[i]:
        buy_or_sell.append('Buy')
        
    else:
        buy_or_sell.append('Hold')
       


for i in range(len(opening_prices)):
    print(f"Day {i+1}:")
    print(f"Opening Price: R{opening_prices_decimal[i]}")
    print(f"Closing Price: R{closing_prices_decimal[i]}")
    print(f"Decision: {buy_or_sell[i]}")
    print("")
