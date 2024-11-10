# Word Frequency Analyzer

This project is a web application that analyzes the most frequent words on a specified webpage. The user inputs a URL, and the backend processes the page content to return the top `n` most frequent words along with their frequencies.

## Features

- Fetches and parses webpage content from a provided URL.
- Counts the frequency of each word on the webpage.
- Returns the `n` most frequent words and displays them in a user-friendly table.(can be set inside the backend)

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Additional Libraries**: 
  - [Requests](https://pypi.org/project/requests/) (for fetching webpage content)
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) (for HTML parsing)
  - [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) from `collections` (for word frequency counting)
  - [CORS](https://flask-cors.readthedocs.io/en/latest/) (to handle cross-origin requests)

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/word-frequency-analyzer.git
    cd word-frequency-analyzer
    ```

2. **Set up a virtual environment** (recommended):
    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask backend**:
    ```bash
    python app.py
    ```
    The backend will run on `http://127.0.0.1:5000`.

5. **Serve the frontend**:
    Open `index.html` in your browser, or serve it using a simple server (e.g., `python -m http.server`).

## API Endpoint

### `POST /analyze`

- **Description**: Receives a URL from the frontend, fetches the webpage content, and analyzes the word frequencies.
- **Request Body**:
    ```json
    {
        "url": "https://example.com"
    }
    ```
- **Response**:
    - Returns a JSON array of objects containing each word and its frequency:
    ```json
    [
        {"word": "example", "frequency": 10},
        {"word": "test", "frequency": 8},
        ...
    ]
    ```

## Code Explanation

The core functionality is in the `get_most_frequent_words` function in `app.py`, which:

1. **Fetches the page content** of the provided URL.
2. **Parses and extracts** text from the page.
3. **Tokenizes and normalizes** words to count their occurrences.
4. **Returns the top n** most frequent words as JSON.

### Frontend and Backend Interaction

1. The **frontend** (in `index.html`) provides an input box for the URL and a button to initiate analysis.
2. When the button is clicked, it sends a POST request to the Flask backend at `/analyze`.
3. The **backend** receives the URL, processes the webpage to find the most frequent words, and sends the results back as JSON.
4. The frontend displays the results in a table, showing each word and its frequency.

## Example

For example, if you input `https://www.example.com` and request the top 10 words, the application will display something like:

| Word     | Frequency |
|----------|-----------|
| example  | 10        |
| website  | 8         |
| ...      | ...       |

## License

This project is licensed under the MIT License. See `LICENSE` for more information.
