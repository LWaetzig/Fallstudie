#!/usr/bin/env python
# coding: utf-8

# In[43]:


from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline


# In[65]:


# Laden des HTML-Contents in soup

url="https://de.finance.yahoo.com"
page=requests.get(url)
soup= BeautifulSoup(page.content, "html.parser")

# In lists Obergruppen laden

lists=soup.find_all("div", class_="Cf")
with open("finance.csv","w",encoding="utf8", newline="") as f:
    thewriter =writer(f)
    header=["Title", "Maintext"]
    thewriter.writerow(header)
    
# In Obergruppe nach Untergruppen filtern und in Liste speichern

    for list in lists:
        maintext=list.find("p", class_="Fz(14px) Lh(19px) Fz(13px)--sm1024 Lh(17px)--sm1024 LineClamp(2,38px) LineClamp(2,34px)--sm1024 M(0)").text
        title=list.find("a", class_="js-content-viewer").text
        info=[title,maintext]
        thewriter.writerow(info)


# In[66]:


financeinfo=pd.read_csv("finance.csv")
financeinfo.head()


# In[67]:


unternehmen=["Adidas" ,"Allianz" ,"Alphabet", "Amazon" ,"Apple", "BASF", "Bayer", "Biontech", "BMW", "CocaCola", "Commerzbank" ,"Daimler" ,"Deutsche Bank" ,"Lufthansa" ,"Meta" ,"Microsoft" ,"Nike" ,"Nvidia" ,"PayPal" ,"Porsche" ,"SAP" ,"Siemens" ,"Telekom" ,"Tesla" ,"Twitter" ,"Volkswagen"]


sentiment = SentimentIntensityAnalyzer()
#sentiment_pipeline = pipeline("sentiment-analysis")

# In Maintext nach Unternehmen suchen

for i in financeinfo.Title:
    for aktien in unternehmen:
        if aktien in i:
            print(aktien,sentiment.polarity_scores(i))
            #print(sentiment_pipeline(i))
        
       


# In[ ]:





# In[ ]:




