import requests

URL = "http://localhost:8000/student-info/"

data = requests.get(url=URL)
json_data = data.json()
print(json_data)
