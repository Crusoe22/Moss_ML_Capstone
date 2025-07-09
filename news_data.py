import csv
import pandas as pd

''' https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests

This data comes from the kaggle website. Here, I've compiled stock news data scraped directly from its source 
into an easy-to-use format. I've also provided the scripts used to get this data and the scripts I use for personally 
trading this data in real-time here: https://github.com/bot-developer3/Scraping-Tools-Benzinga.

  '''
 
df = pd.read_csv('analyst_ratings_processed.csv')
nasdaq = pd.read_csv(  )



print(df.head())

# Drop Column 
df.drop['Index']

# Sycronize time from date column 
