import os
import pandas as pd
import yfinance as yf
import warnings
from Finvizpro_copy_edited import web_scraping

warnings.simplefilter("ignore")

def get_stock_data():
    """function to get all necessary information and historical share price"""

    shares = ['AMZN',"GOOG","BNTX","NKE","AAPL","KO","META","MSFT","NVDA","PYPL","SAP","TSLA"]

    if not os.path.exists("shares"):
        os.mkdir("shares")

    spalten = ["tag", "name", "sector", "volatility", "peg_ratio", "betafactor", "histpath"]
    df = pd.DataFrame(columns=spalten)

    dfcompounds = web_scraping()

    for i, tag in enumerate(shares):
        ticker = yf.Ticker(str(tag))
        history = ticker.history(period="1y", actions=False)
        history.to_csv(f"shares/{tag}.csv")
        df.loc[i, "tag"] = tag
        df.loc[i, "name"] = str(ticker.info["longName"])
        df.loc[i, "sector"] = str(ticker.info["sector"])
        df.loc[i, "peg_ratio"] = float(ticker.info["pegRatio"])
        df.loc[i, "betafactor"] = float(ticker.info["beta"])
        df.loc[i, "histpath"] = f"shares/{tag}.csv"
        df.loc[i, "volatility"] = (history['Close'].pct_change().std() * 100).round(2)   
    df = pd.merge(df, dfcompounds, on='tag', how='left')
    #print(df)
    df.to_csv("sharesdata.csv")

get_stock_data()  
