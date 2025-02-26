#!/usr/bin/python3
import sys
import requests

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <filename>".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    
    # Read the file, stripping whitespace and skipping first and last lines
    with open(filename) as file:
        lines = [line.strip() for line in file][1:-1]

    # Filter lines that contain any of the specified tags
    valid_lines = [
        line for line in lines
        if any(tag in line for tag in ('|G1', '|G2', '|G3'))
    ]
    
    # Extract ticker symbols (assumes ticker is the text before the first '|')
    tickers = [line.split('|')[0] for line in valid_lines]
    
    # Prepare API request
    api_url = (
        "https://api.robinhood.com/prices/?delayed=false&source=nls&symbols="
        + ",".join(tickers)
    )
    
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    
    # Zip ticker symbols with their corresponding prices
    ticker_prices = [
        (ticker, result.get('price'))
        for ticker, result in zip(tickers, data.get('results', []))
        if result.get('price') is not None
    ]
    
    # Sort tickers by price in descending order
    ticker_prices.sort(key=lambda x: float(x[1]), reverse=True)
    
    # Print the results
    for ticker, price in ticker_prices:
        print(f"{ticker}: {price}")

if __name__ == "__main__":
    main()
