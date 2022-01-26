from flask import Flask, Response
from app.blueprints.sport import sport
from app.blueprints.event import event 
from app.blueprints.selection import selection

app = Flask(__name__)

app.register_blueprint(sport, name='sport', url_prefix='/sport')
app.register_blueprint(event, name='event', url_prefix='/event')
app.register_blueprint(selection, name='selection', url_prefix='/selection')

@app.route('/healthz')
def healthz():
    return Response(status=200, response="alive")

print(app.url_map)