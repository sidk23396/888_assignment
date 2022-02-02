from argparse import ArgumentParser

from flask_apscheduler import APScheduler

from app import app
from app.db import db_ch
from app.utils.housekeeping import disable_events_for_disabled_sports, disable_event_for_disabled_selections


def parse_args():
    args_parser = ArgumentParser('Parse arguments for flask server')
    args_parser.add_argument('--host', type=str, default='0.0.0.0', help='Host/IP to use for the server')
    args_parser.add_argument('--port', type=int, default=5001, help='Port to use for the server')
    args_parser.add_argument('--debug', action='store_true', default=False, help='Start app in debug mode')
    return args_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    scheduler = APScheduler()
    db_ch # to initialize the db before the app starts
    try:
        scheduler.add_job(id='update events for sports', func=disable_events_for_disabled_sports, trigger='interval',
                          seconds=60, jitter=5)
        scheduler.add_job(id='update selections for events', func=disable_event_for_disabled_selections,
                          trigger='interval',
                          seconds=71, jitter=5)
        scheduler.start()
        app.run(host=args.host, port=args.port, debug=args.debug)
    except KeyboardInterrupt as e:
        scheduler.shutdown(wait=True)
        db_ch.close()
