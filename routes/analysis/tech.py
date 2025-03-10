from fastapi import APIRouter
from utils.tech_analysis.tech_analysis import tech_analysis, TICKER_SYMBOL

router = APIRouter()

@router.get("/analysis/tech/summary/")
def get_technical_analysis(symbol: str = TICKER_SYMBOL):
    try:
        analysis_result = tech_analysis(symbol)
        return {"symbol": symbol, "analysis": analysis_result}
    except Exception as e:
        return {"error": str(e)}