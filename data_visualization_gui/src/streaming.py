"""
Streaming Tweets and Sentiment - Data Visualization GUIs with Dash and Python p.7
"""
import json
import pandas
import sqlite3
import tweepy
import unidecode
import vaderSentiment.vaderSentiment as vader_sentiment

analyzer = vader_sentiment.SentimentIntensityAnalyzer()
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
    """
    DOCSTRING
    """
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))

create_table()

consumer_key="fsdfasdfsafsffa"
consumer_key="asdfsadfsadfsadf"
access_token="asdf-aassdfs"
access_secret="asdfsadfsdafsdafs"

class listener(tweepy.StreamListener):
    """
    DOCSTRING
    """
    def on_data(self, data):
        """
        DOCSTRING
        """
        try:
            data = json.loads(data)
            tweet = unidecode.unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms, tweet, sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                      (time_ms, tweet, sentiment))
            conn.commit()
        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        """
        DOCSTRING
        """
        print(status)

while True:
    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["a", "e", "i", "o", "u"])
    except Exception as e:
        print(str(e))
        time.sleep(5)
