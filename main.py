from typing import Union
from utils.social_analysis.news_feed import get_news, DEFAULT_SYMBOL

from fastapi import FastAPI

from utils.tech_analysis.tech_analysis import tech_analysis

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/news/")
def fetch_news(symbol: str = DEFAULT_SYMBOL):
    news = get_news(symbol)
    return {"symbol": symbol, "articles": news}

@app.get("/tech-analysis/")
def get_technical_analysis(symbol: str = "DIS"):
    """
    Fetches and returns technical analysis for the given stock symbol.
    
    Query Parameters:
        symbol (str): Stock symbol (default is "DIS").
    
    Returns:
        JSON response with technical analysis summary.
    """
    try:
        # Call the tech_analysis function from tech_analysis.py
        analysis_result = tech_analysis(symbol)
        return {"symbol": symbol, "analysis": analysis_result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}