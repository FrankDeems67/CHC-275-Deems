# Author: Frank Deems
# Date: 10/10/2025
# Title: Lab 2 - Simple Banking System
# Description: A very simple banking system
# that can show, add, remove, deposit,
# withdraw, and transfer money.
# -----------------------------------------

# list of account names
accounts = ["Frank", "Bob"]

# list of balances (same order as accounts)
balances = [500.0, 1000.0]

# main loop to keep program running
while True:
    print("--- BANK MENU ---")
    print("1. Show accounts")
    print("2. Add account")
    print("3. Remove account")
    print("4. Deposit money")
    print("5. Withdraw money")
    print("6. Transfer money")
    print("7. Exit")

    choice = input("Choose 1-7: ")

    # show accounts
    if choice == "1":
        for i in range(len(accounts)):
            print(accounts[i], "has $", balances[i])

    # add account
    elif choice == "2":
        name = input("Enter new account name: ")
        balance = float(input("Enter starting balance: "))
        accounts.append(name)
        balances.append(balance)
        print("Account added!")

    # remove account
    elif choice == "3":
        name = input("Enter account name to remove: ")
        if name in accounts:
            index = accounts.index(name)
            accounts.pop(index)
            balances.pop(index)
            print("Account removed.")
        else:
            print("Account not found.")

    # deposit money
    elif choice == "4":
        name = input("Enter account name: ")
        if name in accounts:
            index = accounts.index(name)
            amount = float(input("Enter amount: "))
            balances[index] += amount
            print("Deposit done!")
        else:
            print("Account not found.")

    # withdraw money
    elif choice == "5":
        name = input("Enter account name: ")
        if name in accounts:
            index = accounts.index(name)
            amount = float(input("Enter amount: "))
            if amount <= balances[index]:
                balances[index] -= amount
                print("Withdraw done!")
            else:
                print("Not enough money.")
        else:
            print("Account not found.")

    # transfer money
    elif choice == "6":
        name1 = input("Transfer from: ")
        name2 = input("Transfer to: ")
        if name1 in accounts and name2 in accounts:
            index1 = accounts.index(name1)
            index2 = accounts.index(name2)
            amount = float(input("Enter amount: "))
            if amount <= balances[index1]:
                balances[index1] -= amount
                balances[index2] += amount
                print("Transfer complete!")
            else:
                print("Not enough money.")
        else:
            print("Account not found.")

    # exit
    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")