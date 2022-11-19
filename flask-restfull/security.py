from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'bob', 'asdf')
]

usename_mapping = {
    # list comprehension used to create a dictionary
    u.username: u for u in users
}

userid_mapping = {
    u.id: u for u in users
}

def authenticate(username, password):
    user = usename_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)