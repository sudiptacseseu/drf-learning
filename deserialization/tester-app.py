import json
import requests


URL = "http://localhost:8000/student-create/"

data = {'name': 'Sudipta', 'roll': 104, 'city': 'Manikganj'}
json_data = json.dumps(data)

data = requests.post(url=URL, data=json_data)
json_data = data.json()

print(json_data)
