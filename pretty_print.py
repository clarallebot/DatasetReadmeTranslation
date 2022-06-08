# Modified from source: https://www.geeksforgeeks.org/json-pretty-print-using-python/ 

import json

# Read JSON data from file and pretty print it
with open("example_data2.json", "r") as read_file:
    data = json.load(read_file)

# Write pretty printed JSON data to file
with open('example_data2_pp.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)

