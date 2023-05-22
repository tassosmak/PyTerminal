from src.utils import add_depend, sys
add_depend(str(sys.argv[1]))
from Kernel.RendererKit import Renderer as RD

import yfinance as yf
while True:
    Stock = RD.CommandQuest(type='3', msg='Enter Your Stock', header='Stock Viewer')

    ticker = yf.Ticker(Stock).info
    market_price = ticker['regularMarketOpen']
    previous_close_price = ticker['regularMarketPreviousClose']

    # RD.CommandSay(f'Selected Stock: {Stock}', 'GREEN')

    # RD.CommandSay((f'Market Price:, {market_price}'))
    # RD.CommandSay((f'Previous Close Price: {previous_close_price}'))
    RD.CommandQuest(type='2', msg=f'Market Price: {market_price}\nPrevious Close Price: {previous_close_price}', header=f'Stock Viewer | Selected Stock: {Stock}')