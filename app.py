from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# load your TF-IDF matrix, model, and dataset here
df = pd.read_csv("imdb_top_1000.csv")
# load pickled TF-IDF vectorizer / matrix if required
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "Movie Recommender API is running!"

@app.route("/recommend", methods=["POST"])
def recommend():
    query = request.json.get("query", "")
    # your TF-IDF filtering logic goes here
    results = ["Example Movie 1", "Example Movie 2"]
    return jsonify(results)
