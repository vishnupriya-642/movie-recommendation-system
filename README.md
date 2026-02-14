# Movie Recommendation System

This project implements a Movie Recommendation System using the MovieLens dataset.
It demonstrates the complete workflow from data analysis in notebooks to serving recommendations using a FastAPI backend.



## Project Structure

movie-recommendation-system/
│
├── notebooks/
│   ├── movie_recommendation_system.ipynb
│   └── data/
│       ├── movies.csv
│       ├── ratings.csv
│       ├── tags.csv
│       └── links.csv
│
├── src/
│   └── app/
│       ├── main.py
│       ├── recommender.py
│       ├── schemas.py
│       ├── __init__.py
│       └── requirements.txt
│
└── README.md



## Dataset

The project uses the MovieLens (latest-small) dataset, which contains:
- Movies and genres
- User ratings
- User-generated tags

This dataset is sparse and reflects real-world recommendation system challenges.



## Approach

Notebook:
- Data loading and preprocessing
- Exploratory data analysis
- Content-based recommendation using movie genres
- Collaborative filtering concepts
- Baseline model for evaluation

Backend:
- FastAPI application to serve recommendations
- Clean separation between ML logic and API layer



## How to Run

Install dependencies:
pip install -r src/app/requirements.txt

Run the API:
uvicorn src.app.main:app --reload

Open API docs:
http://127.0.0.1:8000/docs



## Notes

- The notebook is used for experimentation and learning.
- The FastAPI app is used for serving recommendations.
