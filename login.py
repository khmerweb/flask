from flask import Blueprint, render_template, request
from db.user import user
user.createRootUser()
Login = Blueprint('Login', __name__)

@Login.route('/')
def home():
    data = {'message':""}
    return render_template("login.html", tdata = data)

@Login.route('/', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(email, password)

        return email