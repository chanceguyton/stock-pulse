# 📈 Stock Pulse
Stock Pulse is a full-stack web application that analyzes real-time stock data and Reddit sentiment to generate AI-driven investment recommendations.

Built to practice managing multilayered, interconnected products.

## 🚀 Features
🔍 Search any stock ticker (e.g., AAPL, NVDA)

📈 Displays live stock data, valuation metrics, and recent earnings

💬 Pulls recent Reddit discussion using SerpAPI

🤖 Uses Google Gemini to generate AI sentiment analysis and recommendations

💡 Fully responsive UI with error handling and loading states

## 🧪 Tech Stack
Frontend: React (Vite), deployed via Vercel

Backend: FastAPI, deployed via Render

AI & Data Sources: Google Gemini, Finnhub API, SerpAPI

## ⚙️ Running Locally
Prerequisites
Python 3.11+

Node.js & npm

API Keys: FINNHUB_API_KEY, SERPAPI_KEY, GEMINI_API_KEY

Backend
bash
Copy
Edit
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Frontend
bash
Copy
Edit
cd frontend
npm install
npm run dev

## 🌐 Live Demo
https://stock-pulse-brown.vercel.app

## 💡 Project Motivation
After building 9C Test, I wanted to go deeper — not just into coding, but into managing complex, interconnected projects. I came up with Stock Pulse, an app that analyzes stock sentiment by combining market data, Reddit discussions, and AI-generated recommendations. It required coordinating three backend APIs and a frontend UI—an ideal opportunity to learn how to scope, sequence, and manage a full-stack build from idea to execution.

## ⚠️ Disclaimer
Stock Pulse is for informational purposes only and does not constitute financial, investment, or trading advice. All content, including AI-generated analysis, is provided "as is" and may not reflect real-time market conditions. Always conduct your own research and consult a licensed financial advisor before making investment decisions.


