import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../.."))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")

MODEL_DIR = BASE_DIR
MODEL_PATH = os.path.join(BASE_DIR, "pipe.pkl")
CITIES_PATH = os.path.join(BASE_DIR, "cities.txt")