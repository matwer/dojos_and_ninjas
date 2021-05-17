# this is the many side of the One to Many (many ninjas in one dojo)
from flask import render_template,redirect,request,session,flash

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas/new")
def new_ninja_form():
    # ninjas are associated with a dojo, so you need to get the list of dojos when creating a new ninja and pass that list in to the form 
    dojos = Dojo.get_all_dojos()

    return render_template("new_ninja.html", all_dojos = dojos)

@app.route("/ninjas/create", methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)

    return redirect ("/")


