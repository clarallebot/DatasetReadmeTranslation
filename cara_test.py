from datetime import date
import json
import requests
from lxml import html

today = date.today()
today = today.strftime("%Y-%m-%d")

with open('example_data.json') as json_file:
    data = json.load(json_file)

license_page = requests.get(data['license'][0])
license_tree = html.fromstring(license_page.content)
license_source = "Creative Commons"
license_title = license_tree.xpath("//span[@class='cc-license-title']/text()")[0]
license_id = license_tree.xpath("//span[@class='cc-license-identifier']/text()")[0]
    

text = (
    # header
    "[Instructions in this document are in between brackets.]\n"
    "[Dates in this document should use the format YYYY-MM-DD.]\n"
    "[Scholarly outputs cited in this document should follow a consistent style (e.g. APA style)]\n"
    "[When you are done filling this template delete all instructions and delete any sections or questions that do not apply to your dataset.]\n"
    "[Required items in this template are marked with a REQUIRED note next to the required field]\n"
    "[Items not marked as REQUIRED are optional, but fill this readme file as thoroughly as possible to ensure the reusability of your dataset.]\n"
    "[You may create more than one readme file in your dataset, if appropriate (e.g. one for your tabular data, one for your code)]\n"
    "[This template was created by Research Data Services at Oregon State University by modifying and expanding the University of Minnesota Libraries' readme template that can be found in z.umn.edu/readme]\n"
    "[Other sources used to elaborate this dataset: Georgia tech metadata template http://d7.library.gatech.edu/research-data/metadata;]\n"
    "[For questions or guidance about using this template contact researchdataservices@oregonstate.edu]\n"
    "[This template is published under a CC0 license. You are free to reuse, redistribute and modify this template as you wish.]\n\n"
    f"This documentation file was generated on {today}.\n\n"
    "---------------------\n# GENERAL INFORMATION\n---------------------\n\n"

    "1. Title of Dataset\n"
    f"{data['title'][0]}\n\n"
    
    "2. Creator Information\n\n"
    "[Fill in the names and information about the researchers that are considered authors of this dataset. ]\n"
    "[ORCID is a persistent digital identifier for researchers. https://orcid.org/ We encourage researchers to get one, but it is optional. You may chose to use a different author identifier if you have one.]\n"
    "[Role: role of the author in the dataset. Consider using the CreDit taxonomy to describe these roles: http://credit.niso.org/contributor-roles-defined/]\n"
    "[Creators are mentioned when citing the dataset. Make sure that they coincide with the Creator field in the repository record]\n\n"

    f"Name: {data['creator'][0]}\n\n"
    "...\n...\n...\n...\n\n"

    "--------------------------\nSHARING/ACCESS INFORMATION\n-------------------------- \n\n"
    "1. Licenses/restrictions placed on the data:\n"
    f"This work is licensed under a {license_source} {license_title} license {license_id}. {data['license'][0]}\n"
    )

with open('output_readme.txt', 'w') as readme:
    readme.write(text)

