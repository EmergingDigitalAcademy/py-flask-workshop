from flask import Flask, render_template, request, redirect, url_for, abort

from model import db, save_db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", tasks=db)


@app.route("/task/<int:index>")
def task_view(index):
    try:
        return render_template(
            "task.html", task=db[index], index=index, max_index=len(db) - 1
        )
    except IndexError:
        abort(404)


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task = {"name": request.form["name"]}
        db.append(task)
        save_db()
        return redirect(url_for("home", tasks=db))
    else:
        return render_template("add_task.html")


@app.route("/remove_task/<int:index>", methods=["GET", "POST"])
def remove_task(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for("home", tasks=db))
        else:
            return render_template("remove_task.html", task=db[index])
    except IndexError:
        abort(404)
