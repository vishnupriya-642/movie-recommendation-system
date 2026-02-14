<<<<<<< HEAD
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
=======
# 🎬 Movie Recommendation System

A **content-based Movie Recommendation System** built using Python and machine learning fundamentals.  
The system recommends movies similar to a given movie by analyzing **movie metadata and similarity scores**.

This project focuses on **core ML concepts**, clean data preprocessing, and understanding how real-world recommendation engines work at a basic level.

---

## 🧠 Problem Statement
Users often struggle to discover movies similar to ones they already like.  
This project solves that problem by recommending movies based on **content similarity** rather than user ratings or behavior.

---

## 🛠️ Technologies Used
- Python
- Pandas – data loading and preprocessing  
- NumPy – numerical operations  
- Scikit-learn – feature extraction and similarity computation  

---

## 📂 Dataset

This project uses the **MovieLens dataset** provided by GroupLens.

- Source: https://grouplens.org/datasets/movielens/
- Contains movie metadata and user ratings
- Widely used for building and evaluating recommendation systems

The dataset is not included in this repository due to size constraints.


## ⚙️ Approach & Methodology

1. **Data Preprocessing**
   - Cleaned and selected relevant movie features
   - Handled missing values
   - Prepared text data for modeling

2. **Feature Engineering**
   - Combined important movie attributes (such as genres and descriptions)
   - Converted text data into numerical vectors

3. **Similarity Computation**
   - Used **cosine similarity** to measure similarity between movies
   - Created a similarity matrix

4. **Recommendation Logic**
   - Identified the most similar movies for a given input
   - Returned top recommended movies

---

## ▶️ How to Run the Project

1. Clone the repository
   ```bash
   git clone https://github.com/vishnupriya-642/movie-recommendation-system.git
>>>>>>> 52bfc0544025cb9cf769dc52e8f866e092ac6707
