import pickle
import numpy as np
from flask import jsonify

table, similarity_score = pickle.load(open("book_model.pkl", "rb"))

def recommendBook(book_name):
    indexes = np.where(table.index == book_name)[0]
    if len(indexes) == 0:
        return jsonify({"status":False, "input": book_name, "recommendations": "No such book in database"})  
    index = indexes[0]
    similar_books = sorted( list(enumerate(similarity_score[index])) , key = lambda x:x[1] , reverse=True)[1:11]
    s_book = []
    for i in similar_books:
        s_book.append(table.index[i[0]])
    return jsonify({"status":True, "input": book_name, "recommendations": s_book})