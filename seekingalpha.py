#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline


# In[4]:


url="https://seekingalpha.com/market-news"
page=requests.get(url)
soup= BeautifulSoup(page.content, "html.parser")
lists=soup.find_all("div", class_="ig-p3 aq-b2")
with open("finance.csv","w",encoding="utf8", newline="") as f:
    thewriter =writer(f)
    header=["News"]
    thewriter.writerow(header)
    for list in lists:
        title=list.find("a", class_="ig-y").text
        info=[title]
        thewriter.writerow(info)



# In[6]:


financeinfo=pd.read_csv("finance.csv")
financeinfo


# In[13]:


unternehmen=["Adidas" ,"Allianz" ,"Alphabet", "Amazon" ,"Apple", "BASF", "Bayer", "Biontech", "BMW", "CocaCola", "Commerzbank" ,"Daimler" ,"Deutsche Bank" ,"Lufthansa" ,"Meta" ,"Microsoft" ,"Nike" ,"Nvidia" ,"PayPal" ,"Porsche" ,"SAP" ,"Siemens" ,"Telekom" ,"Tesla" ,"Twitter" ,"Volkswagen"]



for i in financeinfo.News:
   
    for aktien in unternehmen:
        if aktien in i:
            print(aktien,sentiment.polarity_scores(i))
          


# In[14]:





# In[ ]:




