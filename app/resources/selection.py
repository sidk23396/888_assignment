from sqlite3 import DatabaseError

from flask import request
from flask_restful import Resource

from app.custom_exceptions import DataValidationError
from app.models.selection_model import SelectionModel
from app.utils.data_validator import validate_data
from app.utils.normalise_data_utils import to_upper, to_2_decimal_places
from app.utils.response_builder import response_builder


class Selection(Resource):
    def get(self):
        try:
            active_arg = request.args.get('active', None, type=int)
            event_name_arg = request.args.get('event_name', None, type=str)

            res = SelectionModel.get_all_from_db(active=active_arg, event_name=event_name_arg)
        except DatabaseError:
            return response_builder(message="Error: Unable to get the data.", status=500)
        else:
            return response_builder(status=200, data=res)

    def post(self):
        try:
            _post_schema = {
                "name": {"type": "string", "required": True},
                "event_name": {"type": "string", "required": True},
                "price": {"type": "float", "required": True, 'coerce': to_2_decimal_places},
                "active": {"type": "integer", "required": True, 'coerce': int},
                "outcome": {"type": "string", "required": True, "allowed": ("UNSETTLED", "VOID", "LOSE", "WIN"),
                            "coerce": to_upper},
            }
            body = request.get_json()
            _, validated_data = validate_data(_post_schema, body)
            SelectionModel.to_db(**validated_data)
        except DataValidationError as e:
            return response_builder(message=str(e), status=400)
        except DatabaseError:
            return response_builder(message="Error: Unable to store the data.", status=500)
        else:
            return validated_data, 200


class SpecificSelection(Resource):
    def get(self, name):
        try:
            res = SelectionModel.get_n_from_db(name=name, size=1)
            if not res:
                return response_builder(status=404)
        except DatabaseError:
            return response_builder(message="Error: Unable to get the data.", status=500)
        else:
            return response_builder(data=res, status=200)

    def patch(self, name):
        _schema = {
            "price": {"type": "float", "required": False, 'coerce': to_2_decimal_places},
            "active": {"type": "integer", "required": False, 'coerce': int},
            "outcome": {"type": "string", "required": False, "allowed": ("UNSETTLED", "VOID", "LOSE", "WIN"),
                        "coerce": to_upper},
        }
        try:
            body = request.get_json()
            if body:
                _, validated_data = validate_data(_schema, body)
                SelectionModel.update_in_db({'name': name}, **validated_data)
            else:
                return response_builder(status=400)
        except DataValidationError as e:
            return response_builder(message=str(e), status=400)
        except DatabaseError:
            return response_builder(message="Error: Unable to update the data.", status=500)
        else:
            return response_builder(status=204)
