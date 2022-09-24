import json
import sys

f = open('data/dogs.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

this_dog = [dog for dog in data if dog['name'] == "mika"]

name = this_dog[0]['name']
breed = this_dog[0]['breed']
birth_year = this_dog[0]['birth_year']
breed_string = ' '.join(breed)

key_values = name+'¬'+breed_string+'¬'+str(birth_year)
id = hash(key_values) % ((sys.maxsize + 1) * 2)

this_dog[0]['id'] = id

print(this_dog)