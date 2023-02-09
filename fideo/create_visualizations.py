import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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


def create_full_visualization(file_path: str , risk_level):
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
    if risk_level == 0:
        position = {
            "x" : 0.9,
            "y" : 0.9,
            "ax" : -40,
            "ay" : 40,
            "color" : "darkgreen"
        }
    elif risk_level == 1:
        position = {
            "x" : 0.9,
            "y" : 0.8,
            "ax" : -65,
            "ay" : 0,
            "color" : "black"
        }
    else:
        position = {
            "x" : 0.9,
            "y" : 0.75,
            "ax" : -40,
            "ay" : -40,
            "color" : "darkred"
        }

    annotation = go.layout.Annotation(
        x=position["x"],
        y=position["y"],
        xref="paper",
        yref="paper",
        text="Trend",
        showarrow=True,
        arrowhead=3,
        arrowsize=1,
        arrowwidth=3,
        arrowcolor=position["color"],
        ax=position["ax"],
        ay=position["ay"],
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(candlestick, secondary_y=False)

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

    fig.update_layout(
        annotations=[annotation]
    )

    return fig
