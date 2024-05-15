import Transactions
import Statistics
import Balance


class Client:
    def __init__(self, name, id, password, login):
        self.name = name
        self.id = id
        self.password = password
        self.login = login
        self.balance = Balance.Balance(0, "")
        self.statistics = Statistics.Statistics(0, "", 0, "")

    @staticmethod
    def make_transaction(date, amount, category, payment_type, transaction_type, id):
        return Transactions.TypeOfTransaction(date, amount, category, payment_type, transaction_type, id)
