import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

# Resolve dynamic path safely
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "notebooks" / "data" / "movies.csv"

# Load dataset once at startup
try:
    movies = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    raise RuntimeError(f"Dataset not found at {DATA_PATH}")

movies["genres"] = movies["genres"].replace("(no genres listed)", "")

# Build TF-IDF model
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create title index mapping
indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()


def recommend_movies(movie_title: str, top_n: int = 5):
    """
    Returns top_n similar movies based on genre similarity.
    """

    if movie_title not in indices:
        raise ValueError("Movie not found in dataset")

    idx = indices[movie_title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Skip first one (itself)
    sim_scores = sim_scores[1 : top_n + 1]

    movie_indices = [i[0] for i in sim_scores]

    return movies.iloc[movie_indices][["title", "genres"]].to_dict(orient="records")
