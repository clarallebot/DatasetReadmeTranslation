# Execute this program by typing >python clara_learningpython_draft.py in the unix shell
# To save a readme execute this program by typing python clara_learningpython_draft.py >readme_draft.txt

import json
from datetime import date

with open('example_data.json') as json_file:
    data = json.load(json_file)
    #print(data['title'])

#type(data)
today = date.today()

print("This documentation file was generated automatically by ScholarsArchive@OSU on",today)

print("-------------------")
print ("# GENERAL INFORMATION")
print("-------------------")

print("1. Title of Dataset - REQUIRED")
print(data['title'])
print("")
print("2. Creator Information - REQUIRED")

if len(data['creator']) > 1:
  nestcreator = data['nested_ordered_creator']

  ordered_creator = [None] * len(nestcreator)
  for x in nestcreator:
    ordered_creator[int(x['index'][0])] = x['creator'][0]

  for x in ordered_creator:
    print("Name:",x)
elif len(data['creator']) == 1: 
  print("Name:",data['creator'][0])



#print(data['creator'])
#print(data['nested_ordered_creator']['index'])

#print("2. Contributor Information")
#print("Name:",data['contributor'])
#print(data['nested_ordered_contributor'][0]['index'][0])

#nestdic = data['nested_ordered_contributor']
#print(nestdic)

#print("For Loop")
#for x in nestdic:
#  print(x['index'][0])
#  print(x['contributor'][0])

#for x in range(0, len(nestdic)-1);


#What type of variable is data?
#print(type(data))
#<class 'dict'>
#print(type(data['contributor']))
#<class 'list'>
#print(type(data['nested_ordered_contributor']))
#<class 'list'>
#print(type(data['nested_ordered_contributor'][0]))
#<class 'dict'>
#print(type(data['nested_ordered_contributor'][0]['index'][0]))
#<class 'str'>


## Examples from https://www.w3schools.com/python/python_json.asp
## FROM JSON TO PYTHON
## some JSON:
#x =  '{ "name":"John", "age":30, "city":"New York"}'
#
## parse x:
#y = json.loads(x)
#
## the result is a Python dictionary:
#print('print y["name"]')
#print(y["name"])
#
## FROM PYTHON TO JSON
#
#x = {
#  "name": "John",
#  "age": 30,
#  "married": True,
#  "divorced": False,
#  "children": ("Ann","Billy"),
#  "pets": None,
#  "cars": [
#    {"model": "BMW 230", "mpg": 27.5},
#    {"model": "Ford Edge", "mpg": 24.1}
#  ]
#}
#
## convert into JSON:
#y = json.dumps(x)
#
## the result is a JSON string:
#print('print y')
#print(y)
#
#print('json.dumps(True)')
#print(json.dumps(True))
#
#print('End of the Clara learning Python script')