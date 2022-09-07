##https://medium.com/analytics-vidhya/server-validation-in-flask-api-with-json-schema-963aa05e305f

from http.client import OK
from flask import Flask, jsonify, request,Response
from flask_api import status
import json
from flask_expects_json import expects_json

schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "email": { "type": "string" }
  },
  "required": ["email"]
}

app = Flask(__name__)

@app.route('/rescue/', methods=['GET','POST']) 
@expects_json(schema, ignore_for=['GET'])  

def rescue():

    if request.method == 'GET':
        # Opening JSON file
        f = open('rescue/rescue.json')
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)

        return jsonify(data)


    if request.method == 'POST':
   
        with open('rescue/rescue-1.json', 'w') as outfile:
            json.dump(request.json, outfile)
    content = 'Rescue-1 Added'
    return content, status.HTTP_200_OK

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)

## http://localhost:105/rescue/