from utils.create_account import authenticate
from utils.atm_operations import check_balance, deposit, withdraw


def atm_menu(account_number):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            balance = check_balance(account_number)
            print(f"Your balance is: ₹{balance}")
          

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            new_balance = deposit(account_number, amount)
            print(f"Deposit successful! New balance: ₹{new_balance}")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            success, balance = withdraw(account_number, amount)
            if success:
                print(f"Withdrawal successful! Remaining balance: ₹{balance}")
            else:
                print("Insufficient balance!")

        elif choice == "4":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")


def main():
    print("===== Welcome to Python ATM =====")

    account_number = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    user = authenticate(account_number, pin)

    if user:
        print(f"Welcome {user['name']}!")
        atm_menu(account_number)
    else:
        print("Invalid account number or PIN!")


if __name__ == "__main__":
    main()
