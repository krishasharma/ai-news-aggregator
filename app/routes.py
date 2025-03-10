# Defines the API routes

from flask import request, jsonify
from app import app  # Import the Flask app instance
from app.news_fetcher import fetch_news
from app.filter import filter_news

@app.route("/news", methods=["GET"])
def get_news():
    category = request.args.get("category", "technology")  # Default to technology
    raw_articles = fetch_news(category=category)
    filtered_articles = filter_news(raw_articles)
    
    return jsonify(filtered_articles)