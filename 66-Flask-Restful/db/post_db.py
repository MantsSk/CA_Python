import requests
import json

new_task = {
    "title": "asdasdasd",
    "done": False
}

r = requests.post('http://127.0.0.1:8000/tasks/new', json=new_task)
print(json.loads(r.text))

#r = requests.get('http://127.0.0.1:8000/tasks')
# print(json.loads(r.text))

#r = requests.get('http://127.0.0.1:8000/tasks/1')
# print(json.loads(r.text))

#r = requests.put('http://127.0.0.1:8000/tasks/8', json=new_task)
# print(json.loads(r.text))

#r = requests.delete('http://127.0.0.1:8000/tasks/7')
# print(json.loads(r.text))
