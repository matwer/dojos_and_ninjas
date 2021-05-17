# this is the one side of the One to Many (one dojo has many ninjas)
from flask import render_template,redirect,request,session,flash

from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def home():
    return redirect("/dojos")


# CRUD

# Read All
@app.route("/dojos")
def index():
    dojos = Dojo.get_all_dojos()

    return render_template("dojos.html", all_dojos = dojos)


# Read One Dojo with associated ninjas
@app.route("/dojos/<int:dojo_id>")
def show_dojo(dojo_id):
    this_dojo = Dojo.get_dojo_with_ninjas( {"id": dojo_id } )

    return render_template("dojo_show.html", dojo = this_dojo)


# Create
@app.route("/dojo/create", methods = ["POST"])
def add_dojo():

    new_dojo = {
        "name": request.form['name']
    }
    print (new_dojo)

    Dojo.add_dojo(new_dojo)

    return redirect("/dojos")