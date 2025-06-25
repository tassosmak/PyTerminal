from src.utils import add_depend, sys
add_depend(str(sys.argv[1]))
from MakroCore.RendererKit import Renderer as RD

import yfinance as yf
Stock = RD.CommandShow(msg='Enter Your Stock', header='Stock Viewer').Input()
    
if not Stock.lower() == 'exit':
    ticker = yf.Ticker(Stock).info
    market_price = ticker['regularMarketOpen']
    previous_close_price = ticker['regularMarketPreviousClose']


    RD.CommandShow(msg=f'Open Price: {market_price}\nPrevious Close Price: {previous_close_price}', header=f'Stock Viewer | Selected Stock: {Stock}').Info()