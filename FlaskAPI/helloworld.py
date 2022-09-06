# https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24

import json
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.before_request
def before():
    print("Pretend MI...")
    print(json.dumps(dict(request.headers)))

@app.route('/hello/', methods=['GET', 'POST'])

def welcome():
    return "Hello World!"

@app.route('/person/')
def hello():
    return jsonify({'name':'Griff',
                    'address':'Wales',
                    'phone':'999'})

@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))

@app.route('/teapot/')
def teapot():
    return "Would you like some tea?", 418

app.logger.debug('This is a DEBUG message')
app.logger.info('This is an INFO message')
app.logger.warning('This is a WARNING message')
app.logger.error('This is an ERROR message')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)