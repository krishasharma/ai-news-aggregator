# Initializes the Flask app

from flask import Flask

app = Flask(__name__)

from app import routes