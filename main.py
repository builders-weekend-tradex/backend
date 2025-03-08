import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from utils.social_analysis.news_feed import get_news, COMPANY_NAME
from utils.tech_analysis.tech_analysis import tech_analysis, TICKER_SYMBOL
from utils.fundamental_analysis.lexi import lexi_chat 

DISABLE_NEWS_FETCH = os.getenv("DISABLE_NEWS_FETCH", "false").lower() == "true"

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

### GET

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/analysis/social/news/everything/")
def fetch_news(symbol: str = COMPANY_NAME):
    if DISABLE_NEWS_FETCH:
        return {"symbol": symbol, "message": "News fetching is currently disabled."}
    
    news = get_news(symbol)
    return {"symbol": symbol, "articles": news}

@app.get("/analysis/tech/summary/")
def get_technical_analysis(symbol: str = TICKER_SYMBOL):
    try:
        analysis_result = tech_analysis(symbol)
        return {"symbol": symbol, "analysis": analysis_result}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

### POST

@app.post("/analysis/lexi/")
def chat_with_lexi(request: ChatRequest):
    response = lexi_chat(request.message)
    return {"response": response}