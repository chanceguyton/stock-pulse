from app.services import serpapi, finnhub, gemini, prompt_builder
from fastapi import APIRouter
import re

analyze_bp = APIRouter()
@analyze_bp.get("/")
def run_analysis(ticker: str):
    return analyze_stock(ticker)

def clean_markdown(md: str) -> str:
    md = re.sub(r'^\s*\*\s+', '- ', md, flags=re.MULTILINE)
    md = re.sub(r'^\s*\*\s*$', '', md, flags=re.MULTILINE)
    md = re.sub(r'^\s{3,}', '  ', md, flags=re.MULTILINE)
    md = re.sub(r'([^\n])(\n#+ )', r'\1\n\2', md)       
    md = re.sub(r'([^\n])(\n- )', r'\1\n\2', md)    
    return md


def analyze_stock(ticker: str):
    stock_data = finnhub.get_quote(ticker)
    earnings_data = finnhub.get_earnings(ticker)
    financial_data = finnhub.get_financials(ticker)

    if any("error" in d for d in [stock_data, earnings_data, financial_data]):
      return {"error": "Invalid or incomplete data. Please enter a valid stock ticker."}

    reddit_results = serpapi.get_reddit_mentions(ticker)

    if isinstance(reddit_results, dict) and "error" in reddit_results:
        reddit_error = reddit_results["error"]
        reddit_results = []
    else:
        reddit_error = None 

    prompt = prompt_builder.build_prompt(
        ticker=ticker, 
        reddit_results=reddit_results, 
        stock_data=stock_data, 
        financial_data=financial_data,
        earnings_data=earnings_data)
    response = gemini.run_analysis(prompt)
    clean_response = clean_markdown(response)
    return {
        "ticker": ticker,
        "reddit_results": reddit_results,
        "reddit_error": reddit_error,
        "stock_data": stock_data,
        "financial_data": financial_data,
        "earnings_data": earnings_data,
        "analysis": clean_response}