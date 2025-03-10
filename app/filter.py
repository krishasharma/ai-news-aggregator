# Implements keyword-based filtering 
import nltk
import os

# Ensure NLTK uses the correct data path
nltk.data.path.append(os.path.expanduser("~/nltk_data"))

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# User-defined preferences (keywords to filter news)
USER_PREFERENCES = ["AI", "Python", "Machine Learning", "Cybersecurity"]

# Function to preprocess text: tokenize, lowercase, and remove stopwords
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())  # Convert to lowercase and tokenize
    return [word for word in words if word.isalnum() and word not in stop_words]

# Function to filter news articles based on user preferences
def filter_news(articles):
    filtered_articles = []

    for article in articles:
        title_tokens = preprocess_text(article["title"])
        description_tokens = preprocess_text(article["description"])

        # Check if any keyword from USER_PREFERENCES matches the article
        for keyword in USER_PREFERENCES:
            if keyword.lower() in title_tokens or keyword.lower() in description_tokens:
                filtered_articles.append(article)
                break  # Avoid duplicate matches
        
    return filtered_articles