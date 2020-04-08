"""
Sentiment Analysis in Python with TextBlob and VADER Sentiment (also Dash p.6)
"""
import textblob
import vaderSentiment.vaderSentiment as vader_sentiment

def textblob_analysis():
    """
    DOCSTRING
    """
    pos_count = 0
    pos_correct = 0
    with open("Positive.txt", "r") as f:
        for line in f.read().split('\n'):
            analysis = textblob.TextBlob(line)
            if analysis.sentiment.polarity > 0.2:
                if analysis.sentiment.polarity > 0:
                    pos_correct += 1
                pos_count += 1
    neg_count = 0
    neg_correct = 0
    with open("Negative.txt", "r") as f:
        for line in f.read().split('\n'):
            analysis = textblob.TextBlob(line)
            if analysis.sentiment.polarity <= 0.2:
                if analysis.sentiment.polarity <= 0:
                    neg_correct += 1
                neg_count += 1
    print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
    print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

def vader_analysis():
    """
    DOCSTRING
    """
    analyzer = vader_sentiment.SentimentIntensityAnalyzer()
    pos_count = 0
    pos_correct = 0
    with open("positive.txt","r") as f:
        for line in f.read().split('\n'):
            vs = analyzer.polarity_scores(line)
            if not vs['neg'] > 0.1:
                if vs['pos']-vs['neg'] > 0:
                    pos_correct += 1
                pos_count += 1
    neg_count = 0
    neg_correct = 0
    with open("negative.txt","r") as f:
        for line in f.read().split('\n'):
            vs = analyzer.polarity_scores(line)
            if not vs['pos'] > 0.1:
                if vs['pos']-vs['neg'] <= 0:
                    neg_correct += 1
                neg_count += 1
    print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
    print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

if __name__ == '__main__':
    vader_analysis()