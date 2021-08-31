import json
import requests


URL = "http://localhost:8000/student-api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
        'name': 'Antar',
        'roll': 104,
        'city': 'Barisal'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


def update_data():
    data = {
        'id': 5,
        'name': 'Samia',
        'roll': 105,
        'city': 'Chittagong'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {
        'id': 4,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data(2)
# post_data()
# update_data()
delete_data()
