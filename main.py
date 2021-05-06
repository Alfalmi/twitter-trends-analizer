import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntwitter
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# import matplotlib.pyplot as plt

# Set maximum tweets to pull
maxTweets = 20000
# Set what keywords you want your twitter scraper to pull
keyword = 'pfizer'
# Open/create a file to append data to
csvFile = open('../graficos/pfe_tweets_result.csv', 'a', newline='', encoding='utf8')
# Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id', 'date', 'tweet', ])

# Write tweets into the csv file
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(
        keyword + ' lang:en since:2020-01-01 until:2021-01-01 -filter:links -filter:replies').get_items()):

    if i > maxTweets:
        break
    csvWriter.writerow([tweet.id, tweet.date, tweet.content])
    print([tweet.id, tweet.date, tweet.content])
csvFile.close()
