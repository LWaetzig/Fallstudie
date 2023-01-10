from django.db import models
import pandas as pd
import plotly.graph_objects as go


class Share(models.Model):

    share_id = models.CharField(("share_ID"), primary_key=True, max_length=255)
    share_tag = models.CharField(("share_tag"), max_length=255)
    share_name = models.CharField(("share_name"), max_length=255)
    share_sector = models.CharField(("share_sector"), max_length=255)
    share_value1 = models.FloatField(("value1"))
    share_value2 = models.FloatField(("value2"))
    share_historical = models.CharField(("historical"), max_length=50)

    def create_visualization(file_path: str):
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
                "showgrid": False,
                "showticklabels": False,
            },
            yaxis={"fixedrange": True, "showgrid": False, "showticklabels": False},
        )

        return fig
