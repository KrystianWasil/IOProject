import Client
from LogIn import LogIn
from SignIn import SignIn
from Collections import users
from Transactions import transactions, TypeOfTransaction
from os import system

# Bank app
# User to my
user = None
print("Welcome to the bank app "
      "\n1. Log in"
      "\n2. Sign in")
choice = input("Enter your choice: ")
if choice == '1':
    curr_login = LogIn(users)
    print("Type: login and password\n")
    login = input("Enter your login: ")
    p = input("Enter your password: ")
    if not curr_login.log_in(login, p) is None:
        user = curr_login.log_in(login, p)
        print("Logged in")
#     >>>> User logged in
if choice == '2':
    sign_in = SignIn(users)
    print("Type: name, login, id, password\n")
    n = input("Enter your name: ")
    login = input("Enter your login: ")
    i = input("Enter your id: ")
    p = input("Enter your password: ")
    sign_in.set_name(n)
    sign_in.set_login(login)
    sign_in.set_id(int(i))
    sign_in.set_password(p)
    user = Client.Client(n, i, p, login)
    sign_in.add_to_users(user)
    print("Signed in\n")

#     >>>> User signed in

while True:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Choose your activity: ")

    print("1. Make transaction\n"
          "2. Edit transaction\n"
          "3. Delete transaction\n"
          "4. Show statistics\n"
          )
    choice = input("Enter choice: ")
    if choice == '1':
        print("Enter Transaction")
        d = input("Enter date: ")
        a = input("Enter amount: ")
        c = input("Enter category: ")
        pt = input("Enter payment type: ")
        tt = input("Enter transaction type: ")
        id = input("Enter id: ")
        transaction = TypeOfTransaction(d, int(a), c, pt, tt, int(id))
        transaction.save()
    if choice == '2':
        print("Enter id of transaction to edit")
        id = input("Enter id: ")
        for i in transactions:
            if i.id == int(id):
                i.edit(int(id))
                print("Transaction edited")
    if choice == '3':
        print("Enter id of transaction to delete")
        id = input("Enter id: ")
        for i in transactions:
            if i.id == int(id):
                i.delete(int(id))
                print("Transaction deleted")
    if choice == '4':
        print(">>>>>>>>>>>>>>>>>>>>>>Statistics<<<<<<<<<<<<<<<<<<<<<<<<<<")
        user.statistics.upload_statistics()
        user.statistics.show_statistics()
        print("Category count: ", user.statistics.category_count)
        print("Transactions: ")
        for i in transactions:
            print(i.date, i.amount, i.category, i.payment_type, i.transaction_type, i.id)
