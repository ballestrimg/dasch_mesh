from ..app import app
from flask import render_template

@app.route("/home_test")
def teste():
    return render_template("pages/home_test.html")
