import React from "react";
import ReactMarkdown from "react-markdown";
import "./AnalysisCard.css"; 

// Format from the backend response
//  {    
//         "ticker": ticker,
//         "reddit_results": reddit_results,
//         "stock_data": stock_data,
//         "earnings_data": earnings_data,
//         "analysis": response}

const AnalysisCard = ({ result }) => {

  if (!result) {
    return null;
  }

  return (
    <div className="analysis-card">
      <div className="section">
        <h2 className="ticker-heading">AI Analysis for {result.ticker}</h2>
        <div className="markdown-output">
          <ReactMarkdown>{result.analysis}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
};

export default AnalysisCard;