# REST API server for the Nano Node API
# Tested with Python 2.7.13 and Python 3.6.5
# Dependences: flask, nanoapi
import json
import os.path
from flask import Flask, request
from nanoapi import (Client, SocketConnection)

app = Flask(__name__)
global conn
global nano

@app.route('/api/<query>', methods=['POST'])
def api(query):

    try:
        query_obj = nano.from_json(query, request.data)
        if query_obj == None:
            return nano.to_json(nano.error_response(1, "Invalid message"))
        res = nano.request(query_obj)
        return nano.to_json(res)
    except Exception as e:
        return nano.to_json(nano.error_response_from_exception(e))

if __name__ == '__main__':

    # Set up defaults
    config_port = 8080
    config_connection = "local:///tmp/nano"

    if os.path.isfile("config.json"):
        with open("config.json") as json_file:
            json_data = json.load(json_file)
            config_port = json_data['port']
            config_connection = json_data['node']['connection']

    conn = SocketConnection(config_connection)
    nano = Client(conn)

    # If config port is zero, we're hosted in a production quality web server,
    # otherwise, start a debug server.
    if config_port == 0:
        app.run()
    else:
        app.run(debug=True, port=config_port)
