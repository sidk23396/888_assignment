from app.utils.db_delegator import DbDelegator
from app.models.base_model import BaseModel
from app.db import db_ch


class SportModel(BaseModel):
    _table_name = 'sport'
    _cols = ('id', 'name', 'slug', 'active')
    delegator = DbDelegator(_table_name, db_ch)

    # def __init__(self, name, slug, active, db_conn) -> None:
    #     self.name = name
    #     self.slug = slug
    #     self.active = active

    def format(self):
        return dict(self)

    # @classmethod
    # def to_db(cls, **data):
    #     # print(dir(cls.db_conn))
    #     # print(type(cls.db_conn))
    #     cls.delegator.db_conn_hand.create_row(cls._table_name, **data)
    #
    # @classmethod
    # def read_from_db(cls):
    #     all_rows = cls.delegator.db_conn_hand.get_all_rows(cls._table_name)
    #     print(all_rows[0])
    #     res = [cls.load_from_db_object(db_obj) for db_obj in all_rows]
    #     return res
    #
    # @classmethod
    # def load_from_db_object(cls, db_object):
    #     print(type(db_object))
    #     if isinstance(db_object, tuple) and len(cls._cols) == len(db_object):
    #         return dict(zip(cls._cols, db_object))
    #     else:
    #         raise Exception('Serialization error')
