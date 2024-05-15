class LogIn:
    def __init__(self, users):
        self.users = users

    def log_in(self, login, password):
        for user in self.users:
            if user.login == login and user.password == password:
                return user
        return None
    # def verification(self, login):
    #     for user in self.users:
    #         if user.login == login:
    #             return True
    #     return False
