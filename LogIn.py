from Client import Client


class LogIn:
    def __init__(self, file_name):
        self.file_name = file_name

    def log_in(self, login, password):
        with open(self.file_name, 'r') as file:
            for line in file:
                name, file_login, id, file_password = line.strip().split()
                if file_login == login and file_password == password:
                    return Client(name, id, file_password, file_login)
        return None