import requests


database = {
    1: 'Alice',
    2: 'Bob',
    3: 'Charlie'
}

def get_user_from_db(user_id):
    return database[user_id]

def get_comments():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    if r.status_code == 200:
        data = r.json() 
        return data 
    raise requests.exceptions.HTTPError


# f = get_comments()
# print(f)