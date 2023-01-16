import os

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf

from fideo.src.finvispro import web_scraping


def get_stock_data():
    """function to get all necessary information and historical share price"""

    data_storage_path = os.path.join("fideo", "data")
    hist_data_path = os.path.join(data_storage_path, "hist")

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

    df = pd.DataFrame()

    # get compund value from nlp algorithm to classify news depending to the share
    dfcompounds = web_scraping()

    for i, tag in enumerate(shares):
        ticker = yf.Ticker(str(tag))
        history = ticker.history(period="1y", actions=False)
        history.to_csv(f"{hist_data_path}/{tag}.csv")

        # get all information for each share
        share_name = str(ticker.info["longName"])
        share_sector = str(ticker.info["sector"])

        peg_ratio = float(ticker.info["trailingPegRatio"])
        beta_factor = float(ticker.info["beta"])
        market_cap = float(ticker.info["marketCap"])
        volume = float(ticker.info["volume"])
        volatility = (history["Close"].pct_change().std() * (252**0.5) * 100).round(2)

        # store information in DataFrame
        df.loc[i, "tag"] = tag
        df.loc[i, "name"] = share_name
        df.loc[i, "sector"] = share_sector
        df.loc[i, "peg_ratio"] = peg_ratio
        df.loc[i, "betafactor"] = beta_factor
        df.loc[i, "volatility"] = volatility
        df.loc[i, "market_cap"] = market_cap
        df.loc[i, "volume"] = volume
        df.loc[i, "last_close_price"] = float(history["Close"][-1].round(3))
        df.loc[i, "histpath"] = f"{hist_data_path}/{tag}.csv"

    # merge dataframe containing all necessary information with compund dataframe
    df = pd.merge(df, dfcompounds, on="tag", how="left")

    for i , row in df.iterrows():

        # calculation to define risk level for each share
        # classification: -1 = high risk, 0 = neutral, 1 = low risk
        # classify each share value
        class_peg_ratio = 0
        class_beta_factor = 0
        class_volatility = 0
        class_compound = 0

        if row["peg_ratio"] > 2.5:
            class_peg_ratio = -1
        elif row["peg_ratio"] < 1.75:
            class_peg_ratio = 1

        if row["beta_factor"] > 1.15:
            class_beta_factor = -1
        elif row["beta_factor"] < 0.95:
            class_beta_factor = 1

        if row["volatility"] > 45:
            class_volatility = -1
        elif row["volatility"] <= 20:
            class_volatility = 1

        if row["compound"] < -0.05:
            class_compound = -1
        elif row["compound"] > 0.05:
            class_compound = 1

        class_mean = (class_volatility + class_beta_factor + class_peg_ratio + class_compound) / 4

        # caluclate risk level
        if class_mean <= 0 and class_mean > -1.0:
            risk_level = 1
        elif class_mean <= -2/3:
            risk_level = 2
        else:
            risk_level = 0

        # add risk level to DataFrame
        df.loc[i, "risk_level"] = risk_level

    df.to_csv(f"{data_storage_path}/sharesdata.csv")

# df = pd.read_csv("fideo/data/sharesdata.csv" , index_col=0)


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
            "gridcolor": "grey",
            "showticklabels": True,
            "griddash": "dash",
            "minor_griddash": "dot",
        },
        yaxis={"fixedrange": True, "showgrid": False, "showticklabels": False},
    )

    return fig


def create_full_visualization(file_path: str):
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

    scatter = go.Scatter(x=df.index, y=df["Close"], opacity=0.5)
    fig = make_subplots(specs=[[{"secondary_y": False}]])
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
            "gridcolor": "grey",
            "showticklabels": True,
            "griddash": "dash",
            "minor_griddash": "dot",
        },
        yaxis={"fixedrange": True, "showgrid": False, "showticklabels": False},
    )

    return fig
