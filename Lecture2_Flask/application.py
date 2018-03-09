#----------------------------->> 1. INTRO
# main file for a flask application
from flask import Flask, render_template, request, session, url_for
from flask_session import Session # for (10)

import datetime # for (6)

# "I want to create a new application and I want this application to be
# a flask web application"
# "__name__" represents *this* file, which represents my web application
# This creates a new variable that will be the source of this new application
# such that later I can tie specific functions to it.
app = Flask(__name__)

#----------------------------->> [extra] got it off the internet - doesn't work
# @app.route("/")
# def site_map():
#     links = []
#     for rule in app.url_map.iter_rules():
#         # Filter out rules we can't navigate to in a browser
#         # and rules that require parameters
#         if "GET" in rule.methods:
#             url = url_for(rule.endpoint)
#             links.append((url, rule.endpoint))
#     # links is now a list of url, endpoint tuples
#     return render_template("all_links.html", links=links)

#----------------------------->> 2. DEFAULT PAGE
# Flask is designed in terms of routes; a ROUTE is just a part of the url
# that you type in in order to determine which page you want to request.
# Then, the slash below just represents the default page. If I go to my
# website and write www.<name_of_website>.com/ , that is the default page
# of the website.
# The line below says: "when the user goes to the default page, the function
# below is the one that I want to run"
@app.route("/")
def index(): # I'm tying this function to the "/"
    return "Hello, world! Go to /forms"

#----------------------------->> 3. ADD ROUTE
@app.route("/david") #[note] I think this takes precedence to the one below
def david():
    return "Hello, David!"

#----------------------------->> 4. GENERIC INPUT / HARD-CODED HTML
@app.route("/<string:name>")
def hello(name):
    # print("Ola") #[note] this appears on the terminal
    name = name.capitalize()
    return f"<h1 style=\"color:blue\">Hello, {name}!</h1>"

#----------------------------->> 5. HTML IN A SEPARATE FILE
# Tell flask to use the html files that we've already created to send something
# back to the user
# The .html files have to be inside a "Templates" directory
# Function "render_template":
#
@app.route("/html/example/1")
def htmlex1():
    return render_template("lec1.html") # there are some weird things happening

@app.route("/html/example/2")
def htmlex2():
    headline = "Hello, World;"
    # "In addition to returning the .html, I want the variable headline to be
    # defined in the .html to be whatever my variable headline is equal to"
    return render_template("lec2.html", headline=headline)

@app.route("/html/example/2/bye")
def htmlex2bye():
    headline = "Goodbye;"
    return render_template("lec2.html", headline=headline)

#----------------------------->> 6. MORE ADVANCED CONTROLS IN PYTHON
@app.route("/html/isitnewyear")
def isitnewyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("lec2.html", new_year=new_year)

@app.route("/html/loops")
def loops():
    names = {"name1": "Alice", "name2": "Bob", "name3": "Mallory"}
    # names = ("Alice", "Bob", "Mallory")
    return render_template("lec2.html", names=names)

#----------------------------->> 7. LINKING DIFFERENT PARTS OF APPLICATION
# For example, route A that links to route B, but B needs to link back to A
# In the html, add <a href="{{ url_for('B') }}">See here</a>
@app.route("/html/routes/A")
def linkAB():
    return render_template("lec2.html", names={"k": "<my_name>"},
                                        new_year=True, route="A")

@app.route("/html/routes/B")
def linkBA():
    return render_template("lec2.html", names={"k": "<my_name>"},
                                        new_year=True, route="B")

#----------------------------->> 8. Template Inheritance
# Used for pages which are very similar
# SEE layout.html, inherit1.html, inherit2.html
@app.route("/template-inheritance/first")
def inherit1():
    return render_template("inherit1.html")

@app.route("/template-inheritance/second")
def inherit2():
    return render_template("inherit2.html")

#----------------------------->> 9. Forms
# Now that we have a back-end server, we can start doing useful things with
# data submitted by users
# SEE
@app.route("/forms")
def forms():
    return render_template("lec2.html")

# from flask import request
#   will represent whatever request the user has made to my web server
# I'm telling the route: here's the request method you should accept. People
#   will submit data to this route via the post method to the whatsup function
# If sb tries to go to the route on the browser (GET), it'll show "Method Not
#   Allowed"
@app.route("/forms/whatsup", methods=["POST"])
def whatsup():
    # take the request the user made, access the form, and get the part of the
    # form called "name"
    if request.method == "GET": # it is never going to be true; just an example
        return "Please submit the form instead."
    # Search for form whose field "name" of <input> is equal to "usrname"
    name = request.form.get("usrname")
    return render_template("whatsup.html", name=name, notes=["go to forms"])

# WHEN YOU SUBMIT DATA VIA A GET-REQUEST, THAT DATA IS PUT IN THE URL

#----------------------------->> 10. Sessions
# Store information for later, for example
# Data-specific to your user account

# from flask import session - let's me keep user-specific data
# from flask_session import Session - additional extension to flask
#   let's us store session on "server-side" (on our server we're storing all
#   the data from the session, which gives us more control)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# notes = [] # Global - could be seen accross users (this is why we import
             #          'session')

@app.route("/session", methods=["GET", "POST"])
def sessionfun():
    if session.get("notes") is None:
        #I want my PARTICULAR session to have a list of notes
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("new_note")
        # notes.append(note)
        session["notes"].append(note)
    return render_template("whatsup.html", name="User", notes=session["notes"])
