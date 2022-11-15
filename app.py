from flask import Flask, render_template, request, redirect, url_for, abort
from model import db, save_db

# Initializes the application using the Flask Object using the __name__ variable (pulls the name of the file)
# and stores into the app variable
app = Flask(__name__)


# @app.route is a decorator for the route function defined below it. app.route declares the url at which the
# route can be accessed. "/" is usually defined as the home route for a website and the browser will usually exclude
# it from the displayed URL. Ex: https://github.com/ or https://github.com
@app.route("/")
def home():
    # our route functions determine what the api will do when a request is sent from a client to the defined
    # url. Route functions HAVE to return SOMETHING

    # This function will return another function, render_template. render_template will take an HTML file as the first
    # argument, and any argument after is data that can be accessed within the HTML file, thanks to Jinja!
    # We are rendering the "home.html" file and giving it the db variable (which holds our data) to be stored and
    # accessed in HTML through the 'tasks' variable
    return render_template("home.html", tasks=db)


# app.route also accepts a second argument which determines what HTTP methods can access this route.
# All routes default to accepting "GET" requests, we want to send data to our client.
# This route also accepts a "POST" request, a request that is used to send data to the server
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    # If the request that is touching this endpoint is of the POST method, we want to access the form information that
    # was sent from the HTML client and is stored in the request object (imported from flask) and create a new
    # dictionary that we can add to our data model. We are calling save_db to actually write to the JSON object,
    # and redirecting the user to the home route with the updated database stored in the tasks variable
    if request.method == "POST":
        task = {"name": request.form["name"], "date": request.form["date"]}
        db.append(task)
        save_db()
        return redirect(url_for("home", tasks=db))
    # If the method is anything but "POST" (the other accepted method is a "GET" request) then render the add_task form
    else:
        return render_template("add_task.html")


# In the URL defined in app.route, we can add "URL Parameters" to the end of our url. We do that by including an extra
# "/" followed by the name of the parameter surrounded by "<" ">" signs. This parameter has a type declaration on it,
# saying that the piece of data inside the index parameter will be an integer. URL Parameters can be accessed in the
# route function by including the parameter name as an argument of the route function
@app.route("/remove_task/<int:index>", methods=["GET", "POST"])
def remove_task(index):
    # We are wrapping this block of code in a try / except because we want to make sure that the index provided in the
    # URL Parameter is an actual index that we have in our data model. If we are trying to access an index that is not
    # within our data model, we will receive an IndexError, and rather than breaking out of our code, we are catching
    # that error and returning to the client an abort page with the HTTP status code of 404
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for("home", tasks=db))
        else:
            return render_template("remove_task.html", task=db[index])
    except IndexError:
        abort(404)
