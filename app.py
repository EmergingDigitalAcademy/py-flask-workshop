from flask import Flask, render_template, redirect

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/add_card", methods=["GET", "POST"])
def add_card(index):
    return db


@app.route("/remove_card", methods=["GET", "POST"])
def remove_card(index):
    return db
