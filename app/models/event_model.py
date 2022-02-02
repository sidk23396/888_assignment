from app.utils.db_delegator import DbDelegator
from app.models.base_model import BaseModel
from app.db import db_ch


class EventModel(BaseModel):
    _table_name = 'event'
    _cols = ('id', 'name', 'slug', 'active', 'event_type', 'sport_name', 'status', 'scheduled_start', 'actual_start')
    delegator = DbDelegator(_table_name, db_ch)
    
    def __init__(self, name, slug, active, event_type, sport, status, scheduled_start, actual_start) -> None:
        self.name = name
        self.slug = slug
        self.active = active
        self.event_type = event_type
        self.sport_name = sport
        self.status = status # (Pending, Started, Ended or Cancelled)
        self.scheduled_start = scheduled_start # (UTC datetime)
        self.actual_start = actual_start # (created at the time the event has the status changed to "Started")

    def format(self):
        return dict(self)

    # @classmethod
    # def to_db(cls, **data):
    #     cls.delegator.create_row(cls._table_name, **data)
    #
    # @classmethod
    # def read_from_db(cls):
    #     return cls.delegator.get_all_rows(cls._table_name)
