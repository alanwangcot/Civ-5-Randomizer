import os, json

def read_from_path(file_path:str) -> dict:
    # read file as json
    with open(file_path, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data

def save_to_path(file_path:str, data:dict) -> int:
    # save file as json
    with open(file_path, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return 0