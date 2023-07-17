import get_data
import json
def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    s= []
    p = 0
    obj = data['results']
    

    for i in obj:
        s.append(obj[p]['gender'])
        p+=1
    return s
file = open('randomuser_data.json', 'r').read()
data = json.loads(file)
name = data['results'][0]
print(get_gender_users(data))