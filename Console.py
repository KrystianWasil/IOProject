import Client
import Admin
import Balance
import Statistics
import Transactions
from LogIn import LogIn
from SignIn import SignIn
from Collections import users
from Collections import transactions


# Bank app

print("Welcome to the bank app "
      "\n1. Log in"
      "\n2. Sign in")
choice = input("Enter your choice: ")
if choice == '1':
    login = LogIn(users)
    print("Type: login and password\n")
    l = input("Enter your login: ")
    p = input("Enter your password: ")
    login.log_in(l,p)

