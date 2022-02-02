from flask import Flask
from flask_restful import Api

from app.resources.event import Events, SpecificEvent, EventStart
from app.resources.selection import Selection, SpecificSelection
from app.resources.sport import Sports, SpecificSport
from app.utils.response_builder import response_builder

app = Flask(__name__)
api = Api(app)

api.add_resource(Sports, '/sports')
api.add_resource(SpecificSport, '/sports/<name>')

api.add_resource(Events, '/events')
api.add_resource(SpecificEvent, '/events/<name>')
api.add_resource(EventStart, '/events/<name>/started')

api.add_resource(Selection, '/selections')
api.add_resource(SpecificSelection, '/selections/<name>')


@app.route('/healthz')
def healthz():
    return response_builder(message="alive", status=200)
