import yaml
from pprint import pprint

yaml_data = {
    "name": "CLoudKing",
    "from": "Earth",
    "address": {
        "street": "Some where on the earth",
        "city": "Some City",
        "zip_code": 123456
    },
    "languages": ["C", 'Python', "Java", "JavaScript"],
    "about": "Hi Guys! I am a software developer" \
             "From Earth" \
             "Seeking a job at Some city on the Earth"
}

with open('info.yml', 'w') as file:
    yaml.safe_dump(yaml_data, file, default_flow_style=False)

with open('info.yml', 'r') as file:
    data = yaml.safe_load(file)
    pprint(data)
    print("Available keys are : %s" % data.keys())
