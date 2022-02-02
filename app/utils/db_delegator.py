class DbDelegator:
    def __init__(self, table_name, db_conn_hand) -> None:
        self.table_name = table_name
        self.db_conn_hand = db_conn_hand
