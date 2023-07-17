import get_data
import json
def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    s= []
    p = 0
    obj = data['results']
    

    for i in obj:
        s.append(obj[p]['email'])
        p+=1
    return s
file = open('randomuser_data.json', 'r').read()
data = json.loads(file)
name = data['results'][0]
print(get_email(data))