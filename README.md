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
