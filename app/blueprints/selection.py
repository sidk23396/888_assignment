from flask import Blueprint

selection = Blueprint('selection', __name__)

@selection.route('/')
def hello_world():
    return "hello world! selection"