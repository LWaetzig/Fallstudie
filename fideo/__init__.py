import yfinance as yf

ticker = yf.Ticker("msft")
history = ticker.history(period="1y", actions=False)

ticker.info
info = yf.Ticker("AAPL").info["sector"]