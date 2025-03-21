import pyodbc
import pandas as pd

SERVER = "127.0.0.1"
DATABASE = "TRN"
USERNAME = "***"
PASSWORD = "***"


class dbService:
    def __init__(self):
        self.connectionString = (f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                                 f"SERVER={SERVER};"
                                 f"DATABASE={DATABASE};"
                                 f"UID={USERNAME};"
                                 f"PWD={PASSWORD}")

    def create_connection(self) -> pyodbc.Connection:
        connection = pyodbc.connect(self.connectionString)
        return connection

    def execute_query(self, query) -> pd.DataFrame:
        connection = self.create_connection()
        return pd.read_sql(query, connection)
