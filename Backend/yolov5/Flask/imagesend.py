from flask import Flask, request, send_from_directory
import os
#print(os.listdir('./runs/detect/exp155/crops/No_mask'))
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run()