import pandas as pd
import numpy as np
import snscrape.modules.twitter as sntwitter
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

corrected_df = pd.read_csv("tweets_resampled_mean_no_weekends.csv", parse_dates=True, index_col=0)
_pfe = pd.read_csv("PFE.csv", parse_dates=True, index_col=0)
combined_df = corrected_df.merge(_pfe, on='Date', how='outer').dropna()

# Calculating Log Returns Column
combined_df['returns'] = np.log(combined_df['Close'] / combined_df['Close'].shift(1))
# Long when the sentiment[pos > neg] and short otherwise
combined_df['position'] = np.where(combined_df['pos'] > combined_df['neg'], 1, -1)
# Create Strategy column & by multiplying SHIFTED position to avoid hindsight bias
combined_df['strategy'] = combined_df['position'].shift(1) * combined_df['returns']
combined_df.dropna(inplace=True)

# print(_pfe)
combined_df.to_csv('combined.csv')
np.exp(combined_df[['returns', 'strategy']].sum())
