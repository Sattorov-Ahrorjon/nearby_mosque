import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id int,
            name VARCHAR(255),
            selection VARCHAR(255),
            text VARCHAR(400),
            PRIMARY KEY (id)
            );
    """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, pk: int, name: str):
        sql = "INSERT INTO Users(id, name) VALUES(?, ?)"
        self.execute(sql, parameters=(pk, name), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users;
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def get_selection(self, pk):
        sql = """
        SELECT selection FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(pk,), fetchone=True)

    def update_user_selection(self, selection, pk):
        sql = f"""
        UPDATE Users SET selection=? WHERE id=?
        """

        return self.execute(sql, parameters=(selection, pk), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def add_text(self, text, pk):
        sql = """
        UPDATE Users SET text=? WHERE id=?
        """
        return self.execute(sql, parameters=(text, pk), commit=True)

    def get_user(self, pk):
        sql = """
        SELECT * FROM Users WHERE id=?
        """
        return self.execute(sql, parameters=(pk,), fetchone=True)

    def get_id(self):
        sql = """
        SELECT id FROM Users;
        """
        return self.execute(sql, fetchall=True)


def logger(statement):
    print(f"""
----------------------------------------------------
Executing:
{statement}
----------------------------------------------------
""")
