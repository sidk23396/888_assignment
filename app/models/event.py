

from os import name

from app.utils.db_delegator import DbDelegator


class Event:
    table_name = 'event'
    delegator = DbDelegator(table_name=table_name)
    
    def __init__(self, name, slug, active, event_type, sport, status, scheduled_start, actual_start) -> None:
        self.name = name
        self.slug = slug
        self.active = active
        self.event_type = event_type
        self.sport = sport
        self.status = status # (Pending, Started, Ended or Cancelled)
        self.scheduled_start = scheduled_start # (UTC datetime)
        self.actual_start = actual_start # (created at the time the event has the status changed to "Started")
