import json


# This function loads the data stored in the JSON file and returns it as a dictionary to be used in our code
def load_db():
    with open("data.json") as d:
        return json.load(d)


# This function will write changes made to the db object to our JSON data model
def save_db():
    with open("data.json", "w") as f:
        return json.dump(db, f)


db = load_db()
