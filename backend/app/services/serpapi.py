import requests
from config import SERPAPI_KEY

def get_reddit_mentions(ticker, limit: int = 5):
    query = f"{ticker} site:reddit.com"
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY
    }

    # Live call (counts against quota)
    response = requests.get(url, params=params)
    data = response.json()
    if "error" in data or data.get("status") == "Rate limit reached":
        return {"error": "Reddit data limit reached. Please try again later."}

    if response.status_code != 200:
        return {"error": f"SerpAPI request failed: {response.status_code}"}

    
    return data.get("organic_results", [])[:5]