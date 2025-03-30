import pymssql
import pandas as pd

SERVER = "192.168.0.128"
DATABASE = "TRN"
USERNAME = "dbo_user"
PASSWORD = "@11dbo_user_for_RF"


class dbServicePymssql:
    def create_connection(self) -> pymssql.Connection:
        connection = pymssql.connect(
            server=SERVER,
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE,
            as_dict=True
        )
        return connection

    def execute_query(self, query) -> pd.DataFrame:
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return pd.DataFrame(data)
