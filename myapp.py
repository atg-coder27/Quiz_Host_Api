import requests
import json

url = 'http://127.0.0.1:8000/api/quiz/'
def get_data():
    r = requests.get(url=url)
    data = r.json()
    print(data)

get_data()