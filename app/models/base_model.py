from app.custom_exceptions import DataSerializationError


class BaseModel:
    @classmethod
    def to_db(cls, **data):
        cls.delegator.db_conn_hand.create_row(cls._table_name, **data)

    @classmethod
    def get_all_from_db(cls, **filters):
        all_rows = cls.delegator.db_conn_hand.get_all_rows(cls._table_name, **filters)
        res = [cls.load_from_db_object(db_obj) for db_obj in all_rows]
        return res

    @classmethod
    def get_n_from_db(cls, size, **filters):
        all_rows = cls.delegator.db_conn_hand.get_n_rows(cls._table_name, size, **filters)
        res = [cls.load_from_db_object(db_obj) for db_obj in all_rows]
        if size == 1 and res:
            return res[0]
        return res

    @classmethod
    def load_from_db_object(cls, db_object):
        if isinstance(db_object, tuple) and len(cls._cols) == len(db_object):
            return dict(zip(cls._cols, db_object))
        else:
            raise DataSerializationError('Serialization error')

    @classmethod
    def update_in_db(cls, match_condition, **data):
        cls.delegator.db_conn_hand.update(cls._table_name, match_condition, **data)
