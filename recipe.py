# recipes.py
import json

DATA_FILE = "sample_data.json"

def load_recipes():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_recipes(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_recommendations(data, cuisine):
    return [name for name, info in data.items() if info.get("Cuisine", "").lower() == cuisine.lower()]

def search_recipe(data, query):
    results = {}
    for name, info in data.items():
        if query.lower() in name.lower():
            results[name] = info
    return results

def filter_recipes(data, difficulty, max_time, min_rating):
    results = []
    for name, info in data.items():
        if difficulty != "Any" and info.get("Difficulty") != difficulty:
            continue
        if info.get("Prep Time", 0) > max_time:
            continue
        if info.get("Rating", 0) < min_rating:
            continue
        results.append(name)
    return results

def add_recipe(data, name, details):
    data[name] = details

