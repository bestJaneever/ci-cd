import os
import pyodbc
from robot.api.deco import library, keyword

DB_SERVER = "127.0.0.1"
DB_DATABASE = "TRN"
DB_USERNAME = "***"
DB_PASSWORD = "***"


@library(scope='GLOBAL', auto_keywords=True)
class DatabaseService:
    def __init__(self):
        self.connectionString = (f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                                 f'SERVER={DB_SERVER};'
                                 f'DATABASE={DB_DATABASE};'
                                 f'UID={DB_USERNAME};'
                                 f'PWD={DB_PASSWORD}')

    def create_db_connection(self) -> pyodbc.Connection:
        connection = pyodbc.connect(self.connectionString)
        return connection

    @keyword
    def execute_query(self, query: str):
        connection = self.create_db_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

