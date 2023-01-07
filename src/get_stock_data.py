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
                }
            }
        )

    return share_dict


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

    with open("finance.json", "w", encoding="utf-8") as f:
        json.dump(share_dict, f, indent=4, ensure_ascii=False)


def create_visualization(file_path) -> None:
    """create visualization using plotly"""

    df = pd.read_csv(file_path, index_col=0)
    fig = go.Figure

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="stock price",
        )
    )
