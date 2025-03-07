import os
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from dotenv import load_dotenv

# source: https://newsapi.org/

# Init

load_dotenv()

API_KEY = os.getenv("API_KEY")
newsapi = NewsApiClient(api_key=API_KEY)

COMPANY_NAME = "Walt Disney"

def get_news(symbol: str = COMPANY_NAME):
  end_date = datetime.today()
  start_date = end_date - timedelta(days=10)  # 10 days before today
  
  # /v2/everything
  all_articles = newsapi.get_everything(q=symbol,
                                        from_param=start_date,
                                        to=end_date,
                                        language='en',
                                        sort_by='popularity',
                                        page=2)
  
  # Make dataframe
  articles = [
        {"title": article["title"], "publishedAt": article["publishedAt"], "url": article["url"]}
        for article in all_articles["articles"]
    ]

  return articles

get_news(COMPANY_NAME)