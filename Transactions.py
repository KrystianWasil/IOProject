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
        for transaction in transactions[:]:  # Create a copy for iteration
            if transaction.id == id:
                transactions.remove(transaction)
        print(f"Deleted: {self.transaction_type} - {self.date}")

    def edit(self, id):
        if self.id == id:
            print("What would you like to change?")
            print("1. Date")
            print("2. Amount")
            print("3. Category")
            print("4. Payment type")
            print("5. Transaction type")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.date = input("Enter new date: ")
            elif choice == '2':
                self.amount = int(input("Enter new amount: "))
            elif choice == '3':
                self.category = input("Enter new category: ")
            elif choice == '4':
                self.payment_type = input("Enter new payment type: ")
            elif choice == '5':
                self.transaction_type = input("Enter new transaction type: ")
            else:
                print("Invalid choice")

class TransactionIncome(TypeOfTransaction):
    def __init__(self, date, amount, category, payment_type, id):
        super().__init__(date, int(amount), category, payment_type, "Income", int(id))

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
    def __init__(self, date, amount, category, payment_type, id):
        super().__init__(date, int(amount), category, payment_type, "Outcome", int(id))

    def save(self):
        super().save()
        print("Saved: Outcome transaction")

    def delete(self, id):
        super().delete(id)
        print("Deleted: Outcome transaction")

    def edit(self, id):
        super().edit(id)
        print("Edited: Outcome transaction")