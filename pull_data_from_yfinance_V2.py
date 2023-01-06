# README This Program pulls finance data from yahoo finance and saves it into
# a local file encoded in JSON.

import yfinance as yf
import pandas as pd
import json
import os
import shutil

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

# USAGE of the function: symbol of the share has to be inserted as String
# Filename has to be a string with an ending e.g. "file.txt"


def pull_data(share_name, filename):
    share = yf.Ticker(str(share_name))
    data = share.history(period="5y", actions=False)
    df = pd.DataFrame(data)

    # other period options: “1d”, “5d”, “1mo”, “3mo”,
    #  “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”

    # CREATE JSON-file
    json = open(str(filename), "a")
    json.write("\n{\n")
    json.write('"share_name": "')
    json.write(str(share.info["symbol"]))
    json.write('",\n"long_name": "')
    json.write(str(share.info["longName"]))
    json.write('",\n"sector": "')
    json.write(str(share.info["sector"]))
    json.write('",\n"stock_data": [')

    for i in df.iterrows():
        json.write('\n\t{\n\t"Date": "')
        json.write(str(i[0])[:11])
        json.write('",\n\t"Values":{\n\t\t"Open": "')
        json.write(str(i[1][0]))
        json.write('",\n\t\t"High": "')
        json.write(str(i[1][1]))
        json.write('",\n\t\t"Low": "')
        json.write(str(i[1][2]))
        json.write('",\n\t\t"Close": "')
        json.write(str(i[1][3]))
        json.write('",\n\t\t"Volume": "')
        json.write(str(i[1][4]))
        json.write('"\n\t\t}\n\t},')


# for comp in selected_shares:
#     pull_data(comp, "FinanceData.json")

testshares = ["AAPL", "ADDDF"]


def ticker(share_symbol):
    symbol = yf.Ticker(str(share_symbol))
    return symbol


# data = testshares.history(period="1d", actions=False)
# df = pd.DataFrame(data)
# maybe a better alternative to create file?

def historical_data(shares: list):
    """function to get all history data for each passed share
    """

    if os.path.exists("shares") :
        #this command deletes the folder and all files in it without making trouble because of permission etc...
        shutil.rmtree("shares")

    os.mkdir("shares")
    for i in shares:
        share = str(i)
        history = ticker(share).history(period = "5d" , actions=False)
        history.to_csv(f"shares/{share}.csv")

    #history = pd.read_csv("shares/aapl.csv" , index_col=0)

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


def wrapper_function():

    # selected shares : list

    # ticker function
    historical_data(testshares)
    share_dict = create_data_dict(testshares)

    with open("finance.json" , "w" , encoding="utf-8") as f:
        json.dump(share_dict , f, indent=4 , ensure_ascii=False)


wrapper_function()
