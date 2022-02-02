
from asyncio import events
from multiprocessing.dummy import active_children
from os import name

from app.utils.db_delegator import DbDelegator
from app.models.base_model import BaseModel
from app.db import db_ch


class SelectionModel(BaseModel):
    _table_name = 'selection'
    _cols = ('id', 'name', 'event', 'price', 'active', 'outcome')
    delegator = DbDelegator(_table_name, db_ch)

    def __init__(self, name, event, price, active, outcome) -> None:
        self.name = name
        self.event = event
        self.price = price # (Decimal value, to 2 decimal places)
        self.active = active # (Either true or false)
        self.outcome = outcome # (Unsettled, Void, Lose or Win)

    def format(self):
        return dict(self)

    # @classmethod
    # def to_db(cls, **data):
    #     cls.delegator.create_row(cls._table_name, **data)
    #
    # @classmethod
    # def read_from_db(cls):
    #     return cls.delegator.get_all_rows(cls._table_name)
