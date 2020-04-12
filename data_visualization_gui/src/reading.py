"""
DOCSTRING
"""
import pandas
import sqlite3

df.sort_values('unix', inplace=True)
df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
df.dropna(inplace=True)
print(df.tail())
