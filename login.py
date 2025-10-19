from flask import Blueprint, render_template

Login = Blueprint('login', __name__)

@Login.route('/')
def home():
    data = {'message':""}
    return render_template("Login.html", tdata = data)