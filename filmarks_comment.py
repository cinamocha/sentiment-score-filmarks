import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_reviews(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text , 'html.parser')
  #タイトルとレビューを集める箱の準備、空のリスト
  movies = []
  reviews = []
  #タイトルとレビューの取得
  for movie in soup.select('.p-content-cassette'):      #トレンドの映画データの取得
    title_elem = movie.select_one('.p-content-cassette__title')
    title = title_elem.get_text(strip=True) if title_elem else 'No title'
    review_elem = movie.select_one('.p-content-cassette__review__text')
    review_text = review_elem.get_text(strip=True) if review_elem else "No review"
    #データをリストに追加する
    movies.append(title)
    reviews.append(review_text)

  #データフレーム化する
  df = pd.DataFrame({'Title': movies , 'Review': reviews})
  return df

