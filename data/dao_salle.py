import mysql.connector
import json

class DataSalle:

    def get_connection(sef):
        with open("Data/config.json","r") as f:
            config = json.load(f)

        conn=mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return conn
