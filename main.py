from typing import Union
from utils.social_analysis.news_feed import get_news, DEFAULT_SYMBOL

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/news/")
def fetch_news(symbol: str = DEFAULT_SYMBOL):
    news = get_news(symbol)
    return {"symbol": symbol, "articles": news}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}