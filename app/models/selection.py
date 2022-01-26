
from asyncio import events
from multiprocessing.dummy import active_children
from os import name

from app.utils.db_delegator import DbDelegator


class Selection:
    table_name = 'selection'
    delegator = DbDelegator(table_name=table_name)
    def __init__(self, name, event, price, active, outcome) -> None:
        self.name = name
        self.event = event
        self.price = price # (Decimal value, to 2 decimal places)
        self.active = active # (Either true or false)
        self.outcome = outcome # (Unsettled, Void, Lose or Win)
