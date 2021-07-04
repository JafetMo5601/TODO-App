from flask import render_template

from . import home_bp


@home_bp.route("/")
def home():
    return "Hi!"
    # return render_template("index.html")
