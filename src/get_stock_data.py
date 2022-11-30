import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

class Stock():

    def __init__(self, name):
        self.name = name


    def request_stock_data(self) -> dict:
        """request stock data from yahoo finance 

        Returns:
            dict: dictionary storing important stock information and historical data
        """

        interval = "1d"
        period = "max"
        data = yf.Ticker(self.name).history(interval=interval, period=period)
        data = data.drop(columns=["Volume" , "Dividends" , "Stock Splits"])

        return data

    def create_visualization(self) -> None:
        """create visualization using plotly
        """




aapl = yf.Ticker("AAPL")
div = aapl.get_actions()
an = aapl.get_analysis()
reco = aapl.get_recommendations()

info = aapl.get_calendar()



news = aapl.get_news()
news[0]
