class SignIn:
    def __init__(self, file_name):
        self.name = None
        self.login = None
        self.id = None
        self.password = None
        self.file_name = file_name

    def set_password(self, password: str) -> None:
        self.password = password

    def set_id(self, id: int) -> None:
        self.id = id

    def set_login(self, login: str) -> None:
        self.login = login

    def set_name(self, name: str) -> None:
        self.name = name

    def add_to_users(self, user) -> None:
        with open(self.file_name, 'a+') as file:
            file.write(f"{user.name} {user.login} {user.id} {user.password}\n")
