import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

# NEW
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

# Latest model (used by API)
MODEL_PATH = os.path.join(BASE_DIR, "ml", "pipe.pkl")

CITIES_PATH = os.path.join(BASE_DIR, "ml", "cities.txt")