from sqlite3 import DatabaseError

from flask import request
from flask_restful import Resource

from app.custom_exceptions import DataValidationError, DbOperationError
from app.models.sport_model import SportModel
from app.utils.data_validator import validate_data
from app.utils.normalise_data_utils import normalise_name
from app.utils.response_builder import response_builder


class Sports(Resource):
    def get(self):
        try:
            active_arg = request.args.get('active', None, type=int)
            res = SportModel.get_all_from_db(active=active_arg)
        except DatabaseError:
            return response_builder(message="Error: Unable to get the data.", status=500)
        else:
            return response_builder(status=200, data=res)

    def post(self):
        try:
            _post_schema = {
                "name": {"type": "string", "required": True, "coerce": normalise_name},
                "slug": {"type": "string", "required": True},
                "active": {"type": "integer", "required": True, 'coerce': int}
            }
            body = request.get_json()
            _, validated_data = validate_data(_post_schema, body)
            SportModel.to_db(**validated_data)
        except DataValidationError as e:
            return response_builder(message=str(e), status=400)
        except DbOperationError as e:
            return response_builder(message=str(e), status=409)
        except DatabaseError:
            return response_builder(message="Error: Unable to store the data.", status=500)
        else:
            return response_builder(data=validated_data, status=200)


class SpecificSport(Resource):
    def get(self, name):
        try:
            res = SportModel.get_n_from_db(name=name, size=1)
            if not res:
                return response_builder(status=404)
        except DatabaseError:
            return response_builder(message="Error: Unable to get the data.", status=500)
        else:
            return response_builder(data=res, status=200)

    def patch(self, name):
        _schema = {
            "slug": {"type": "string", "required": False},
            "active": {"type": "integer", "required": False, 'coerce': int}
        }
        try:
            body = request.get_json()
            if body:
                _, validated_data = validate_data(_schema, body)
                SportModel.update_in_db({'name': name}, **validated_data)
            else:
                return response_builder(status=400)
        except DataValidationError as e:
            return response_builder(message=str(e), status=400)
        except DatabaseError:
            return response_builder(message="Error: Unable to update the data.", status=500)
        else:
            return response_builder(status=204)
