import React from "react";

const formatMarketCap = (rawCapInMillions) => {
  const cap = rawCapInMillions * 1_000_000; // Convert M → absolute

  if (cap >= 1e12) return `$${(cap / 1e12).toFixed(2)}T`;
  if (cap >= 1e9) return `$${(cap / 1e9).toFixed(2)}B`;
  if (cap >= 1e6) return `$${(cap / 1e6).toFixed(2)}M`;
  return `$${cap.toLocaleString()}`;
};

const StockDataCard = ({ results }) => {
    if (!results) {
        return null;
    }
    
    return (
        <div className="stock-data-card">
            <h2 className="basic-data">Quote</h2>
                <div className="stock-data">
                <p><strong>Ticker:</strong> {results.ticker}</p>
                <p><strong>Current Price:</strong> ${results.stock_data.c.toFixed(2)}</p>
                <p><strong>High:</strong> ${results.stock_data.h.toFixed(2)}</p>
                <p><strong>Low:</strong> ${results.stock_data.l.toFixed(2)}</p>
                <p><strong>Open:</strong> ${results.stock_data.o.toFixed(2)}</p>
                <p><strong>Previous Close:</strong> ${results.stock_data.pc.toFixed(2)}</p>
                </div>
            <hr/>
            <h2 className="valuation-data">Valuation Metrics</h2>
            <div className="valuation-data">
                <p><strong>Market Cap:</strong> {formatMarketCap(results.financial_data.marketCap)}</p>
                <p><strong>52 Week High:</strong> ${results.financial_data.high52.toFixed(2)}</p>
                <p><strong>52 Week Low:</strong> ${results.financial_data.low52.toFixed(2)}</p> 
                <p><strong>PE Ratio:</strong> {results.financial_data.peRatio.toFixed(2)}</p>
                <p><strong>PB Ratio:</strong> {results.financial_data.pbRatio.toFixed(2)}</p>
                <p><strong>Current Ratio:</strong> {results.financial_data.currentRatio.toFixed(2)}</p>
                <p><strong>Net Margin:</strong> {results.financial_data.netMargin.toFixed(2)}%</p>
                <p><strong>Revenue Growth:</strong> {results.financial_data.revenueGrowth.toFixed(2)}%</p> 
            </div>  
            <hr/>
            <h2 className="earnings">Earnings Last 2 Quarters</h2>
            <div className="earnings-data">
                {results.earnings_data.map((q, i) => (
                <div key={i}>
                    <p><strong>Quarter: {q.quarter}</strong></p>
                    <ul>
                        <li>Period: {q.period}</li>
                        <li>EPS Actual: {q.actual.toFixed(2)}</li>
                        <li>EPS Estimate: {q.estimate.toFixed(2)}</li>
                        <li>Surprise: {q.surprisePercent.toFixed(2)}%</li>
                    </ul>
                </div>
                ))}
            </div>
        </div>
    )
}

export default StockDataCard;