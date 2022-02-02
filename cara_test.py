from datetime import date
from lxml import html
import json
import requests

today = date.today()
today = today.strftime('%Y-%m-%d')

with open('example_data.json') as json_file:
    data = json.load(json_file)

license_page = requests.get(data['license'][0])
license_tree = html.fromstring(license_page.content)
license_title = license_tree.xpath('//span[@class="cc-license-title"]/text()')[0]
license_id = license_tree.xpath('//span[@class="cc-license-identifier"]/text()')[0]
license_id = license_id.replace('\n','')
    

text = (
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

1. Title of Dataset
{data['title'][0]}
   
2. Creator Information
[Fill in the names and information about the researchers that are considered authors of this dataset. ]
[ORCID is a persistent digital identifier for researchers. https://orcid.org/ We encourage researchers to get one, but it is optional. You may chose to use a different author identifier if you have one.]
[Role: role of the author in the dataset. Consider using the CreDit taxonomy to describe these roles: http://credit.niso.org/contributor-roles-defined/]
[Creators are mentioned when citing the dataset. Make sure that they coincide with the Creator field in the repository record]

Name: {data['creator'][0]}

...\n...\n...\n...\n

--------------------------
SHARING/ACCESS INFORMATION
--------------------------

1. Licenses/restrictions placed on the data:
This work is licensed under a Creative Commons {license_title} license {license_id}. {data['license'][0]}
    """
    )

with open('output_readme.txt', 'w') as readme:
    readme.write(text)

