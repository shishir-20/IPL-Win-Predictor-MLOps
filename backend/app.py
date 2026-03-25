from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ML_DIR = os.path.join(BASE_DIR, "ml")

sys.path.append(ML_DIR)

from predictor import predict_win

app = Flask(__name__)
CORS(app)


# Home route
@app.route('/')
def home():
    return jsonify({"message": "IPL Win Predictor Backend is running"})


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        required_fields = [
            'batting_team', 'bowling_team', 'city',
            'runs_left', 'balls_left', 'wickets', 'target'
        ]

        # Check missing fields
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        result = predict_win(
            data['batting_team'],
            data['bowling_team'],
            data['city'],
            int(data['runs_left']),
            int(data['balls_left']),
            int(data['wickets']),
            int(data['target'])
        )

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Cities route
@app.route('/cities', methods=['GET'])
def get_cities():
    try:
        cities_path = os.path.join(ML_DIR, 'cities.txt')

        with open(cities_path, 'r') as f:
            cities = [line.strip() for line in f.readlines()]

        return jsonify(cities)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)