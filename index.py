from flask import Blueprint, render_template

Index = Blueprint('index', __name__)

@Index.route('/')
def home():
    return render_template("Index.html", name="World")