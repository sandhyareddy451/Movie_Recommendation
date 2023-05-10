import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movies_recomend_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity_pkl.pkl','rb'))
st.title("Movie Recommended System")
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown", movies['title'].values)


if st.button('Recommended Movies'):
    recommendations = recommend(selected_movie)

    for i in recommendations:
        st.write(i)

