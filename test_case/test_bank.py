
import unittest
from bank import Bank

class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_add_account(self):
        self.bank.add_account("Alice", 1000)
        self.assertEqual(self.bank.accounts["Alice"].balance, 1000)

    def test_deposit(self):
        self.bank.add_account("Alice", 1000)
        self.bank.deposit("Alice", 200)
        self.assertEqual(self.bank.accounts["Alice"].balance, 1200)

    def test_withdraw(self):
        self.bank.add_account("Alice", 1000)
        self.bank.withdraw("Alice", 500)
        self.assertEqual(self.bank.accounts["Alice"].balance, 500)

    def test_transfer_money(self):
        self.bank.add_account("Alice", 1000)
        self.bank.add_account("Bob", 500)
        self.bank.transfer_money("Alice", "Bob", 200)
        self.assertEqual(self.bank.accounts["Alice"].balance, 800)
        self.assertEqual(self.bank.accounts["Bob"].balance, 700)

    def test_overdraft(self):
        self.bank.add_account("Alice", 1000)
        with self.assertRaises(ValueError):
            self.bank.withdraw("Alice", 1500)

    def test_save_and_load(self):
        self.bank.add_account("Alice", 1000)
        self.bank.add_account("Bob", 500)
        self.bank.save2csv("testBank.csv")

        new_bank = Bank()
        new_bank.load_from_csv("testBank.csv")

        self.assertEqual(new_bank.accounts["Alice"].balance, 1000)
        self.assertEqual(new_bank.accounts["Bob"].balance, 500)

if __name__ == '__main__':
    unittest.main()
