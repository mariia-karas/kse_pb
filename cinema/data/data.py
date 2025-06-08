import json

def get_data(FILE_PATH):
    with open(FILE_PATH, 'r+') as f:
        content = json.load(f)
    return content

def load_data(data, FILE_PATH):
    with open(FILE_PATH, 'r+') as f:
        json.dump(data, f)
