from fastapi import APIRouter, Query
from app.services.serpapi import get_reddit_mentions

reddit_bp = APIRouter()

@reddit_bp.get("/")
def fetch_reddit_mentions(ticker: str = Query(...)):
    return get_reddit_mentions(ticker)