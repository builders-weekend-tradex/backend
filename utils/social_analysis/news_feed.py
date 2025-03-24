import os
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from dotenv import load_dotenv

# source: https://newsapi.org/

load_dotenv()

API_KEY = os.getenv("API_KEY")
newsapi = NewsApiClient(api_key=API_KEY)

# Ticker symbol mapping to ensure we fetch the correct news
ticker_mapping = {
    "GOOG": "GOOGLE",
    "AAPL": "APPLE",
    "AMZN": "AMAZON",
    "TSLA": "TESLA",
    "MSFT": "MICROSOFT",
    "NVDA": "NVIDIA",
    "META": "Meta",
    "AVGO": "Broadcom",
    "BRK.B": "Berkshire Hathaway"
}

def get_news(symbol: str):
    # Check if the symbol needs to be mapped to a different name
    if symbol in ticker_mapping:
        symbol = ticker_mapping[symbol]
    
    # Fetch news for the mapped symbol
    end_date = datetime.today()
    start_date = end_date - timedelta(days=10)  # 10 days before today
    
    # /v2/everything
    all_articles = newsapi.get_everything(q=symbol,
                                          from_param=start_date,
                                          to=end_date,
                                          language='en',
                                          sort_by='popularity',
                                          page=2)
    
    # Extract articles into a structured list
    articles = [
        {"title": article["title"], "publishedAt": article["publishedAt"], "url": article["url"]}
        for article in all_articles["articles"]
    ]
    
    return articles
