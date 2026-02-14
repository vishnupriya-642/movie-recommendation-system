import streamlit as st
import sys
from pathlib import Path

# Add src folder to path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR / "src"))

from app.recommender import recommend_movies

st.title("Movie Recommendation System")

st.write("Enter a movie name to get similar movie recommendations.")

movie_title = st.text_input("Movie Title")
top_n = st.number_input("Number of Recommendations", min_value=1, max_value=20, value=5)

if st.button("Get Recommendations"):
    if movie_title:
        results = recommend_movies(movie_title, top_n)

        if results:
            st.subheader("Recommended Movies:")
            for movie in results:
                st.write(f"Title: {movie['title']}")
                st.write(f"Genres: {movie['genres']}")
                st.write("---")
        else:
            st.warning("Movie not found.")
    else:
        st.warning("Please enter a movie title.")
