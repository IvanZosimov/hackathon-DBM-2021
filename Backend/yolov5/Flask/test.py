from flask import Flask, jsonify
import sqlite3
from sqlite3 import Error
import json
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)


@app.route('/', methods=["GET"])
@cross_origin()
def hello_world():
    response = str(fetch_data())
    #response = jsonify(message=mess)
    #response.headers.add("Access-Control-Allow-Origin", "*")
    return response

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
    final_list = []
    for res in result:
        temp_dict = {
            'id': res[0],
            'url': rebuild_url(res[1]),
            'date': res[2],
            'inMask': res[3],
            'accuracy': res[4]
        }
        final_list.append(temp_dict)
    json_string = json.dumps(final_list)
    #print(json_string)
    # result = result.split(' ')
    # print(result[0])
    return json_string


def rebuild_url(url):
    raw_string = r''
    url_2 = url.replace('\\', '/')
    temp_list = url_2.split('static')
    #print(os.path.abspath(url))
    return 'http://127.0.0.1:5000/static' + temp_list[1]

if __name__ == '__main__':
    app.run()






