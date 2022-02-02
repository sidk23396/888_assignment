from app import app
from argparse import ArgumentParser


def parse_args():
    args_parser = ArgumentParser('Parse arguments for flask server')
    args_parser.add_argument('--host', type=str, default='0.0.0.0', help='Host/IP to use for the server')
    args_parser.add_argument('--port', type=int, default=5001, help='Port to use for the server')
    args_parser.add_argument('--debug', action='store_true', default=False, help='Start app in debug mode')
    return args_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
