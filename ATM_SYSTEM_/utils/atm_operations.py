from utils.create_account import load_accounts, save_accounts


def check_balance(account_number):
    accounts = load_accounts()
    return accounts[account_number]["balance"]


def deposit(account_number, amount):
    accounts = load_accounts()
    accounts[account_number]["balance"] += amount
    save_accounts(accounts)
    return accounts[account_number]["balance"]


def withdraw(account_number, amount):
    accounts = load_accounts()

    if accounts[account_number]["balance"] >= amount:
        accounts[account_number]["balance"] -= amount
        save_accounts(accounts)
        return True, accounts[account_number]["balance"]
    else:
        return False, accounts[account_number]["balance"]
