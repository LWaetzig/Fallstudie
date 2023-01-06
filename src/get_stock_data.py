import yfinance as yf
import plotly.graph_objs as go
import pandas as pd


def request_stock_data(name) -> dict:
    """request stock data from yahoo finance
    Returns:
        dict: dictionary storing important stock information and historical data
    """
    interval = "1d"
    period = "max"
    
    data = dict()
    data["stock_name"] = name
    
    stock = yf.Ticker(name)
    data["data"] = stock.history(interval=interval, period=period)
    data["info"] = {
        "sector" : stock.info["sector"],
        "major_holders" : stock.major_holders,
        "institutional_holders" : stock.institutional_holders
        }
    
    return data

def create_visualization(self) -> None:
    """create visualization using plotly
    """