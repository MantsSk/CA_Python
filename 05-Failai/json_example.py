import json
 
# Opening JSON file
f = open('my_json.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['komandos']:
    if i['komandos_arena'] == "Nezinau":
        print(i['komandos_pavadinimas'])

# Closing file
f.close()