import pyodbc
import pandas as pd

SERVER = "127.0.0.1"
DATABASE = "TRN"
USERNAME = "dbo_user"
PASSWORD = "@11dbo_user_for_RF"


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
