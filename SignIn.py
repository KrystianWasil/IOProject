
class SignIn:

    def __init__(self, users):
        self.name = None
        self.login = None
        self.id = None
        self.password = None
        self.users = users

    def set_password(self, password: str) -> None:
        self.password = password

    def set_id(self, id: int) -> None:
        self.id = id

    def set_login(self, login: str) -> None:
        self.login = login

    def set_name(self, name: str) -> None:
        self.name = name

    def add_to_users(self, user) -> None:
        self.users.append(user)
