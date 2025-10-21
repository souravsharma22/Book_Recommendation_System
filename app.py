from flask import Flask
import pickle
# table, similarity_score = pickle.load(open("book_model.pkl", "rb"))
from recommend import recommendBook
# print(recommendBook('1984'))

app = Flask(__name__)
@app.route('/')
def index():
    return "This is an API, all : api/recommend/<book_name>"

@app.route("/api/recommend/<book_name>")
def recommendations(book_name): 
    books = recommendBook(book_name)
    return books

if __name__ == "__main__":
    app.run(debug=True)