from app.custom_exceptions import DbOperationError
from app.models.event_model import EventModel
from app.models.selection_model import SelectionModel
from app.models.sport_model import SportModel


def disable_events_for_disabled_sports():
    try:
        sports = SportModel.get_all_from_db()
        if sports:
            for sport in sports:
                sport_name = sport['name']
                sport_active = sport['active']
                deactivate_sport = False
                if sport_active != 0:   # only check if sport should be deactivated if it is active in the first place
                    events_for_sport = EventModel.get_all_from_db(sport_name=sport_name)
                    for event in events_for_sport:
                        if event['active'] == 0:
                            deactivate_sport = True
                            break
                if deactivate_sport:
                    SportModel.update_in_db({'name': sport_name}, active=0)
    except DbOperationError as e:
        print('Error occurred during housekeeping activity: ', str(e))


def disable_event_for_disabled_selections():
    try:
        events = EventModel.get_all_from_db()
        if events:
            for event in events:
                event_name = event['name']
                event_active = event['active']
                deactivate_event = False
                if event_active != 0:  # only check if event should be deactivated if it is active in the first place
                    selection_for_events = SelectionModel.get_all_from_db(event_name=event_name)
                    for selection in selection_for_events:
                        if selection['active'] != 1:
                            deactivate_event = True
                            break
                if deactivate_event:
                    EventModel.update_in_db({'name': event_name}, active=0)
    except DbOperationError as e:
        print('Error occurred during housekeeping activity: ', str(e))
