from typing import List
import json

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    def process_file(file: str) -> str:
        file = file.replace('\\', '\\\\')
        file = file.replace('/', '\\/')
        file = file.replace('"', '\\"')
        return file

    json_list = []
    for en, de in zip(english_file_list, german_file_list):
        en = process_file(en)
        de = process_file(de)
        json_str = json.dumps({"English": en, "German": de}, ensure_ascii=False)
        json_list.append(json_str)
    return json_list

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w', encoding='utf-8') as f:
        for line in file_list:
            f.write(line + '\n')

if __name__ == "__main__":
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, './concated.json')
