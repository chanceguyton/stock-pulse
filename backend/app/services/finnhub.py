import finnhub
from config import FINNHUB_API_KEY

# Setup client
client = finnhub.Client(api_key=FINNHUB_API_KEY)

# Get real-time quote data
def get_quote(ticker):
    try:
        data = client.quote(ticker)
        # Finnhub returns 0 for all fields if ticker is invalid
        if not data or data.get("c") == 0:
            return {"error": f"No valid quote data found for ticker '{ticker}'."}
        return data
    except Exception as e:
        return {"error": str(e)}

# Get earnings data
def get_earnings(ticker):
    try:
        response = client.company_earnings(ticker)
        if not response or not isinstance(response, list):
            return {"error": f"No earnings data found for ticker '{ticker}'."}
        return response[:2]
    except Exception as e:
        return {"error": str(e)}
    
def get_financials(ticker):
    try:
        data = client.company_basic_financials(ticker, 'all')
        metrics = data.get("metric", {})

        # If metrics dict is empty, it's an invalid ticker
        if not metrics:
            return {"error": f"No financial metrics found for ticker '{ticker}'."}

        return {
            "peRatio": metrics.get("peBasicExclExtraTTM"),
            "pbRatio": metrics.get("pbAnnual"),
            "netMargin": metrics.get("netProfitMarginTTM"),
            "revenueGrowth": metrics.get("revenueGrowthTTMYoy"),
            "currentRatio": metrics.get("currentRatioAnnual"),
            "marketCap": metrics.get("marketCapitalization"),
            "high52": metrics.get("52WeekHigh"),
            "low52": metrics.get("52WeekLow")
        }
    except Exception as e:
        return {"error": str(e)}