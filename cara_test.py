import json

with open('example_data.json') as json_file:
    data = json.load(json_file)
    print(data['title'])