from flask import Blueprint, render_template

Index = Blueprint('Index', __name__)

@Index.route('/')
def home():
    return "<p>Hello, World!</p>"