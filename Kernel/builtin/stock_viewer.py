from src.utils import add_depend, sys
add_depend(str(sys.argv[1]))
from Kernel.RendererKit import Renderer as RD

import yfinance as yf
Stock = RD.CommandQuest(type='3', msg='Enter Your Stock', header='Stock Viewer')
    
if not Stock.lower() == 'exit':
    ticker = yf.Ticker(Stock).info
    market_price = ticker['regularMarketOpen']
    previous_close_price = ticker['regularMarketPreviousClose']


    RD.CommandQuest(type='2', msg=f'Open Price: {market_price}\nPrevious Close Price: {previous_close_price}', header=f'Stock Viewer | Selected Stock: {Stock}')