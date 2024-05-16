from Collections import transactions

class Statistics:
    def __init__(self, spend_amount, most_common_category, earned_amount, date):
        self.spend_amount = spend_amount
        self.most_common_category = most_common_category
        self.earned_amount = earned_amount
        self.date = date
        self.transactions = transactions
        self.category_count = {}

    def show_statistics(self):
        print("Spend amount: ", self.spend_amount)
        print("Most common category: ", self.most_common_category)
        print("Earned amount: ", self.earned_amount)
        print("Date: ", self.date)

    def upload_statistics(self):
        for transaction in transactions:
            if transaction.transaction_type == "Income":
                self.earned_amount += transaction.amount
            else:
                self.spend_amount += transaction.amount

            if transaction.category in self.category_count:
                self.category_count[transaction.category] += 1
            else:
                self.category_count[transaction.category] = 1