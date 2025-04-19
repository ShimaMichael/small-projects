import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

if response.status_code == 200:
    post = response.json()
    for p in post:
        if p['id'] == 7:
            print(p)