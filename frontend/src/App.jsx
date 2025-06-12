import { useState } from 'react'
import SearchBar from './components/SearchBar'
import AnalysisCard from './components/AnalysisCard'
import StockDataCard from './components/StockData'
import RedditCard from './components/RedditCard'
import LoadingSpinner from './components/LoadingSpinner';
import './App.css'

function App() {

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (ticker) => {
  setLoading(true);
  setError(null);  // Clear any previous error
  try {
    const response = await fetch(`https://stock-pulse-api.onrender.com/api/analyze?ticker=${ticker}`);
    const data = await response.json();

    if (data.error) {
      setError(data.error);
      setResult(null);
    } else {
      setResult(data);
    }
  } catch (err) {
    setError("Something went wrong. Please try again later.");
    setResult(null);
  } finally {
    setLoading(false);
  }
};

  return (
    <div className='app-container'>
      <h1 className='app-title'>📈 Stock Pulse</h1>
      <SearchBar onSearch={handleSearch}/>
      {error && <div className="error-message">{error}</div>}
      {loading && <LoadingSpinner/>}
      {!error && !loading && result && (
        <div className="cards-container">
          <div className="left-column">
            <StockDataCard results={result} />
            <RedditCard results={result} />
          </div>
          <AnalysisCard result={result} />
        </div>
      )}

      <footer className='footer'>
        <p>Disclaimer: Stock Pulse is for informational 
          purposes only and does not constitute financial, investment, 
          or trading advice. All content, including AI-generated analysis, 
          is provided "as is" and may not reflect real-time market conditions. 
          Always conduct your own research and consult a licensed financial advisor 
          before making investment decisions.</p>
      </footer>
    </div>
  )
  
    
}

export default App
