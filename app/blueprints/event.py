from flask import Blueprint

event = Blueprint('event', __name__)

@event.route('/')
def hello_world():
    return "hello world! event"