from flask import Blueprint, render_template
from db.user import user

Login = Blueprint('Login', __name__)

@Login.route('/')
def home():
    data = {'message':""}
    return render_template("login.html", tdata = data)