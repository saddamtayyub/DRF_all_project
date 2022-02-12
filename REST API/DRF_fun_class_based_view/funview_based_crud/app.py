import requests
import json

URL = "http://127.0.0.1:8000/home/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=header, data=json_data)
    data = r.json()
    print(data)


# get_data()


def post_data():
    data = {
        'name': 'dummy1',
        'roll': 50,
        'city': 'mumbai'
    }
    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'}
    r = requests.post(url=URL, headers=header, data=json_data)
    data = r.json()
    print(data)


# post_data()

def update_data():
    data = {
        'id': 3,
        'name': 'update_dummy1',
        'roll': 4,
        'city': 'noida'
    }
    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'}
    r = requests.put(url=URL, headers=header, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {'id': 3}
    json_data = json.dumps(data)
    header = {'content-Type': 'application/json'}
    r = requests.delete(url=URL, headers=header, data=json_data)
    data = r.json()
    print(data)


delete_data()