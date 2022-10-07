# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:41:11 2021

@author: Harald.Norvald.Stabbetorp
"""
"""
Date,Open,High,Low,Close,Volume,Adj Close
2008-06-02,12.91,13.06,10.76,10.88,16945700,10.88
"""
import matplotlib.pyplot as plt


def read_file(filename):
    
    infile = open(filename, 'r')
    data = infile.readlines()
    infile.close()
    
    dates = []
    prices = []
    
    # Hopper over rad 1 [1:]
    for line in data[1:]:
        columns = line.split(',')
        date = columns[0]
        date = date[:-3]
        price = columns[-1]
        
        dates.append(date)
        prices.append(float(price))
        
    dates.reverse()
    prices.reverse()
        
    return dates, prices
    


dates = {}
prices = {}


d, p = read_file('stockprices_Sun.csv')
dates ['Sun'] = d
prices ['Sun'] = p

d, p = read_file('stockprices_Google.csv')
dates ['Google'] = d
prices ['Google'] = p

d, p = read_file('stockprices_Microsoft.csv')
dates ['Microsoft'] = d
prices ['Microsoft'] = p


data = {'prices' : prices, 'dates' : dates}

# Normalize prices
norm_price = prices['Sun'][0]
prices['Sun'] = [p/ norm_price for p in prices['Sun']]

norm_price = prices['Microsoft'][0]
prices['Microsoft'] = [p/ norm_price for p in prices['Microsoft']]

# Normalize prices for Google
jan05_Microsoft = prices['Microsoft'][dates['Microsoft'].index('2005-01')]
jan05_Sun = prices['Sun'][dates['Sun'].index('2005-01')]

norm_price = prices['Google'][0] / max(jan05_Microsoft, jan05_Sun)
prices['Google'] = [p/ norm_price for p in prices['Google']]

# Januar 1988 er måned 0
x = {}
x['Sun'] = range(len(prices['Sun']))
x['Microsoft'] = range(len(prices['Microsoft']))

jan05 = dates['Sun'].index('2005-01')
x['Google'] = range(jan05, jan05 + len(prices['Google']),1)

plt.plot(x['Microsoft'], prices['Microsoft'], 'r-')
plt.plot(x['Sun'], prices['Sun'], 'b-')
plt.plot(x['Google'], prices['Google'], 'y-')
plt.legend(['Microsoft', 'Sun', 'Google'])
