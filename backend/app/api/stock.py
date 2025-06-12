from fastapi import APIRouter, Query
from app.services.finnhub import get_quote, get_earnings, get_financials

stock_bp = APIRouter()

@stock_bp.get("/quote")
def quote(ticker: str = Query(...)):
    data = get_quote(ticker)
    if "error" in data:
        return {"error": data["error"]}
    return data

@stock_bp.get("/earnings")
def earnings(ticker: str = Query(...)):
    data = get_earnings(ticker)
    if "error" in data:
        return {"error": data["error"]}
    return data

@stock_bp.get("/financials")
def financials(ticker: str = Query(...)):
    data = get_financials(ticker)
    if "error" in data:
        return {"error": data["error"]}
    return data