# "https://devapi.beyondchats.com/api/get_message_with_sources"

import requests
from flask import Flask, render_template
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

def retrieve_data():
    api_endpoint = "https://devapi.beyondchats.com/api/get_message_with_sources"
    response = requests.get(api_endpoint)
    return response.json().get("data", {}).get("data", [])

def tokenize_texts(texts):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    tokens_list = []
    for text in texts:
        tokens = vectorizer.build_analyzer()(text)
        tokens_list.append(set(tokens))
    return tokens_list

def find_citations(data):
    citations = []

    for entry in data:
        response_text = entry['response']
        sources = entry['source']
        response_tokens = tokenize_texts([response_text])[0]
        matching_sources = []

        for source in sources:
            context_tokens = tokenize_texts([source['context']])[0]
            if response_tokens & context_tokens:
                matching_sources.append({
                    "id": source['id'],
                    "link": source.get('link', '')
                })

        citations.extend(matching_sources)

    return citations

@app.route('/')
def home():
    data = retrieve_data()
    citations = find_citations(data)
    return render_template('index.html', citations=citations)

if __name__ == '__main__':
    app.run(debug=True)