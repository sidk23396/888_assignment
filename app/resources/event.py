from sqlite3 import DatabaseError

from flask import request
from flask_restful import Resource

from app.custom_exceptions import DataValidationError, DbOperationError, IncorrectDatetimeFormatException
from app.models.event_model import EventModel
from app.utils.data_validator import validate_data
from app.utils.normalise_data_utils import to_datetime, normalise_name, to_upper
from app.utils.response_builder import response_builder


class Events(Resource):
    def get(self):
        try:
            active_arg = request.args.get('active', None, type=int)
            sport_arg = request.args.get('sport_name', None, type=str)
            status_arg = request.args.get('status', None, type=str)
            event_type_arg = request.args.get('event_type', None, type=str)

            res = EventModel.get_all_from_db(active=active_arg, sport_name=sport_arg, status=status_arg,
                                             event_type=event_type_arg)
        except DatabaseError:
            return response_builder(message="Error: Unable to get the data.", status=500)
        else:
            return response_builder(status=200, data=res)

    def post(self):
        try:
            _post_schema = {
                "name": {"type": "string", "required": True, "coerce": normalise_name},
                "slug": {"type": "string", "required": True},
                "active": {"type": "integer", "required": True, 'coerce': int},
                "sport_name": {"type": "string", "required": True},
                "event_type": {"type": "string", "required": True, "allowed": ("PREPLAY", "INPLAY"),
                               'coerce': to_upper},
                "status": {"type": "string", "required": True, "allowed": ("PENDING", "STARTED", "ENDED", "CANCELLED"),
                           'coerce': to_upper},
                "scheduled_start": {"type": "string", "required": True, 'coerce': to_datetime},
                "actual_start": {"type": "string", "required": False, 'coerce': to_datetime}
            }
            body = request.get_json()
            _, validated_data = validate_data(_post_schema, body)
            EventModel.to_db(**validated_data)
        except DbOperationError as e:
            return response_builder(message=str(e), status=409)
        except DataValidationError as e:
            return response_builder(message=str(e), status=400)
        except DatabaseError:
            return response_builder(message="Error: Unable to store the data.", status=500)
        else:
            return validated_data, 200


class SpecificEvent(Resource):
    def get(self, name):
        try:
            res = EventModel.get_n_from_db(name=name, size=1)
            if not res:
                return response_builder(status=404)
        except DatabaseError:
            return response_builder(message="Error: Unable to get the data.", status=500)
        else:
            return res, 200

    def patch(self, name):
        _schema = {
            "slug": {"type": "string", "required": False},
            "active": {"type": "integer", "required": False, 'coerce': int},
            "event_type": {"type": "string", "required": False, "allowed": ("PREPLAY", "INPLAY"),
                           'coerce': to_upper},
            "status": {"type": "string", "required": False, "allowed": ("PENDING", "STARTED", "ENDED", "CANCELLED"),
                       'coerce': to_upper},
            "scheduled_start": {"type": "string", "required": False, 'coerce': to_datetime}
        }
        try:
            body = request.get_json()
            if body:
                _, validated_data = validate_data(_schema, body)
                EventModel.update_in_db({'name': name}, **validated_data)
            else:
                return response_builder(status=400)
        except IncorrectDatetimeFormatException as e:
            return response_builder(message=str(e), status=400)
        except DataValidationError as e:
            return response_builder(message=str(e), status=400)
        except DatabaseError:
            return response_builder(message="Error: Unable to update the data.", status=500)
        else:
            return response_builder(status=204)


class EventStart(Resource):
    def post(self, name):
        try:
            from datetime import datetime
            data = {"actual_start": datetime.utcnow(),
                    "status": "STARTED"}
            EventModel.update_in_db({'name': name}, **data)
        except DatabaseError:
            return response_builder(message="Error: Unable to update the data.", status=500)
        else:
            return response_builder(status=204)
