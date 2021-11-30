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

connection = create_connection("C:\\Users\\nikita.alexandrov\\Desktop\\db\\intruders.db")

cursor = connection.cursor()

# command1 = """CREATE TABLE IF NOT EXISTS
# persons(person_id INTEGER PRIMARY KEY, url TEXT, time TEXT, isInMask NUMERIC, accuracy REAL)"""

# cursor.execute(command1)
#
# cursor.execute("INSERT INTO persons VALUES (322, \'1.png', \'11-26-2021', 1, 0.83)")
# cursor.execute("INSERT INTO persons VALUES (333, \'2.png', \'11-26-2021', 1, 0.8)")
# cursor.execute("INSERT INTO persons VALUES (323, \'3.png', \'11-26-2021', 1, 0.7)")
# connection.commit()

cursor.execute("SELECT * FROM persons")

result = cursor.fetchall()
print(result)