def response_builder(status, message=None, data=None):
    if message or message == "":
        return {'message': message}, status
    if data or data == []:
        return data, status
    return "", status
