import json
import yaml

with open("sample_json.json", "r") as file:
	value = json.load(file) 


# json to text
with open("sample_text.txt", "w") as text_file:
	text_file.write(str(value)) 

# json to yaml
with open("sample_yaml.yaml", "w") as yaml_file:
	yaml.dump(value, yaml_file)

# yaml to json
with open("sample_yaml.yaml", "r") as yaml_file:
	value_1 = yaml.load(yaml_file)

with open("sample_json.json", "w") as json_file:
	json.dump(yaml_file, json_file, indent = 2, sort_keys = True)

# yaml to text
with open("sample_text_1.txt", "w") as text_file_1:
	text.write(str(value_1))



