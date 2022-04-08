#!/usr/bin/env python3

from flask import Flask, request
from requests import get
import os

app = Flask(__name__)

@app.route("/api/list_files")
def list_files():
    d = request.args.get('directory')
    return '\n'.join(os.listdir(d))

@app.route("/api/read_file")
def read_file():

    # To prevent people from the Internet reading files :D
    if request.remote_addr != '127.0.0.1':
        return 'Uk9UMTM6dWdnY2Y6Ly9qamoubGJoZ2hvci5wYnovam5ncHU/aT1xRGo0ajlKdEtwRA=='

    p = request.args.get('path')
    with open(p, 'r') as f:
        return f.read()

@app.route("/api/get_request")
def get_request():
    u = request.args.get('url')
    return get(u).text

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=1337)


