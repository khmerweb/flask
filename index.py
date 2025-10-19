from flask import Blueprint, render_template

Index = Blueprint('Index', __name__)
#test
@Index.route('/')
def home():
    return render_template("index.html", name="World")