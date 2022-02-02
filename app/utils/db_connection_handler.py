import sqlite3

from app.custom_exceptions import DbOperationError
from app.settings import PROJECT_ROOT, DbSettings


class DbConnectionHandler:
    def __init__(self, db_name, dry_run=False):
        self.db_name = db_name
        self.db_conn = self._get_db_connection()
        self.dry_run = dry_run

    def get_all_rows(self, table, **filters):
        query = f"""SELECT * FROM {table}"""
        params = None
        if filters and all([True for v in list(filters.values()) if v != None]):
            conditions = [f"""{c}=?""" for c, v in filters.items() if v != None]
            params = [v for _, v in filters.items() if v != None]

            if len(conditions) > 1:
                conditions = ' AND '.join(conditions)

            elif conditions:
                conditions = conditions[0]

            if conditions:
                query = f"""SELECT * FROM {table} WHERE {conditions}"""

        return self.run_sql_query(query, params)

    def get_n_rows(self, table, n, **filters):
        if filters:
            conditions = [f"""{c}='{v}'""" for c, v in filters.items()]
            if len(filters.items()) > 1:
                conditions = ' AND '.join(filters.items())
            else:
                conditions = conditions[0]
            query = f"""SELECT * FROM {table} WHERE {conditions}"""
        else:
            query = f"""SELECT * FROM {table}"""
        return self.run_sql_query(query, sized_result=n)

    def update(self, table, match_condition, **col_val_pairs):
        """
        Match conditions are paired with AND operator only. OR not supported
        :param table:
        :param match_condition: eg: {'name': 'football'} or {'active': 1}
        :type match_condition: dict
        :param col_val_pairs:
        :return:
        """
        match_cond = [f'{c} = ?' for c, _ in match_condition.items()]
        match_condition_vals = [v for _, v in match_condition.items()]
        update_col_val = [f'{c} = ?' for c, v in col_val_pairs.items()]
        update_vals = [v for _, v in col_val_pairs.items()]
        params = [*update_vals, *match_condition_vals, ]

        query = f"""UPDATE {table} SET {','.join(update_col_val)} WHERE {' AND '.join(match_cond)}"""
        return self.run_sql_query(query, params)

    def create_row(self, table, **data):

        cols = [key for key, _ in data.items()]
        vals = tuple([val for _, val in data.items()])

        query = f"""INSERT INTO {table} ({','.join(cols)}) VALUES {vals}"""
        return self.run_sql_query(query)

    def delete_with_conditions(self, table, **condition):
        keys = [f'{c} = ?' for c, v in condition.items()]
        values = tuple([v for c, v in condition.items()])

        if len(condition.items()) > 1:
            keys = ' AND '.join(keys)
        else:
            keys = keys[0]
        query = f"""DELETE FROM {table} WHERE {keys}"""

        return self.run_sql_query(query, values)

    def run_sql_query(self, query, params=None, sized_result=None):
        if self.dry_run:
            print('Dry run mode')
            print('SQL query to be executed: ', query)
            print('params ', params)
        else:
            try:
                cursor = self.db_conn.cursor()
                if params:
                    res = cursor.execute(query, params)
                else:
                    res = cursor.execute(query)
                self.db_conn.commit()

                if sized_result and isinstance(sized_result, int):
                    result_val = res.fetchmany(sized_result)
                else:
                    result_val = res.fetchall()
                cursor.close()
                return result_val

            except sqlite3.DatabaseError as e:
                raise DbOperationError(e)
        return True

    def _get_db_connection(self):
        try:
            db_conn = sqlite3.connect(self.db_name, check_same_thread=False)
            db_conn.execute("PRAGMA foreign_keys = 1")
            self.cursor = db_conn.cursor()
            print("Successfully Connected to SQLite")

            with open(f'{PROJECT_ROOT}/{DbSettings.DB_TABLES_SCRIPT}', 'r') as sqlite_file:
                sql_script = sqlite_file.read()

            self.cursor.executescript(sql_script)
            print("SQLite script executed successfully")
            self.cursor.close()

        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)

        return db_conn

    def close(self):
        self.db_conn.close()
