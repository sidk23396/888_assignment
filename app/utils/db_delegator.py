from utils.db_connection_handler import DbConnectionHandler

class DbDelegator(DbConnectionHandler):
    def __init__(self, table_name) -> None:
        self.table_name = table_name
        super().__init__()