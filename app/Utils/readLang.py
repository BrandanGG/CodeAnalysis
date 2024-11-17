import json
import os

def readJson(fileName: str) -> str:
    dictionary = {}
    JFile = 'Utils/FileTypes/lang.json'
    
    try:
        with open(JFile, 'r') as f:
            data = json.load(f)
            for x in data:
                if 'extensions' in x:
                    # Store each extension as a key in the dictionary
                    for ext in x['extensions']:
                        dictionary[ext.lower()] = x['name'].lower()  # Ensure both keys and values are lowercase
        # Split the filename to get the extension
        split = fileName.split('.')
        if len(split) > 1:  # Check if there is an extension
            extension = '.' + split[-1].lower()  # Include the dot for matching
            if extension in dictionary:  # Check directly against the dictionary keys
                return dictionary[extension]  # Return the corresponding type

    except FileNotFoundError:
        return "File not found"
    except Exception:
        return "Error occurred while detecting file type"
    
    return None  # Explicit return for clarity if no match is found
