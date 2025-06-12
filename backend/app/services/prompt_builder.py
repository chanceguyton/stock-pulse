
def build_prompt(ticker, reddit_results, stock_data, financial_data, earnings_data):
    reddit_snippets = "\n\n".join([f"- {item['title']}: {item['snippet']}" for item in reddit_results[:5]])
    earnings_summary = "\n".join([
        f"{r.get('period', 'N/A')}: EPS {r.get('actual', 'N/A')} vs {r.get('estimate', 'N/A')}"
        for r in earnings_data[:2]  # safely slice the list
    ])
    prompt = f"""You are an expert financial analyst. Analyze the top reddit threads, stock data,
            and earnings data below for {ticker}.

---

### Reddit Sentiment
{reddit_snippets}

### Stock Market Data
- Current Price: {stock_data.get('c')}
- High: {stock_data.get('h')} 
- Low: {stock_data.get('l')}
- Open: {stock_data.get('o')}
- Previous Close: {stock_data.get('pc')}

### Financial Metrics
- P/E Ratio: {financial_data.get('peRatio')}
- P/B Ratio: {financial_data.get('pbRatio')}
- Net Profit Margin: {financial_data.get('netMargin')}
- Revenue Growth (YoY): {financial_data.get('revenueGrowth')}
- Current Ratio: {financial_data.get('currentRatio')}
- Market Capitalization: {financial_data.get('marketCap')}
- 52 Week High: {financial_data.get('high52')}
- 52 Week Low: {financial_data.get('low52')}

### Recent Earnings Reports
{earnings_summary}

Make a recommendation (Buy, Sell, Hold) based on the above information. Provide a brief explanation for your recommendation and consider outside context (larger market trends) as necessary."
"""
    return prompt.strip()
