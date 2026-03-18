import streamlit as st
import pickle
import pandas as pd
import random

# Load data
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:11]

    return [movies.iloc[i[0]].title for i in movies_list]


# 🎨 Page config
st.set_page_config(page_title="Pick A Movie", layout="wide")

# 🎨 FULL UI CSS (Modern Website Feel)
st.markdown("""
<style>

/* Remove padding */
.block-container {
    padding-top: 2rem;
}

/* Background gradient */
body {
    background: linear-gradient(135deg, #141e30, #243b55);
}

/* Center everything */
.main {
    text-align: center;
}

/* Big title */
.title {
    font-size: 60px;
    font-weight: 800;
    color: white;
    margin-top: 50px;
}

/* Subtitle */
.subtitle {
    font-size: 20px;
    color: #cccccc;
    margin-bottom: 40px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    border-radius: 30px;
    padding: 14px 35px;
    font-size: 18px;
    border: none;
    margin: 10px;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* Movie Card */
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    margin: 15px auto;
    width: 60%;
    color: white;
    font-size: 20px;
    transition: 0.3s;
    backdrop-filter: blur(10px);
}

.card:hover {
    transform: scale(1.05);
    background: rgba(255,255,255,0.15);
}

/* Input box */
.stTextInput>div>div>input {
    border-radius: 20px;
    padding: 10px;
}

/* Selectbox */
.stSelectbox>div>div {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


# 🎬 HEADER (Hero Section)
st.markdown('<div class="title">🎬 Pick A Movie</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover your next favorite movie instantly</div>', unsafe_allow_html=True)

# 🔍 Search
search = st.text_input("", placeholder="Search for a movie...")

filtered = movies[movies['title'].str.contains(search, case=False)] if search else movies

selected_movie = st.selectbox("", filtered['title'].values)

# 🎯 Buttons (centered)
col1, col2, col3 = st.columns([1,1,1])

with col2:
    recommend_btn = st.button("🎯 Recommend")
    random_btn = st.button("🎲 Surprise Me")

# 🎥 Recommendations
if recommend_btn:
    results = recommend(selected_movie)

    st.markdown("## 🎥 Recommendations")

    for movie in results[:5]:
        st.markdown(f'<div class="card">{movie}</div>', unsafe_allow_html=True)

# 🎲 Random Movies
if random_btn:
    random_movies = random.sample(list(movies['title']), 5)

    st.markdown("## 🎲 Random Picks")

    for movie in random_movies:
        st.markdown(f'<div class="card">{movie}</div>', unsafe_allow_html=True)