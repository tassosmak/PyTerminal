from src.utils import add_depend, sys
add_depend(str(sys.argv[1]))
from Makro.MakroCore.RendererKit import Renderer as RD

import requests

API_KEY = 'd1q2grpr01qrh89nojegd1q2grpr01qrh89nojf0'  # Replace this with your actual Finnhub API key

def fetch_stock_data(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol.upper()}&token={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["o"] == 0 and data["pc"] == 0:
            raise ValueError("Symbol not found or market closed.")
        return {
            "symbol": symbol.upper(),
            "open": data["o"],
            "previous_close": data["pc"]
        }
    elif response.status_code == 429:
        raise RuntimeError("Rate limit exceeded — try again in a minute.")
    else:
        raise ValueError(f"Unexpected response: {response.status_code}")

def main():
    symbol = RD.CommandShow(msg='Enter Stock Symbol', header='Stock Viewer').Input()

    try:
        stock = fetch_stock_data(symbol)
        RD.CommandShow(
            msg=f"Open Price         : {stock['open']}\nPrevious Close Price: {stock['previous_close']}",
            header=f"Stock Viewer | {stock['symbol']}"
        ).Info()
    except Exception as e:
        RD.CommandShow(msg=f"{str(e)}", header='Stock Viewer Error').Info()
main()