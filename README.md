# Premium Stock Scanner 📈

A simple Python project that scans selected stocks and suggests whether they might be worth watching or entering based on daily price movement.

This project uses **Yahoo Finance data** through the `yfinance` library.

## Features

* Access Key system 🔐
* Real stock price data
* Daily price change analysis
* Basic Buy / Wait suggestion
* Command line interface

## Example Output

==== PREMIUM STOCK SYSTEM ====

Enter Access Key: INV-7845-ABCD

Access Granted

Today's Stock Recommendation

AAPL | Price: 260.29 | Change: -2.23 | WAIT
NVDA | Price: 183.34 | Change: 0.30 | BUY
MSFT | Price: 410.68 | Change: 5.48 | BUY

## Installation

Install required library

pip install yfinance

or

pip install -r requirements.txt

## Run Program

python investment_system.py

## Project Structure

premium-stock-system
│
├── investment_system.py
├── requirements.txt
└── README.md

## Stocks Included

* AAPL (Apple)
* TSLA (Tesla)
* NVDA (Nvidia)
* MSFT (Microsoft)
* AMZN (Amazon)
* META (Meta)

## Note

Stock prices come from Yahoo Finance and may have a delay.

## Author

Nattanan
