📈 Stock Pulse
Stock Pulse is a full-stack web application that analyzes real-time stock data and Reddit sentiment to generate AI-driven investment recommendations.

Built to practice managing a multi-layered product with frontend/backend integration, third-party APIs, and a real-world user experience.

🚀 Features
🔍 Search any stock ticker (e.g., AAPL, NVDA)

📈 Displays live stock data, valuation metrics, and recent earnings

💬 Pulls recent Reddit discussion using SerpAPI

🤖 Uses Google Gemini to generate AI sentiment analysis and recommendations

💡 Fully responsive UI with error handling and loading states

🧠 Tech Stack
Frontend: React (Vite), deployed via Vercel

Backend: FastAPI, deployed via Render

AI & Data Sources:

Google Gemini

Finnhub API

SerpAPI

Other: Tailored CORS config, custom prompt engineering, error state logic

⚙️ Running Locally
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
🌐 Live Demo
Frontend: https://stock-pulse.vercel.app
Backend: https://stock-pulse-api.onrender.com

🧑‍💼 Project Motivation
After completing a smaller project (9C Test), I wanted to go deeper and learn how to plan and manage a multi-part product. Stock Pulse gave me the opportunity to design a tool end-to-end — including a clean user interface, backend architecture, and intelligent API coordination.

I focused on managing complexity, prioritizing usability, and building robust error-handling into the system — key PM skills I wanted to grow.

⚠️ Disclaimer
Stock Pulse is for informational purposes only and does not constitute financial advice. All AI-generated content is provided "as is."

Let me know if you'd like a badge-based version, portfolio-optimized version, or tailored for recruiters.
