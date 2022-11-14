import json


def load_db():
    with open("data.json") as d:
        return json.load(d)


db = load_db()
