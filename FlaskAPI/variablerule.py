# https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24

from flask import Flask
app = Flask(__name__)

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name
    
app.run()