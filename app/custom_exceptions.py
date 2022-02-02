class DbOperationError(Exception):
    pass


class DataValidationError(Exception):
    pass


class DataSerializationError(Exception):
    pass


class IncorrectDatetimeFormatException(Exception):
    pass
