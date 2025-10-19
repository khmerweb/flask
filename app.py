# save this as app.py
from flask import Flask
from index import Index
from login import Login

app = Flask(__name__)

app.register_blueprint(Index, url_prefix='/')
app.register_blueprint(Login, url_prefix='/login')