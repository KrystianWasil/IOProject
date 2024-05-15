from Collections import transactions


class Statistics:
    def __init__(self, spend_amount, most_common_category, earned_amount, date):
        self.spend_amount = spend_amount
        self.most_common_category = most_common_category
        self.earned_amount = earned_amount
        self.date = date
        self.transactions = transactions

    def show_statistics(self, date_start, date_end):
        for transaction in transactions:
            if date_start <= transaction.date <= date_end:
                print("Spend amount: ", self.spend_amount)
                print("Most common category: ", self.most_common_category)
                print("Earned amount: ", self.earned_amount)
                print("Date: ", self.date)
