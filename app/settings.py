from enum import Enum
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent


class DbSettings(str, Enum):
    DB_URI = 'application.db'
    DB_TABLES_SCRIPT = 'app/db_scripts/tables.sql'

    def __str__(self):
        return self.value
