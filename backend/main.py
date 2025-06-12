from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from app.api.reddit import reddit_bp
from app.api.stock import stock_bp
from app.api.analyze import analyze_bp  # you can stub this for now

# Load environment variables from .env
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Stock Sentiment API",
    version="1.0",
    description="API for combining news, stock data, and AI analysis"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://stock-pulse-brown.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(reddit_bp, prefix="/api/reddit")
app.include_router(stock_bp, prefix="/api/stock")
app.include_router(analyze_bp, prefix="/api/analyze")

# Root route
@app.get("/")
def read_root():
    return {"message": "Stock Sentiment App backend is running"}
