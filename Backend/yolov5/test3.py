

import sqlite3
from sqlite3 import Error
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def fetch_data():
    connection = create_connection("C:\\Users\\nikita.alexandrov\\Desktop\\db\\intruders.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM persons")
    result = cursor.fetchall()
    print(result)
    return result

if __name__ == '__main__':
    fetch_data()