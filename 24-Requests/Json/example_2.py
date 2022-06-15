import json

data = '''{ "student": [ { "id":"01", "name": "Tom", "lastname": "Price" },{ "id":"02", "name":"Nick","lastname":"Thameson"} ]   }'''

data_dict = json.loads(data)
json_text = json.dumps(data_dict, indent=2)
final = json.loads(json_text)
with open("example.json") as example:
    from_file = json.load(example)
pass
