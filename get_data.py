import json
import pprint
def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
file = open('randomuser_data.json', "r").read()
data = json.loads(file)
pprint.pprint(data)