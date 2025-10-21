import pandas as pd 
import numpy as np 
import pickle
from sklearn.metrics.pairwise import cosine_similarity


Users = pd.read_csv('./data/Users.csv')
Books = pd.read_csv('./data/Books.csv')
Ratings = pd.read_csv('./data/Ratings.csv')

ratings_with_name = Ratings.merge(Books, on='ISBN')
# print(Users.shape)
# print(Books.shape)
# print(Ratings.shape)


x = ratings_with_name.groupby('User-ID').count()['Book-Rating'] > 200
reader_users = x[x].index
# print(reader_users.shape)
filtered_rating  = ratings_with_name[ratings_with_name['User-ID'].isin(reader_users)]

y = filtered_rating.groupby('Book-Title').count()['Book-Rating']>=50
famous_books = y[y].index
final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]
# print(famous_books.shape)

table = final_ratings.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
# print(table.shape)
# an importnat step otherwise we will get error calculting similarity score
table.fillna(0, inplace=True) 

similarity_score = cosine_similarity(table)

pickle.dump((table, similarity_score), open("book_model.pkl", "wb"))


# creating a function to find this similar books 
def recommend(book_name):
    index = np.where(table.index ==book_name)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])),key= lambda x:x[1],reverse=True)[1:6]

    for i in similar_books:
        print(table.index[i[0]])
    
# print(recommend('1984'))