# 🎬 Movie Recommendation System

A modern **Movie Recommendation Web App** built using **Machine Learning and Streamlit**, inspired by platforms like Netflix and PickAMovieForMe.

🔗 **Live Demo:** (Add your deployed link here)

---

## 🚀 Features

- 🎯 Personalized movie recommendations
- 🔍 Search-based movie selection
- 🎲 "Surprise Me" random movie generator
- 🎨 Clean and modern UI (Netflix-style design)
- ⚡ Fast and interactive Streamlit web app

---

## 🧠 Machine Learning Approach

This project uses **Content-Based Filtering**:

- Feature extraction from:
  - Genres
  - Cast
  - Keywords
  - Overview
- Text vectorization using **CountVectorizer**
- Similarity calculation using **Cosine Similarity**

---

## 📁 Project Structure
movie-recommender-app
│
├── app.py # Streamlit web app
├── movies.pkl # Processed movie dataset
├── similarity.pkl # Similarity matrix
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## ⚙️ Installation (Run Locally)

```bash
# Clone the repository
git clone https://github.com/your-username/movie-recommender-app.git

# Navigate to project folder
cd movie-recommender-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
