import streamlit as st
import pickle
import pandas as pd
import requests

api_key = "2703462b"


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # TO FIND INDEX
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]



    recommended_movies=[]
    for i in movies_list:


        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)





        # url = f"http://www.omdbapi.com/?apikey={api_key}&t={i}"
        #
    image_width = 200
        #
        # response = requests.get(url)
        # data = response.json()
        # poster_url = data["Poster"]

        # st.image(poster_url, width=image_width)
        # st.write(i)
        # st.write(recommendations[0])

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        url_1 = f"http://www.omdbapi.com/?apikey={api_key}&t={recommendations[0]}"


        response = requests.get(url_1)
        data = response.json()
        poster_url_1 = data["Poster"]


        st.image(poster_url_1, width=image_width,use_column_width='never')
        st.write(recommendations[0])

    with col2:
        url_2 = f"http://www.omdbapi.com/?apikey={api_key}&t={recommendations[1]}"
        response = requests.get(url_2)
        data = response.json()
        poster_url_2 = data["Poster"]

        st.image(poster_url_2, width=image_width,use_column_width='never')
        st.write(recommendations[1])

    with col3:
        url_3 = f"http://www.omdbapi.com/?apikey={api_key}&t={recommendations[2]}"
        response = requests.get(url_3)
        data = response.json()
        poster_url_3 = data["Poster"]

        st.image(poster_url_3, width=image_width,use_column_width='never')
        st.write(recommendations[2])

    with col4:
        url_4 = f"http://www.omdbapi.com/?apikey={api_key}&t={recommendations[3]}"
        response = requests.get(url_4)
        data = response.json()
        poster_url_4 = data["Poster"]

        st.image(poster_url_4, width=image_width,use_column_width='never')
        st.write(recommendations[3])

    with col5:
        url_5 = f"http://www.omdbapi.com/?apikey={api_key}&t={recommendations[4]}"
        response = requests.get(url_5)
        data = response.json()
        poster_url_5 = data["Poster"]

        st.image(poster_url_5, width=image_width,use_column_width='never')
        st.write(recommendations[4])

st.markdown("<style>div.Widget.row-widget.stHorizontal > div{flex: 0 0 auto;}</style>", unsafe_allow_html=True)