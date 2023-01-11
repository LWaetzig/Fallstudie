import os

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf

from fideo.src.finvispro import web_scraping



def get_stock_data():
    """function to get all necessary information and historical share price"""

    data_storage_path = os.path.join("fideo" , "data")
    hist_data_path = os.path.join(data_storage_path , "hist")

    if not os.path.exists(hist_data_path):
        os.makedirs(hist_data_path)

    shares = [
        "AMZN",
        "GOOG",
        "DB",
        "NKE",
        "AAPL",
        "KO",
        "META",
        "MSFT",
        "NVDA",
        "PYPL",
        "SAP",
        "TSLA",
    ]

    # columns = [
    #     "tag",
    #     "name",
    #     "sector",
    #     "volatility",
    #     "peg_ratio",
    #     "betafactor",
    #     "histpath",
    #     "market_cap",
    #     "volume",
    #     "last_close_price"
    # ]
    df = pd.DataFrame()

    # get compund value from nlp algorithm to classify news depending to the share
    dfcompounds = web_scraping()

    for i, tag in enumerate(shares):
        ticker = yf.Ticker(str(tag))
        history = ticker.history(period="1y", actions=False)
        history.to_csv(f"{hist_data_path}/{tag}.csv")

        df.loc[i, "tag"] = tag
        df.loc[i, "name"] = str(ticker.info["longName"])
        df.loc[i, "sector"] = str(ticker.info["sector"])
        df.loc[i, "peg_ratio"] = ticker.info["trailingPegRatio"]
        df.loc[i, "betafactor"] = float(ticker.info["beta"])
        df.loc[i, "histpath"] = f"{hist_data_path}/{tag}.csv"
        df.loc[i, "volatility"] = (history["Close"].pct_change().std() * 100).round(2)
        df.loc[i, "market_cap"] = float(ticker.info["marketCap"])
        df.loc[i, "volume"] = float(ticker.info["volume"])
        df.loc[i, "last_close_price"] = float(history["Close"][-1].round(3))

        # class_peg_ratio = 0
        # if float(ticker.info["pegRatio"]) > 1:
        #     class_peg_ratio = -1
        # elif float(ticker.info["pegRatio"]) < 1:
        #     class_peg_ratio = 1
# 
        # class_betafactor = 0
        # if float(ticker.info["beta"]) > 1:
        #     class_peg_ratio = -1
        # elif float(ticker.info["beta"]) < 1:
        #     class_peg_ratio = 1



    # merge dataframe containing all necessary information with compund dataframe
    df = pd.merge(df, dfcompounds, on="tag", how="left")

    # "class_volatility"
    # 0-16 -> 0
    # 16-45 -> 1
    # > 45 -> 2

    # "risk_level" = sum(class_volatitily, class_betafactor, class_peg_ratio) 
    # alternative: mean()

    df.to_csv(f"{data_storage_path}/sharesdata.csv")

def create_small_visualization(file_path: str):
    """function to create a plot using plotly to display the historical share price

    Args:
        share_historical (str): path to historical share data

    Returns:
        function: returns a figure containing the plot
    """
    df = pd.read_csv(file_path, index_col=0)

    candlestick = go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
    )
    fig = go.Figure()
    fig.add_trace(candlestick)

    fig.update_layout(
        autosize=True,
        margin=dict(l=0, r=0, b=0, t=0),
        height=300,
        width=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        xaxis={
            "fixedrange": True,
            "rangeslider": {"visible": False},
            "showgrid": True,
            "gridcolor" : "grey",
            "showticklabels": True,
            "griddash" :"dash",
            "minor_griddash" : "dot",
        },
        yaxis={
            "fixedrange": True,
            "showgrid": False,
            "showticklabels": False},
    )

    return fig


def create_full_visualization(file_path : str):
    """function to generat a bigger visualization with zoom and paning function

    Args:
        file_path (str): path to historical share data 
    
    Returns:
        function: returns a figure containing the plot
    """
    df = pd.read_csv(file_path, index_col=0)

    candlestick = go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
    )

    scatter = go.Scatter(
        x=df.index,
        y=df["Close"],
        opacity=0.5
    )
    fig = make_subplots(specs=[[{"secondary_y" : False}]])
    fig.add_trace(scatter)
    fig.add_trace(candlestick)
    

    fig.update_layout(
        autosize=False,
        margin=dict(l=0, r=0, b=0, t=0),
        height=300,
        width=600,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        xaxis={
            "fixedrange": True,
            "rangeslider": {"visible": True},
            "showgrid": True,
            "gridcolor" : "grey",
            "showticklabels": True,
            "griddash" :"dash",
            "minor_griddash" : "dot",
        },
        yaxis={
            "fixedrange": True,
            "showgrid": False,
            "showticklabels": False},
    )



    return fig