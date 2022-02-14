import os
from flask import *
import json

app = Flask(__name__)

@app.route('/rafa', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Hello World! :D'}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__=="__main__":
    app.run()