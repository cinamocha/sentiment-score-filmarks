from filmarks_comment import get_reviews
from analysis import analyze_sentiment

url = 'https://filmarks.com/list/trend'

df = get_reviews(url)

for index, row in df.iterrows():
  review = row['Review']
  sentiment = analyze_sentiment(review)
  
  compound_score = sentiment['compound']
  if compound_score >= 0.05:
    sentiment_label = 'ポジティブ'
  elif compound_score <= -0.05:
    sentiment_label = 'ネガティブ'
  else:
    sentiment_label = 'なんとも言えない'
  
  print(f"Movie: {row['Title']}\nReview: {review}\nSentiment: {sentiment_label} (Compound: {compound_score})\n")