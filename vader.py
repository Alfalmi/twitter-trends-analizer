import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntwitter
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

analyzer = SentimentIntensityAnalyzer()
df = pd.read_csv('../graficos/pfe_tweets_result.csv')
df = df.set_index('date')

df['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df['tweet']]
df['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df['tweet']]
df['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df['tweet']]
df['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df['tweet']]

df.index = pd.to_datetime(df.index, errors='coerce', format='%Y-%m-%d %H:%M:%S')
df = df.resample('D').mean()
df = df.loc[df.index.to_series().dt.weekday < 5]  # Remove weekends
df.to_csv('tweets_resampled_mean_no_weekends.csv')


