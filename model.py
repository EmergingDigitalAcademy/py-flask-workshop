import json


def load_db():
    with open("data.json") as d:
        return json.load(d)


def save_db():
    with open("data.json", "w") as f:
        return json.dump(db, f)


db = load_db()
