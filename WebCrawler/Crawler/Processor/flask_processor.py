import json
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

class Indexer:
    def __init__(self, documents):
        self.documents = documents
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)

    def search(self, query, top_k=5):
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix)
        scores = cosine_similarities[0]
        sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        result = []
        for i in sorted_indices[:top_k]:
            if scores[i] > 0 and i < len(self.documents):
                result.append((i, scores[i]))  # Return document index and score
        return result

# Load data from JSON file
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract text from JSON data
documents = [entry.get('text', '') for entry in data if entry.get('text')]

# Create Indexer instance
indexer = Indexer(documents)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def process_query():
    req_data = request.get_json()
    if not req_data or 'query' not in req_data or not req_data['query'].strip():
        return jsonify({'error': 'Invalid query. Query cannot be empty.'}), 400

    query = req_data['query']
    top_k = int(req_data.get('top_k', 5))  # Number of top results to return, default is 5

    results = indexer.search(query, top_k=top_k)
    if not results:
        return jsonify({'error': 'No results found for the query.'}), 404

    formatted_results = []
    for i, score in results:
        if i < len(data) and data[i].get('author'):
            filename = data[i]['author']
            text = data[i]['text']
            tags = data[i]['tags']
        else:
            filename = "Undefined"
            text = ""
            tags = []
        formatted_results.append({"Authorname": filename, "text": text, "tags": tags, "cosine_similarity_score": score})

    return jsonify(formatted_results)

if __name__ == '__main__':
    app.run(debug=True)
