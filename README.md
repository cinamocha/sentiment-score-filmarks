# 概要  
Filmarksのトレンドページのレビューの感情の分析ができます。  
RequestsでURLからHTMLの内容を取得し、BeautifulSoupで内容を分析してタイトルとレビューを抽出。  
Pandasでスクレイピングしたデータをデータフレームにまとめ、nltkでVADER辞書を取得。  
最後にSentimentIntensityAnalyzerで感情分析をしています。  
レビューのcompoundスコアによってポジティブかネガティブかを返してくれます。  

## 改善点  
そもそも扱うデータと感情分析の相性が悪いように感じた。参考に出来るデータも少ないため改善の余地あり。  

## このリポジトリについて  
analysis.py 感情分析の処理をanalyze_sentiment関数と定義している  
filmark_comment.py タイトルやレビューを取得する処理をget_reviews関数と定義している  
main.py 上の定義した関数をインポートし根幹の流れを作っている  



## 使い方  
１．このリポジトリをクローンする  
git clone https://github.com/cinamocha/sentiment-score-filmarks  

２．下記ライブラリのインストール
pip install requests beautifulsoup4 pandas nltk  

３．スクリプト実行  
python main.py  
  
Python 3.13.0  
beautifulsoup4 4.12.3  
bs4 0.0.2  
requests 2.32.3  
pandas 2.2.3  
nltk 3.9.1  
