from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np
import os
import random
from datetime import datetime, timedelta# ---------- Load model and columns ----------

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '../model/banglore_home_prices_model.pickle')
columns_path = os.path.join(base_dir, '../model/columns.json')

# Load model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load column data
with open(columns_path, 'r') as f:
    data_columns = json.load(f)['data_columns']

locations = data_columns[3:]  # all locations

# ---------- Flask App ----------

templates_dir = os.path.join(base_dir, '../templates')
app = Flask(__name__, template_folder=templates_dir)

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

@app.route('/')
def home():
    return render_template('app.html', locations=locations)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    location = data['location']
    sqft = float(data['sqft'])
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    estimated_price = predict_price(location, sqft, bath, bhk)
    return jsonify({'estimated_price': estimated_price})

@app.route('/api/forecast_sentiment', methods=['POST'])
def forecast_sentiment():
    data = request.get_json()
    location = data.get('location', 'Bangalore')
    current_price = float(data.get('current_price', 0))

    news_pool = [
        {"text": "Tech Park Expansion Announced Nearby", "impact": 0.02},
        {"text": "Minor Property Tax Increase Proposed", "impact": -0.01},
        {"text": "New Metro Line Approved", "impact": 0.03},
        {"text": "Local Road Repair Delays", "impact": -0.005},
        {"text": "Major Tech Company Relocating to Area", "impact": 0.04},
        {"text": "Water Supply Infrastructure Upgrade", "impact": 0.015},
        {"text": "Interest Rates Stabilize", "impact": 0.01},
        {"text": "New Commercial Mall Opens", "impact": 0.025},
        {"text": "Temporary Traffic Rerouting", "impact": -0.01},
        {"text": "Influx of Startup Talent in Region", "impact": 0.02}
    ]

    months = []
    prices = []
    headlines = []

    price = current_price
    today = datetime.now()

    for i in range(1, 7):
        target_date = today + timedelta(days=30*i)
        months.append(target_date.strftime("%B %Y"))
        
        num_news = random.randint(1, 2)
        monthly_news = random.sample(news_pool, num_news)
        
        month_impact = 0
        month_headline = []
        for n in monthly_news:
            month_impact += n["impact"]
            month_headline.append(n["text"])
            
        market_drift = random.uniform(-0.005, 0.01)
        total_growth = month_impact + market_drift
        
        price = price * (1 + total_growth)
        prices.append(round(price, 2))
        headlines.append(" | ".join(month_headline))

    return jsonify({
        "months": months,
        "prices": prices,
        "headlines": headlines
    })

if __name__ == "__main__":
    print("✅ Starting Flask Server for Bangalore Home Price Prediction...")
    app.run(debug=True)
