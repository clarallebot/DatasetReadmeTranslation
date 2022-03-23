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

#-----------Title
print("1. Title of Dataset - REQUIRED")
print(data['title'][0])
print("")

#-----------Creator
print("2. Creator Information - REQUIRED")

if len(data['creator']) > 0:
  nestcreator = data['nested_ordered_creator']

  ordered_creator = [None] * len(nestcreator)
  for x in nestcreator:
    ordered_creator[int(x['index'][0])] = x['creator'][0]

  for x in ordered_creator:
    print("Name:",x)
    print("Institution:")
    print("College, School or Department:")
    print("Address:")
    print("Email:")
    print("ORCID:")
    print("Role:")
    print("")

#elif len(data['creator']) == 1: 
#  print("Name:",data['creator'][0])
#  print("Institution:")
#  print("College, School or Department:")
#  print("Address:")
#  print("Email:")
#  print("ORCID:")
#  print("Role:")
#  print("")

#-----------Contributor
print("3. Contributor Information")
if len(data['contributor']) > 0:
  nestcontributor = data['nested_ordered_contributor']

  ordered_contributor = [None] * len(nestcontributor)
  for x in nestcontributor:
    ordered_contributor[int(x['index'][0])] = x['contributor'][0]

  for x in ordered_contributor:
    print("Name:",x)
    print("Institution:")
    print("College, School or Department:")
    print("Address:")
    print("Email:")
    print("ORCID:")
    print("Role:")
    print("")

elif len(data['contributor']) == 0:
  print("No contributors")
  print("")

#-----------Contact information
print("3. Contact Information - REQUIRED ")
print("Name:",x)
print("Institution:")
print("College, School or Department:")
print("Address:")
print("Email:")
print("ORCID:")
print("")

print("-------------------")
print ("# CONTEXTUAL INFORMATION")
print("-------------------")

#-----------Abstract
print("1. Abstract for the dataset - REQUIRED")

if len(data['abstract']) > 0:
  nestabstract = data['nested_ordered_abstract']

  ordered_abstract = [None] * len(nestabstract)
  for x in nestabstract:
    ordered_abstract[int(x['index'][0])] = x['abstract'][0]

  for x in ordered_abstract:
    print(x)
    print("")

#-----------Abstract
print("2. Context of the research project that this dataset was collected for.")
print("")

#-----------Date of data collection
print("3. Date of data collection:")
if len(data['date_collected']) > 0:
  print(data['date_collected'][0])

elif len(data['date_collected']) == 0:
  print("NA")

print("")



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