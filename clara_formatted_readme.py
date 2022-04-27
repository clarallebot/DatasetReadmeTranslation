# https://realpython.com/python-f-strings/#python-f-strings-the-pesky-details

from datetime import date
from lxml import html
import json
import requests

def getvalue( arg1, arg2 ):
   # arg1 is a string, the name of the variable. arg2 is the value that the result should have if it is not defined  "
   if len(data[arg1]) > 0:
   	   value = data[arg1][0]
   elif len(data[arg1]) == 0:
       value = arg2
   return value;


today = date.today()
today = today.strftime('%Y-%m-%d')

with open('example_data2.json') as json_file:
    data = json.load(json_file)


template = (
    f"""
[Instructions in this document are in between brackets.]
[Dates in this document should use the format YYYY-MM-DD.]
[Scholarly outputs cited in this document should follow a consistent style (e.g. APA style)]
[When you are done filling this template delete all instructions and delete any sections or questions that do not apply to your dataset.]
[Required items in this template are marked with a REQUIRED note next to the required field]
[Items not marked as REQUIRED are optional, but fill this readme file as thoroughly as possible to ensure the reusability of your dataset.]
[You may create more than one readme file in your dataset, if appropriate (e.g. one for your tabular data, one for your code)]
[This template was created by Research Data Services at Oregon State University by modifying and expanding the University of Minnesota Libraries' readme template that can be found in z.umn.edu/readme]
[Other sources used to elaborate this dataset: Georgia tech metadata template http://d7.library.gatech.edu/research-data/metadata;]
[For questions or guidance about using this template contact researchdataservices@oregonstate.edu]
[This template is published under a CC0 license. You are free to reuse, redistribute and modify this template as you wish.]

This documentation file was generated automatically by ScholarsArchive@OSU on {today}.

-------------------
GENERAL INFORMATION
-------------------

1. Title of Dataset - REQUIRED
{data['title'][0]}

2. Creator Information - REQUIRED
[Fill in the names and information about the researchers that are considered authors of this dataset.]
[ORCID is a persistent digital identifier for researchers. https://orcid.org/ We encourage researchers to get one, but it is optional. You may chose to use a different author identifier if you have one.]
[Role: role of the author in the dataset. Consider using the CreDit taxonomy to describe these roles: http://credit.niso.org/contributor-roles-defined/]
[Creators are mentioned when citing the dataset. Make sure that they coincide with the Creator field in the repository record.]
    """)


if len(data['creator']) > 0:
  nestcreator = data['nested_ordered_creator']

  ordered_creator = [None] * len(nestcreator)
  for x in nestcreator:
    ordered_creator[int(x['index'][0])] = x['creator'][0]

  for x in ordered_creator:
  	template = (
  	f""" {template}
Name:{x}
Institution:
College, School or Department:
Address:
Email:
ORCID:
Role:
    """
)

template = (
    f"""{template}
3. Contributor information
[Contributors are not authors, they are collaborators that have contributed somehow to the dataset. They are not mentioned when citing the dataset. Make sure that they coincide with the Contributor field in the repository record.]
""")

if len(data['contributor']) > 0:
  nestcontributor = data['nested_ordered_contributor']

  ordered_contributor = [None] * len(nestcontributor)
  for x in nestcontributor:
    ordered_contributor[int(x['index'][0])] = x['contributor'][0]

  for x in ordered_contributor:
  	template = (
  	f""" {template}
Name:{x}
Institution:
College, School or Department:
Address:
Email:
ORCID:
Role:
 """)

elif len(data['contributor']) == 0:
    template = (
  	f""" {template} No contributors
  	""")

template = (
    f"""{template}
4. Contact Information - REQUIRED
[Usually a creator, but may be somebody else. Consider adding more than one contact if the main contact is expected to change positions soon (e.g. a student expected to graduate)]

Name:
Institution:
College, School or Department:
Address:
Email:
ORCID:


-------------------
CONTEXTUAL INFORMATION
-------------------

1. Abstract for the dataset - REQUIRED"""
)
if len(data['abstract']) > 0:
  nestabstract = data['nested_ordered_abstract']

  ordered_abstract = [None] * len(nestabstract)
  for x in nestabstract:
    ordered_abstract[int(x['index'][0])] = x['abstract'][0]

  for x in ordered_abstract:
    template = (
  	f""" {template} 
{x}
    """)

template = (
    f"""{template}
2. Context of the research project that this dataset was collected for.
[Any contextual information that will help to interpret the dataset. You can give details about the research questions that prompted the collection of this dataset. ]


3. Date of data collection:
[single date or range of dates in format YYYY-MM-DD]

""")
if len(data['date_collected']) > 0:
	template = (
  	f""" {template} 
{data['date_collected'][0]}
    """)

fundingstatement = getvalue('funding_statement','No funding statement')

template = (
    f"""{template}

4. Geographic location of data collection:
[Location of the data collection.]
[If you include coordinates use format: "latitude, longitude" where latitude and longitude are preferably in fraction of degrees (a decimal number), not sexagesimal, and where north latitude is positive (south is negative) and east longitude is positive (west is negative).]
[If you include a Bounding box indicate Label, Latitude North, Latitude South, Longitude West, Longitude East]
   


5. Funding sources that supported the collection of the data:
[Include agency and grant number if applicable]

{getvalue('funding_statement','No funding statement')}
 """)


# Make a function that will check if the variable exists and brings the value. Modify the function so that it includes the option of loading ordered items. 

with open('output_readme.txt', 'w') as readme:
    readme.write(template)
#    readme.write(creatortext)