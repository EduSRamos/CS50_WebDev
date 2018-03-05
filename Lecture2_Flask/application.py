#----------------------------->> 1. INTRO
# main file for a flask application
from flask import Flask, render_template

import datetime # for (6)

# "I want to create a new application and I want this application to be
# a flask web application"
# "__name__" represents *this* file, which represents my web application
# This creates a new variable that will be the source of this new application
# such that later I can tie specific functions to it.
app = Flask(__name__)

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
    return "Hello, world!"

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
