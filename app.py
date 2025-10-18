# save this as app.py
from flask import Flask
from index import index

app = Flask(__name__)

app.register_blueprint(index, url_prefix='/')