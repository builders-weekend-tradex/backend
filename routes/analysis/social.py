from fastapi import APIRouter
from utils.social_analysis.news_feed import get_news, COMPANY_NAME

router = APIRouter()

DISABLE_NEWS_FETCH = True

@router.get("/analysis/social/news/everything/")
def fetch_news(symbol: str = COMPANY_NAME):
    if DISABLE_NEWS_FETCH:
        return {"symbol": symbol, "message": "News fetching is currently disabled."}
    
    news = get_news(symbol)
    return {"symbol": symbol, "articles": news}