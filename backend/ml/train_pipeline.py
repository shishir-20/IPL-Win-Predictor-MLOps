import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# ✅ NEW IMPORTS
from config import DATA_DIR, MODEL_PATH, CITIES_PATH
from utils.logger import get_logger

from datetime import datetime
from config import DATA_DIR, MODEL_PATH, CITIES_PATH, MODEL_DIR

logger = get_logger()


# 1️⃣ Load Data
def load_data():
    matches = pd.read_csv(os.path.join(DATA_DIR, 'matches.csv'))
    deliveries = pd.read_csv(os.path.join(DATA_DIR, 'deliveries.csv'))
    return matches, deliveries


# 2️⃣ Preprocess Data
def preprocess(matches, deliveries):
    matches = matches[['id', 'city', 'winner']]

    deliveries = deliveries.merge(matches, left_on='match_id', right_on='id')

    total_runs = deliveries.groupby(['match_id', 'inning'])['total_runs'].sum().reset_index()
    total_runs = total_runs[total_runs['inning'] == 1]
    total_runs.rename(columns={'total_runs': 'target'}, inplace=True)

    deliveries = deliveries.merge(
        total_runs[['match_id', 'target']],
        on='match_id'
    )

    deliveries = deliveries[deliveries['inning'] == 2]

    deliveries['current_score'] = deliveries.groupby('match_id')['total_runs'].cumsum()
    deliveries['runs_left'] = deliveries['target'] - deliveries['current_score']

    deliveries['balls_left'] = 120 - (
        deliveries['over'] * 6 + deliveries['ball']
    )

    deliveries['wickets'] = 10 - deliveries.groupby('match_id')['player_dismissed'].transform(
        lambda x: x.notnull().cumsum()
    )

    deliveries = deliveries[deliveries['balls_left'] > 0]

    deliveries['result'] = deliveries.apply(
        lambda row: 1 if row['batting_team'] == row['winner'] else 0,
        axis=1
    )

    final_df = deliveries[[
        'batting_team',
        'bowling_team',
        'city',
        'runs_left',
        'balls_left',
        'wickets',
        'target',
        'result'
    ]]

    # ✅ FIXED WARNING
    final_df = final_df.dropna()

    return final_df


# 3️⃣ Train Model
def train_model(df):
    X = df.drop('result', axis=1)
    y = df['result']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    trf = ColumnTransformer(
        [
            ('trf', OneHotEncoder(sparse_output=False, drop='first'),
             ['batting_team', 'bowling_team', 'city'])
        ],
        remainder='passthrough'
    )

    # ✅ WITH SCALING
    pipe = Pipeline([
        ('transformer', trf),
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(max_iter=2000))
    ])

    pipe.fit(X_train, y_train)

    return pipe


def save_model(pipe, df):
    # Save latest model (for API)
    pickle.dump(pipe, open(MODEL_PATH, 'wb'))

    # Save versioned model
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    versioned_path = os.path.join(MODEL_DIR, f"model_{timestamp}.pkl")

    pickle.dump(pipe, open(versioned_path, 'wb'))

    logger.info(f"Versioned model saved at {versioned_path}")

    # Save cities
    cities = sorted(df['city'].unique())

    with open(CITIES_PATH, 'w') as f:
        for city in cities:
            f.write(city + '\n')


# 5️⃣ Run Full Pipeline
def run_pipeline():
    logger.info("🚀 Starting Training Pipeline...")

    try:
        matches, deliveries = load_data()
        logger.info("Data loaded successfully")

        df = preprocess(matches, deliveries)
        logger.info("Data preprocessing completed")

        model = train_model(df)
        logger.info("Model training completed")

        save_model(model, df)
        logger.info("Model and cities saved successfully")

        logger.info("✅ Training Completed Successfully!")

    except Exception as e:
        logger.error(f"Error in pipeline: {e}")
        raise e


# Run
if __name__ == "__main__":
    run_pipeline()