# Interfejs TypeOfTransaction
from Collections import transactions


class TypeOfTransaction:
    def __init__(self, date, amount, category, payment_type, transaction_type, id):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category
        self.payment_type = payment_type
        self.transaction_type = transaction_type

    def save(self):
        transactions.append(self)
        print(f"Saved: {self.transaction_type} - {self.date}")

    def delete(self, id):
        for transaction in transactions:
            if transaction.id == id:
                transactions.remove(transaction)
        print(f"Deleted: {self.transaction_type} - {self.date}")

    def edit(self, id):
        print("Type to change?")
        print("1. Date")
        print("2. Amount")
        print("3. Category")
        print("4. Payment type")
        print("5. Transaction type")
        choice = input()
        if choice == 1:
            self.date = input("Enter new date: ")
        elif choice == 2:
            self.amount = input("Enter new amount: ")
        elif choice == 3:
            self.category = input("Enter new category: ")
        elif choice == 4:
            self.payment_type = input("Enter new payment type: ")
        elif choice == 5:
            self.transaction_type = input("Enter new transaction type: ")
        else:
            print("Invalid choice")


class TransactionIncome(TypeOfTransaction):
    def __init__(self, date, amount, category, payment_type):
        super().__init__(date, amount, category, payment_type, "Income", id)

    def save(self):
        super().save()
        print("Saved: Income transaction")

    def delete(self, id):
        super().delete(id)
        print("Deleted: Income transaction")

    def edit(self, id):
        super().edit(id)
        print("Edited: Income transaction")


class TransactionOutcome(TypeOfTransaction):
    def __init__(self, date, amount, category, payment_type):
        super().__init__(date, amount, category, payment_type, "Outcome", id)

    def save(self):
        super().save()
        print("Saved: Outcome transaction")

    def delete(self, id):
        super().delete(id)
        print("Deleted: Outcome transaction")

    def edit(self, id):
        super().edit(id)
        print("Edited: Outcome transaction")
