# 🏏 IPL Win Predictor  
### Machine Learning–Powered Match Outcome Prediction

Ever wondered how the winning probability of an IPL match changes ball by ball?  
This project predicts the **win probability of IPL teams in real time** using historical match data and machine learning.

It is a **fully deployed end-to-end web application**, combining data science, backend development, and frontend design.

---

## 📌 Introduction

The **IPL Win Predictor** analyzes live match situations such as:
- Current score
- Remaining balls
- Wickets in hand
- Target score
- Match location

Using these factors, the system predicts the **probability of the batting team winning the match**.

This project demonstrates the **practical application of machine learning** in sports analytics and full-stack web development.

---

## 🚀 Key Features

✅ Real-time win probability prediction  
✅ Interactive and responsive web interface  
✅ Machine learning model trained on historical IPL data  
✅ Flask backend serving ML predictions via REST API  
✅ Deployed frontend and backend (production ready)  
✅ Handles backend cold-start using loading animation  

---

## 🧠 Project Workflow

The project follows a structured pipeline:

### 1️⃣ Data Collection
- Historical IPL match and ball-by-ball datasets
- Extracted relevant match features

### 2️⃣ Data Preprocessing
- Cleaned missing values
- Feature engineering (runs left, balls left, wickets, target)
- Encoded categorical variables

### 3️⃣ Model Training
- Trained a machine learning classification model
- Built a preprocessing + model pipeline
- Saved trained model using Pickle (`pipe.pkl`)

### 4️⃣ Backend Development
- Flask API to serve predictions
- Endpoints for:
  - City list
  - Win probability prediction
- Integrated trained ML model

### 5️⃣ Frontend Development
- Built using HTML, CSS, and JavaScript
- User inputs match details
- Displays win probability dynamically
- Added loading animation to handle backend cold start

### 6️⃣ Deployment
- Frontend hosted on **Netlify**
- Backend hosted on **Render**
- Model served in production environment

---

## 🏗️ Architecture Overview
User (Browser)
↓
Frontend (Netlify)
↓
Flask API (Render)
↓
Machine Learning Model (scikit-learn)

## 🛠️ Tech Stack

### 🔹 Frontend
- HTML
- CSS
- JavaScript

### 🔹 Backend
- Python
- Flask
- Flask-CORS
- Gunicorn

### 🔹 Machine Learning
- Pandas
- NumPy
- Scikit-learn

### 🔹 Deployment
- Netlify (Frontend)
- Render (Backend)

---

## 📂 Project Structure

IPL-WIN-PREDICTOR/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── init.py
│
├── ml/
│ ├── predictor.py
│ ├── pipe.pkl
│ └── cities.txt
│
├── frontend/
│ └── index.html
│
├── README.md
└── .gitignore


---

## 🌐 Live Demo

🔗 **Frontend (Netlify):**  
👉 https://serene-vacherin-5760d3.netlify.app/

🔗 **Backend API (Render):**  
👉 https://ipl-win-predictor-1-ieox.onrender.com

---

## ⏳ Backend Cold-Start Handling

The backend is hosted on **Render Free Plan**, which goes to sleep when inactive.

🔹 First request may take some time  
🔹 A loading animation is shown to users  
🔹 Improves user experience during server wake-up  

This design decision reflects **real-world production constraints**.

---

## 📈 Future Enhancements

- Cache city list on frontend
- Improve model accuracy with more features
- Add match history visualization
- User authentication
- Upgrade backend hosting to eliminate cold starts

---

## 👨‍💻 Author

**Shishir M S**  
 


