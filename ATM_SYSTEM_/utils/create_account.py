import json
import os

DATA_FILE = r"C:\Users\user\Desktop\Project_of_python\ATM_SYSTEM_\data\person_data.json"


def load_accounts():
    with open(DATA_FILE, "r") as file:
      return json.load(file)

def save_accounts(accounts):
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)


def authenticate(account_number, pin):
    accounts = load_accounts()
    if account_number in accounts and accounts[account_number]["pin"] == pin:
        return accounts[account_number]
    return None
