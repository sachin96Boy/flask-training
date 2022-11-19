class User:
    def __init__(self, _id, username, password):
        # used _id because id is a reserved word in python
        self.id = _id
        self.username = username
        self.password = password