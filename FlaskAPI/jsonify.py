from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/rescue/')
def hello():
    return jsonify({
    "guid": "e9ac950f-5779-4c9b-ad2c-0abeef270cf0",
    "name": "Blue Cross",
    "adch_status": "Full",
    "website": {
        "guid": "b1524ed1-d6ee-4e9f-968a-55513de9ceda",
        "address": "www.bluecross.org.uk",
        "urls": {
            "dogs": "https://www.bluecross.org.uk/rehome/dog",
            "dog": "https://www.bluecross.org.uk/pet/{name}-{number}",
            "cats": "https://www.bluecross.org.uk/rehome/cat",
            "cat": "https://www.bluecross.org.uk/pet/{name}-{number}",
            "contact": ""
        }
    },
    "contact": {
        "email": "",
        "telephone": "",
        "address": "Shilton Road, Burford, Oxfordshire",
        "postcode": "OX18 4PF",
        "lat": "",
        "lng": ""
    },
    "kennels": [
        {
            "guid": "43a23f56-c7e8-4ea8-b312-98cc672ba517",
            "name": "Blue Cross Bromsgrove",
            "contact": {
                "email": "bromsgrove@bluecross.org.uk",
                "telephone": "0300 777 1460",
                "address": "Wildmoor Lane, Catshill, Bromsgrove",
                "postcode": "B61 0R",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "aa0f2fb6-92da-47b8-a8e8-5058a7e73f8a",
            "name": "Blue Cross Suffolk",
            "contact": {
                "email": "suffolk@bluecross.org.uk",
                "telephone": "0300 777 1480",
                "address": "Bourne Hill, Wherstead, Ipswich",
                "postcode": "IP2 8NQ",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "33547fe5-cd9e-4b45-8e4c-683c988bc127",
            "name": "Blue Cross Sheffield",
            "contact": {
                "email": "sheffield@bluecross.org.uk",
                "telephone": "0300 777 1591",
                "address": "Old Station Drive, Sheffield",
                "postcode": "S7 2PY",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "71447fb6-150e-438d-8d1b-d9cd52ead94a",
            "name": "Blue Cross Thirsk",
            "contact": {
                "email": "thirsk@bluecross.org.uk",
                "telephone": "0300 777 1540",
                "address": "Parklands, Station Road, Topcliffe, Thirsk",
                "postcode": "YO7 3SE",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "05f27b11-0d19-4c57-a48f-7e9f889a7024",
            "name": "Blue Cross Rolleston",
            "contact": {
                "email": "rolleston@bluecross.org.uk",
                "telephone": "0300 777 1520",
                "address": "Hilda Archer Sanctuary, Dovecliff Road, Rolleston-on-Dove",
                "postcode": "DE13 9AU",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "986e7faa-fff3-4b9d-bc5f-4c1c2331de6d",
            "name": "Blue Cross Manchester",
            "contact": {
                "email": "manchester@bluecross.org.uk",
                "telephone": "0300 777 1592",
                "address": "48 Blackburn Street, Radcliffe",
                "postcode": "M26 1NQ",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "e6cea63a-1002-4569-9b63-01fd173801b3",
            "name": "Blue Cross Newport",
            "contact": {
                "email": "newport@bluecross.org.uk",
                "telephone": "0300 777 1590",
                "address": "Willenhall Street, Newport",
                "postcode": "NP19 0GE",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "e6cea63a-1002-4569-9b63-01fd173801b3",
            "name": "Blue Cross Devon",
            "contact": {
                "email": "devon@bluecross.org.uk",
                "telephone": "0300 777 1593",
                "address": "Pynes Hill Business Centre Ltd, Pynes Hill, Exeter",
                "postcode": "EX2 5JL",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "938c3e16-d1a0-4556-8389-7d9301ddd0c7",
            "name": "Blue Cross Herfordshire",
            "contact": {
                "email": "hertfordshire@bluecross.org.uk",
                "telephone": "0300 777 1490",
                "address": "Kimpton Bottom, Hertfordshire",
                "postcode": "SG4 8EU",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "50e6fb3c-54b8-45e9-bec1-0bd5395ce5bb",
            "name": "Blue Cross Boston",
            "contact": {
                "email": "boston@bluecross.org.uk",
                "telephone": "0300 777 1944",
                "address": "",
                "postcode": "",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "8668d49f-f62c-4566-96fe-251f373f341f",
            "name": "Blue Cross Burford",
            "contact": {
                "email": "burdford@bluecross.org.uk",
                "telephone": "0300 777 1570",
                "address": "Shilton Road, Burford",
                "postcode": "OX18 4PF",
                "lat": "",
                "lng": ""
            }
        },
        {
            "guid": "8668d49f-f62c-4566-96fe-251f373f341f",
            "name": "Blue Cross Southampton",
            "contact": {
                "email": "sourthampton@bluecross.org.uk",
                "telephone": "0300 777 1530",
                "address": "Bubb Lane, West End, Southampton",
                "postcode": "SO30 2HL",
                "lat": "",
                "lng": ""
            }
        }
    ]
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)