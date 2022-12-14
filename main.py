from src.get_stock_data import request_stock_data
import plotly.graph_objects as go

data = request_stock_data("aapl")

data.keys()

fig = go.Figure(data=[
    go.Candlestick(
        x=data["data"].index,
        open=data["data"]["Open"],
        high=data["data"]["Open"],
        low=data["data"]["Low"],
        close=data["data"]["Close"],
    )
])

fig.show()
data



