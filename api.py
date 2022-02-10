from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Hello World! :D'}
    json_dump = json.dumps(data_set)
    return json_dump

    
@app.route('/user/', methods=['GET'])
def request_page():

    user_query = str(request.args.get('user')) 

    data_set = {'Page': 'Request', 'Message': f'Hello, {user_query}! :D'}
    json_dump = json.dumps(data_set)
    return json_dump

if(__name__ == '__main__'):
    app.run(port=7777)