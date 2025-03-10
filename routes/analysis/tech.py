from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from utils.tech_analysis.tech_analysis import tech_analysis, TICKER_SYMBOL

router = APIRouter()

@router.get("/analysis/tech/summary/")
def get_technical_analysis(symbol: str = TICKER_SYMBOL):
    try:
        analysis_result = tech_analysis(symbol)[1]
        return {"symbol": symbol, "analysis": analysis_result}
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/analysis/tech/charts/all/")
def get_all_charts(symbol: str = TICKER_SYMBOL):
    try:
        html_charts = tech_analysis(symbol)
        combined_html = "<br>".join(html_charts.values())
        return HTMLResponse(content=combined_html)
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/analysis/tech/charts/{chart_name}")
def get_single_chart(chart_name: str, symbol: str = TICKER_SYMBOL):
    try:
        html_charts = tech_analysis(symbol)[0]
        if chart_name in html_charts:
            return HTMLResponse(content=html_charts[chart_name])
        else:
            raise HTTPException(status_code=404, detail="Chart not found")
    except Exception as e:
        return {"error": str(e)}