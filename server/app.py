from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from collections import Counter
from bs4 import BeautifulSoup
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_most_frequent_words(url, n=10):
    # Fetch page content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Tokenize and filter words
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(n)

    return [{"word": word, "frequency": count} for word, count in most_common_words]

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        result = get_most_frequent_words(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
