class UserDto(object):
    def __init__(self, id=None, username=None, email=None, status=None, error=None):
        self.id = id
        self.username = username
        self.email = email
        self.status = status
        self.error = error
