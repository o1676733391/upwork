import json
import re

# Read file xlsx and save to json
import pandas as pd
df = pd.read_excel('poster_designs\\poster_designs.xlsx')
df.to_json('output2.json', orient='records', lines=True)

# Load the JSON data from the file

json_file_path = 'output2.json'

data = []
with open(json_file_path, mode='r', encoding='utf-8') as json_file:
    for line in json_file:
        data.append(json.loads(line))



#     {
#         "Prompt": "A caricature of Ariana Grande with exaggerated high ponytail reaching the sky, wearing a fluffy unicorn onesie, singing into a microphone made of rainbow candy, on a stage surrounded by oversized cat-eared headphones --ar 2:3"
#     }
# split the string by '--ar' and store the first part in 'Prompt' and the second part in 'Aspect Ratio'
for item in data:
    if '--ar' in item['Prompt']:
        item['Prompt'], item['Aspect Ratio'] = item['Prompt'].split('--ar')
        item['Prompt'] = item['Prompt'].strip()
        item['Aspect Ratio'] = item['Aspect Ratio'].strip()

# Save the updated JSON data to a file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
    
# Load the JSON data from the file
json_file_path = 'output2.json'

with open(json_file_path, mode='r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Function to decode Unicode escape sequences
def decode_unicode_escapes(text):
    return re.sub(r'\\u[0-9a-fA-F]{4}', lambda x: x.group(0).encode().decode('unicode_escape'), text)

# Process each item to decode Unicode escape sequences
for item in data:
    for key, value in item.items():
        if isinstance(value, str):
            item[key] = decode_unicode_escapes(value)

# Save the cleaned data back to the JSON file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"JSON data has been successfully cleaned and saved to {json_file_path}")