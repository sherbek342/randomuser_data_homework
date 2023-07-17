import json
import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    s= 0
    for i in data['results']:
        s += 1
    return s
file = open('randomuser_data.json', 'r').read()
data = json.loads(file)
name = data['results'][0]
print(get_count_users(data))