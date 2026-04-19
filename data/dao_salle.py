from logging import exception

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

    def insert_salle(self,salle):
        conn=self.get_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO salle VALUES (%s,%s,%s,%s)",
                       (salle.code,salle.description,salle.categorie,salle.capacite))
        conn.commit()
        conn.close()
        print(f"salle ajoutee")

    def update_salle(self,salle):
        conn=self.get_connection()
        cursor=conn.cursor()
        cursor.execute("UPDATE salle SET description=%s,categorie=%s,capacite=%s WHERE code=%s",
                   (salle.description,salle.code,salle.categorie,salle.capacite))
        conn.commit()
        conn.close()

        print(f"salle modifiee")
    def delete_salle(self,salle):
        conn=self.get_connection()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM salle WHERE code=%s",(code,))
        conn.commit()
        conn.close()
        print(f"salle suprimee")

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salle")
        rows = cursor.fetchall()
        conn.close()
        return rows




