from app.settings import DbSettings
from app.utils.db_connection_handler import DbConnectionHandler

db_ch = DbConnectionHandler(DbSettings.DB_URI)
db_conn = db_ch.db_conn
