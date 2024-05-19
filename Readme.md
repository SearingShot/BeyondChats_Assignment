```markdown

# BeyondChats Assignment

Building a Citation Checker From Given API - https://devapi.beyondchats.com/api/get_message_with_sources 

# Citations Checker

Citations Checker is a web application that fetches data from a given API endpoint and identifies citations in responses based on the sources provided. The application uses `Flask` for the web framework and `scikit-learn` for text processing.

## Features

- Fetch data from a remote API.
- Tokenize and filter text to identify matching sources.
- Display citations with their IDs and links in a user-friendly interface.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SearingShot/Citation_Checker.git
    cd citations-checker
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
        ```bash
        venv\Scripts\activate
        ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## File Structure

```
citations-checker/
├── templates/
│   └── index.html       # HTML template for the main page
├── static/
│   └── style.css        # CSS styles for the application
├── Task.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── README.md            # This README file
```

## Dependencies

- Flask
- scikit-learn
- requests

## Code Overview

### 'Task.py'

This is the main file that contains the Flask application logic. It includes functions to:

- Fetch data from the API endpoint ('retrieve_data').
- Tokenize and filter text using 'scikit-learn' ('tokenize_texts').
- Find citations by matching tokens in the response and context ('find_citations').
- Define the home route to render the citations ('home').

### `templates/index.html`

This file contains the HTML template for the main page. It dynamically displays the citations fetched and processed by the Flask application.

### `static/style.css`

This file contains the CSS styles for the application. It styles the main page and the citations list.
