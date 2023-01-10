import json
import os

import pandas as pd
import plotly.graph_objs as go
import yfinance as yf


def ticker(share_symbol):
    symbol = yf.Ticker(str(share_symbol))
    return symbol


def historical_data(shares: list):
    """function to get all history data for each share in list

    Args:
        shares (list): list containing share tags as string
    """

    if not os.path.exists("shares"):
        os.mkdir("shares")

    for i in shares:
        history = ticker(i).history(period="5d", actions=False)
        history.to_csv(f"shares/{i}.csv")


def create_data_dict(shares: list) -> dict:
    """function that takes a list with selected shares and creates a dictionary with important information
    Args:
        shares (list): selected shares

    Returns:
        dict: content (see function above)
    """
    share_dict = dict()
    for i in shares:
        share_dict.update(
            {
                str(i): {
                    "LongName": str(ticker(i).info["longName"]),
                    "Sector": str(ticker(i).info["sector"]),
                    "HistData": f"shares/{i}.csv",

                    # ich hoffe 52WeekChange ist die Volatilität in % und ich bin nicht dumm
                    # laut ChatGPT bin ich dumm lul, ist nicht das selbe
                    "volatility": float(ticker(i).info["52WeekChange"]),

                    

                    "peg": float(ticker(i).info["pegRatio"]),

                    "beta": float(ticker(i).info["beta"]),
                }
            }
        )

    return share_dict

df = pd.DataFrame(create_data_dict())
df.to_csv("sharesdata.csv", index=False)

def wrapper_function() -> None:
    """wrapper function to create .csv files for historical stock data and .json file with further information about the share"""

    selected_shares = [
        "ADDDF",
        "ALIZF",
        "GOOGL",
        "AMZN",
        "AAPL",
        "BFFAF",
        "BAYZF",
        "BNTX",
        "BAMXF",
        "KO",
        "CRZBF",
        "MBGAF",
        "DB",
        "DLAKF",
        "META",
        "MSFT",
        "NKE",
        "NVDA",
        "PYPL",
        "POAHF",
        "SAPGF",
        "SMAWF",
        "DTEGF",
        "TSLA",
        "VLKPF",
    ]

    historical_data(selected_shares)
    share_dict = create_data_dict(selected_shares)



def get_stock_data():
    """function to get all necessary information and historical share price"""

    # define list with seleted shares

    # create csv file for historical share prices
    
    
    # create csv file with information depending on the share

