from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__)
#test
@frontend.route('/')
def home():
    return render_template("index.html", name="World")