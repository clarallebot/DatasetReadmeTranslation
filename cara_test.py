from datetime import date
from lxml import html
import json
import requests

today = date.today()
today = today.strftime('%Y-%m-%d')

with open('example_data2_pp.json') as json_file:
    data = json.load(json_file)


def getvalue( arg1, arg2, pre_text="", post_text="" ):
    # arg1 is a string, the name of the variable. arg2 is the value that the result should have if it is not defined  "
    print(arg1)
    if len(data[arg1]) == 1:
        print("Length equal one")
        value = data[arg1][0]
    elif len(data[arg1]) == 0:
        print("Length equal zero")
        value = arg2
    elif len(data[arg1]) > 1:
        print("Length more than one")
        nestedarg1 = "nested_ordered_"+arg1
        temp = data[nestedarg1]
        tempvalue = [None] * len(temp)
        value = (f""" """)
        for x in temp:
            tempvalue[int(x['index'][0])] = x[arg1][0]
        for x in tempvalue:
            value = (
            f""" {value}
{pre_text}{x} {post_text}
    """
)
        # We need to add an option for not ordered too.
    return value;


def getlabel(fieldname, xpath, pre_text=""):
    # fieldname is the name of the field where the URI is located
    # xpath is the path to the location of the label in the LD source page
    print(fieldname)
    if len(data[fieldname]) == 1:
        print("Length equal one")
        uri = data[fieldname][0]
        page = requests.get(uri)
        tree = html.fromstring(page.content)
        label = pre_text + tree.xpath(xpath)[0].replace('\n','')
    else:
        print("Length not equal to one")
        label = "No label available at this time"
    return label;



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

...\n...\n...\n...
    """)

# Pull label from Academic Affiliation URI
affiliation_uri = data['academic_affiliation'][0]
jsonld = 'http://opaquenamespace.org/ns/osuAcademicUnits.jsonld'
affiliation_dict = requests.get(jsonld).json()['@graph']
record = None
for unit in affiliation_dict:
 if unit['@id'] == affiliation_uri:
  record = unit
affiliation_label = record['rdfs:label']['@value']

template = (
    f""" {template}

5. Publisher Information

College, School or Department: 
{affiliation_label}
  """)


# Pull label from Location URI
location_uri = data['based_near'][0]['id']
geonameId = location_uri[location_uri.index('org/') + 4:-1]
geo_json = 'http://www.geonames.org/getJSON?geonameId=' + geonameId + '&username=demo'
geo_record = requests.get(geo_json).json()
location_label = geo_record['toponymName']

geo_label = None
for geo in data['nested_geo']:
    if geo['label'] != []:
        geo_label = geo['label'][0]
    if geo['point'] != []:
        geo_label = geo_label + ' (' + str(geo['point'][0]) + ')'
    elif geo['bbox'][0] != []:
        geo_label = geo_label + ' (' + str(geo['bbox'][0]) + ')'

template = (
    f""" {template}
-------------------
CONTEXTUAL INFORMATION
-------------------
...\n...\n...\n...

4. Geographic location of data collection:
{location_label}
{geo_label}

    """)

# Pull label from License URI
license_uri = data['license'][0]
license_page = requests.get(license_uri)
license_tree = html.fromstring(license_page.content)
license_label = "Creative Commons " + license_tree.xpath('//span[@class="cc-license-title"]/text()')[0]
license_id = license_tree.xpath('//span[@class="cc-license-identifier"]/text()')[0].replace('\n','')


# Pull label from Rights Statement URI
rights_uri = data['rights_statement'][0]
rights_page = requests.get(rights_uri)
rights_tree = html.fromstring(rights_page.content)
rights_label = rights_tree.xpath('//div[@class="statement-textcolumn"]/h1/text()')[0]

template = (
    f""" {template}
--------------------------
SHARING/ACCESS INFORMATION
--------------------------

1. Licenses/restrictions placed on the data:
This work is licensed under a {getlabel('license', '//span[@class="cc-license-title"]/text()', 'Creative Commons ')} license {getlabel('license', '//span[@class="cc-license-identifier"]/text()')}. More information: {getvalue('license','Not applicable')}
The copyright status for this work is {getlabel('rights_statement', '//div[@class="statement-textcolumn"]/h1/text()', '')}. More information: {getvalue('rights_statement','oops')}

...\n...\n...\n...

    """) 
 
with open('output_readme.txt', 'w') as readme:
    readme.write(template)

