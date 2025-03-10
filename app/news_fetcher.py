# Handles fetching and preprocessing news 

import requests
from config import NEWS_API_KEY


def fetch_news(category="technology", language="en", page_size=10):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&language={language}&pageSize={page_size}&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    if data.get("status") == "ok":
        return [
            {"title": article["title"], "description": article["description"], "url": article["url"]}
            for article in data.get("articles", []) if article["title"] and article["description"]
        ]
    
    return []