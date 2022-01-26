from flask import Blueprint

sport = Blueprint('sport', __name__)

@sport.route('/')
def hello_world():
    return "hello world! sport"

