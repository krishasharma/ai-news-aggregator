# Implements keyword-based filtering 

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

USER_PREFERENCES = ["AI", "Python", "Machine Learning", "Cybersecurity"]

def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())  # Convert to lowercase and tokenize
    return [word for word in words if word.isalnum() and word not in stop_words]

def filter_news(articles):
    filtered_articles = []

    for article in articles:
        title_tokens = preprocess_text(article["title"])
        description_tokens = preprocess_text(article["description"])

        for keyword in USER_PREFERENCES:
            if keyword.lower() in title_tokens or keyword.lower() in description_tokens:
                filtered_articles.append(article)
                break  # Avoid duplicate matches
        
    return filtered_articles