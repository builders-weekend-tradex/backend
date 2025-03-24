from fastapi import APIRouter
from utils.social_analysis.news_feed import get_news

router = APIRouter()

DISABLE_NEWS_FETCH = False

@router.get("/analysis/social/news/everything/")
def fetch_news(symbol: str):
    if DISABLE_NEWS_FETCH:
        return {"symbol": symbol, "message": "News fetching is currently disabled."}
    
    news = get_news(symbol)
    return {"symbol": symbol, "articles": news}