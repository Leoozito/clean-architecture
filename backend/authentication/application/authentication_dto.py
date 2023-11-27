class AuthDto(object):
    id: int
    user: str
    is_admin: bool

    def __init__(self, user: str, is_admin: bool):
        self.user = user
        self.is_admin = is_admin

    