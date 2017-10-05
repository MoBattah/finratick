#!/usr/bin/python3
import requests
import json
from sys import argv

rh = 'https://api.robinhood.com/prices/?delayed=false&source=nls&symbols='

# process securities list
tf = list(map(lambda x: x.strip(), open(argv[1]).readlines()))[1:-1]
tf = list(filter(lambda x: '|G1' in x or '|G2' in x or '|G3' in x, tf))
tf = list(map(lambda x: x.split('|')[0], tf))

# get price by ticker
tickers = list(zip(tf, map(lambda x: x['price'] if x is not None else None, requests.get(rh + ','.join(tf)).json()['results'])))
tickers = filter(lambda x: x[1] is not None, tickers)
tickers = sorted(tickers, key=lambda t: float(t[1]), reverse=True)

for ticker in tickers:
    print(ticker[0] + ': ' + ticker[1])

    
