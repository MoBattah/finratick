# FINRATick


## Overview

This simple Python script fetches US equities meeting certain criteria and groups within the SEC Pilot program. It processes an input file containing securities data, filters securities based on specific tags (`|G1`, `|G2`, or `|G3`), extracts ticker symbols, and retrieves current price data from the Robinhood API. The securities are then sorted in descending order by price for further use and research.

## Features

- **File Processing:**  
  Reads an input file containing securities data, skipping the first and last lines.
- **Data Filtering:**  
  Filters lines containing specific tags (`|G1`, `|G2`, or `|G3`) relevant to the SEC Pilot program.
- **Ticker Extraction:**  
  Extracts ticker symbols (assumes the ticker is the text before the first `|`).
- **API Integration:**  
  Fetches price data from the Robinhood API.
- **Sorting:**  
  Sorts the securities by price in descending order.
- **Output:**  
  Prints each ticker along with its corresponding price for easy review and research.

## Requirements

- **Python 3.x**
- **Requests library:**  
  Install via pip if not already installed:
  ```bash
  pip install requests
