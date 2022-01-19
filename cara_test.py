from datetime import date
import json

with open('example_data.json') as json_file:
    data = json.load(json_file)
    today = date.today()
    today = today.strftime("%Y-%m-%d")

text = (
    # header
    f"This documentation file was generated on {today}.\n\n"
    "-------------------\n# GENERAL INFORMATION\n-------------------\n\n"

    "1. Title of Dataset\n"
    f"{data['title'][0]}\n\n"
    
    "2. Creator Information\n\n"
    f"Name: {data['creator'][0]}"
    )

with open('output_readme.txt', 'w') as readme:
    readme.write(text)