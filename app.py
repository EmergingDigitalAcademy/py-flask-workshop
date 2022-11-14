from flask import Flask

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return db
