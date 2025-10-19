# save this as app.py
from flask import Flask
from index import frontend
from login import Login

app = Flask(__name__)

app.register_blueprint(frontend, url_prefix='/')
app.register_blueprint(Login, url_prefix='/login')