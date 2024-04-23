import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup

class Indexer:
    def __init__(self, filenames):
        self.filenames = filenames
        self.documents = self._retrieve_documents()
        print("Retrieved documents:", len(self.documents))

        if len(self.documents) == 0:
            raise ValueError("No valid documents found. Check your scraping logic.")

        self.vectorizer = TfidfVectorizer(stop_words='english', min_df=1)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
        print("TF-IDF matrix shape:", self.tfidf_matrix.shape)

        self.inverted_index = self._build_inverted_index()
        print("Inverted index:")
        for term, indices in self.inverted_index.items():
            print(term, indices)

    def _retrieve_documents(self):
        documents = []
        for filename in self.filenames:
            with open(filename, 'r', encoding='utf-8') as f:
                html_content = f.read()
                soup = BeautifulSoup(html_content, 'html.parser')
                quote_elements = soup.find_all('strong')
                for quote_element in quote_elements:
                    quote = quote_element.text.strip().replace('\n', ' ')
                    if quote:
                        documents.append(quote)
        return documents

    def _build_inverted_index(self):
        inverted_index = {}
        terms = self.vectorizer.get_feature_names_out()
        for i, doc in enumerate(self.documents):
            for term in terms:
                if term in doc:
                    if term not in inverted_index:
                        inverted_index[term] = []
                    inverted_index[term].append(i)
        return inverted_index

    def search(self, query):
        query_vector = self.vectorizer.transform([query])
        print("Query vector shape:", query_vector.shape)
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix)
        print("Cosine similarities shape:", cosine_similarities.shape)
        scores = cosine_similarities[0]
        print("Cosine similarity scores:", scores)
        sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        result = []
        for i in sorted_indices:
            if scores[i] > 0 and i < len(self.filenames):
                result.append((self.filenames[i], scores[i]))
        return result

    def print_index_as_pickle(self):
        inverted_index_pickle = pickle.dumps(self.inverted_index)
        print("Inverted Index (pickle format):")
        print(inverted_index_pickle)  # Print binary data directly

# Example usage
html_content = """
<html>
<head>
    <title>Goodreads Quotes</title>
</head>
<body>
    <p><strong>“A day without sunshine is like, you know, night.”</strong> - Steve Martin<br>Tags: humor, obvious, simile</p>
    <!-- Other quote elements -->
</body>
</html>
"""

filenames = ['goodreads_quotes.html']

# Write the HTML content to a temporary file
with open('goodreads_quotes.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

try:
    indexer = Indexer(filenames)
    indexer.print_index_as_pickle()

    query = input("Enter your query: ")
    results = indexer.search(query)

    for filename, score in results:
        print(f"Filename: {filename}, Cosine Similarity Score: {score}")

except ValueError as e:
    print("Error:", e)
