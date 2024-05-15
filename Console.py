import Client
from LogIn import LogIn
from SignIn import SignIn
from Collections import users
from Transactions import transactions

# Bank app
# User to my

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


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Choose your activity: ")

print("1. Make transaction\n"
      "2, Edit transaction\n"
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
    transaction = Client.Client.make_transaction(d, a, c, pt, tt, id)
    transaction.save()
#     opulod statistic czyli zrobienie statystyk edytowanie ususawnie i wysweitlanie ich i w sumie tyle poczytaj o dacie i bedzie git

print(transactions)

print(">>>>>>>>>>> T E S T >>>>>>>>>>>>")




