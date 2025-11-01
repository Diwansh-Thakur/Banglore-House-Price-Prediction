from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np
import os

# ---------- Load model and columns ----------

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
import os
from flask import Flask

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  

TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "templates")  
STATIC_DIR = os.path.join(BASE_DIR, "..", "static")       
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

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

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    location = data['location']
    sqft = float(data['sqft'])
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    estimated_price = predict_price(location, sqft, bath, bhk)
    return jsonify({'estimated_price': estimated_price})

if __name__ == "__main__":
    print("✅ Starting Flask Server for Bangalore Home Price Prediction...")
    if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


