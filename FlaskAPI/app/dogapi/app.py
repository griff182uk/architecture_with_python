from flask import Flask, jsonify,request
import json
from flask_expects_json import expects_json
import sys

app = Flask(__name__)
 
schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "breed": { "type": "array" },
    "birth_year": { "type": "integer" },
    "birth_month": { "type": "integer" },
    "birth_day": { "type": "integer" },
    "microchip_id": { "type": "string" }
  },
  "required": ["name","breed","birth_year"]
}

@app.route('/dogs/', methods=['GET','POST']) 
@expects_json(schema, ignore_for=['GET'])  
def dogs():
    if request.method == 'GET':
    # Opening JSON file
        f = open('data/dogs.json')
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)

        return jsonify(data)

    if request.method == 'POST':
        filename = 'data/dogs.json'
        new_dog = request.json
        name = new_dog['name']
        breed = new_dog['breed']
        birth_year = new_dog['birth_year']
        breed_string = ' '.join(breed)

        key_values = name+'/'+breed_string+'/'+str(birth_year)
        id = hash(key_values) % ((sys.maxsize + 1) * 2)

        new_dog['id'] = id
        with open(filename) as outfile:
            dogs = json.load(outfile)
            if new_dog not in dogs:
                dogs.append(new_dog)
                with open(filename, 'w') as json_file:
                    json.dump(dogs, json_file, 
                                        indent=4,  
                                        separators=(',',': '))
                    content = 'Dog Added'
            else:
                content = 'Dog already exists'

        return content

@app.route('/dogs/<name>', methods=['GET','PUT']) 
@expects_json(schema, ignore_for=['GET'])  
def dog(name):
    if request.method == 'GET':
    # Opening JSON file
        f = open('data/dogs.json')
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)

        dog = [dog for dog in data if dog['name'] == name]

        return jsonify(dog)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

##http://127.0.0.1:5000/dogs/