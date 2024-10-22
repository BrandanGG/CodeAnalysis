import json
import os
# Read the data from the lang.json file to manage the allowed submission file types
def readJson(JFile:str) -> dict:
    dictionary = {}
    with open (JFile, 'r') as f:
        data = json.load(f)
        for x in data:
            if not 'extensions' in x:
                continue
            else:
                dictionary[x['name']] = x['extensions']
        return dictionary