# 🏡 Bangalore Home Price Prediction Web App

A **Machine Learning–powered web application** built with **Flask**, designed to predict real estate prices across different locations in **Bangalore** based on square footage, number of bedrooms, and bathrooms.
This project combines **data preprocessing**, **model training**, and a **beautiful, modern web interface** for seamless real-time price prediction.

## ✨ Preview
![App Preview](banglore/preview/screenshot.jpg)

---

## 🚀 Features
- 💻 **Interactive Web Interface** – Simple, elegant, and premium UI built using HTML, CSS, and Flask templates.
- 🧠 **Machine Learning Model** – Trained using **Linear Regression** for accurate home price estimation.
- 📍 **Dynamic Location Dropdown** – Automatically loads all Bangalore locations from JSON data.
- 📊 **Real-Time Predictions** – Instantly predicts prices based on user input without reloading the page.
- 🖼️ **Property Slideshow** – Eye-catching property image carousel to give a realistic visual touch.
- 📈 **Scalable Backend** – Flask-based architecture ready for deployment on any cloud or hosting platform.

---

## 🧩 Tech Stack
- **Python 3.x**
- **Flask** (Backend Framework)
- **HTML5, CSS3, JavaScript** (Frontend)
- **NumPy, Pandas, scikit-learn** (Machine Learning)
- **Pickle** for model serialization

---

## ⚙️ How It Works
1. The model is trained on Bangalore housing dataset.
2. It uses key features: `total_sqft`, `bath`, `bhk`, and `location`.
3. Flask loads the model and column data from the `model/` folder.
4. The user enters property details, and the backend predicts the estimated home price.

---

## 🏗️ Project Structure
