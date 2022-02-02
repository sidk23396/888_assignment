from cerberus import Validator
from app.custom_exceptions import DataValidationError


def validate_data(schema, data):
    v = Validator(schema=schema)
    v.allow_unknown = False
    if not v.validate(data, schema):
        raise DataValidationError(v.errors)
    return True, v.document
