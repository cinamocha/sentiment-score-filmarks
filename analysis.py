from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment(review_text):
  sia = SentimentIntensityAnalyzer()
  sentiment = sia.polarity_scores(review_text)
  return sentiment