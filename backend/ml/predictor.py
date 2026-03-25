import pickle
import pandas as pd
import os

# Model path
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'pipe.pkl')

# Load model once (global)
def load_model():
    try:
        with open(MODEL_PATH, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        raise Exception(f"Error loading model: {e}")

model = load_model()


def predict_win(batting_team, bowling_team, city,
                runs_left, balls_left, wickets, target):
    try:
        input_df = pd.DataFrame([{
            'batting_team': batting_team,
            'bowling_team': bowling_team,
            'city': city,
            'runs_left': runs_left,
            'balls_left': balls_left,
            'wickets': wickets,
            'target': target
        }])

        prediction = model.predict_proba(input_df)[0]

        return {
            "win_prob": round(prediction[1] * 100, 2),
            "lose_prob": round(prediction[0] * 100, 2)
        }

    except Exception as e:
        return {"error": str(e)}