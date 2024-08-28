import csv
import json
import os


class Account(object):

    def __init__(self, name, balance):
        self.name = name
        if balance < 0:
            raise ValueError('balance must be positive')

        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError('balance must be greater than or equal to amount')

        self.balance -= amount
        return self.balance



class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance):
        if name in self.accounts:
            raise ValueError('account name already exists')

        self.accounts[name] = Account(name, balance)
        return self.accounts[name]

    def deposit(self, name, amount):
        if name not in self.accounts:
            raise ValueError('account does not exists')

        self.accounts[name].deposit(amount)

    def withdraw(self, name, amount):
        if name not in self.accounts:
            raise ValueError('account does not exists')

        self.accounts[name].withdraw(amount)

    def transfer_money(self, name, receiver, amount):
        if name not in self.accounts:
            raise ValueError('account does not exists')

        self.accounts[name].withdraw(amount)
        self.accounts[receiver].deposit(amount)

    def save2csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'balance'])

            for account in self.accounts.values():
                writer.writerow([account.name, account.balance])

    def load_from_csv(self, filename):
        if not os.path.exists(filename):
            return

        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add_account(row['name'], float(row['balance']))


if __name__ == "__main__":
    bank = Bank()
    bank.add_account("Tom", 2000)
    bank.add_account("Jack", 1500)
    bank.deposit("Jack", 200)
    bank.withdraw("Tom", 100)
    bank.transfer_money("Tom", "Jack", 150)
    print(bank)
    bank.save2csv("bank.csv")







