from urllib.request import Request, urlopen

import pandas as pd
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def web_scraping():
    finwiz_url = "https://finviz.com/quote.ashx?t="
    news_tables = {}
    tickers = [
        "AMZN",
        "GOOG",
        "BNTX",
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
    for ticker in tickers:
        url = finwiz_url + ticker
        req = Request(
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0"
            },
        )
        response = urlopen(req)
        html = BeautifulSoup(response)
        news_table = html.find(id="news-table")
        news_tables[ticker] = news_table
    parsed_news = []

    # Iterate through the news
    for file_name, news_table in news_tables.items():
        for x in news_table.findAll("tr"):
            text = x.a.get_text()
            date_scrape = x.td.text.split()
            if len(date_scrape) == 1:

                time = date_scrape[0]
            else:
                date = date_scrape[0]
                time = date_scrape[1]

            ticker = file_name.split("_")[0]
            parsed_news.append([ticker, date, time, text])

    vader = SentimentIntensityAnalyzer()

    columns = ["ticker", "date", "time", "headline"]
    parsed_and_scored_news = pd.DataFrame(parsed_news, columns=columns)
    scores = parsed_and_scored_news["headline"].apply(vader.polarity_scores).tolist()
    scores_df = pd.DataFrame(scores)
    parsed_and_scored_news = parsed_and_scored_news.join(scores_df, rsuffix="_right")
    parsed_and_scored_news["date"] = pd.to_datetime(parsed_and_scored_news.date).dt.date
    compounddata = parsed_and_scored_news.groupby(["ticker"])
    compoundmean = pd.DataFrame(compounddata["compound"].mean()).reset_index()
    return compoundmean.to_csv("finviznews")