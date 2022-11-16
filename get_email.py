import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    answer = []
    for i in range(20):
        answer.append(data['results'][i]['email'])
    return answer
f = open('randomuser_data.json','r')
f = f.read()
data = json.loads(f)
print(get_email(data))