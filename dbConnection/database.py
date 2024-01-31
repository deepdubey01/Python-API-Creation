import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = cls._instance._create_connection()
        return cls._instance

    def _create_connection(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mataji@786",
                database="pythonLearning"
            )
            if conn.is_connected():
                print("Connected to MySQL database")
                return conn
        except Error as e:
            print("Error:", e)

    def get_connection(self):
        return self._connection

    def close_connection(self):
        if self._connection:
            self._connection.close()
