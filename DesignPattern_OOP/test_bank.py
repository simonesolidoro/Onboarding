import unittest
from banche_RefactoringStartegy import BankAccount, SavingsAccount, Interesse,Fisso,Composto

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount()
        money = 1000
        account.deposit(money)
        self.assertEqual(money, account.get_balance())  # add assertion here
    def test_withdraw(self):
        start_balance = 1000
        account = BankAccount(start_balance)
        money_to_withdraw = 500
        money_rest = start_balance-money_to_withdraw
        account.withdraw(money_to_withdraw)
        self.assertEqual(money_rest, account.get_balance())
    def test_compute_interest_fisso(self):
        start_money = 1000
        rate = 0.10
        saving_account = SavingsAccount(Fisso(),start_money,rate)
        years = 2
        saving_account.compute_interest(years)
        self.assertEqual(1200,saving_account.get_balance())

    def test_compute_interest_composto(self):
        start_money = 1000
        rate = 0.10
        saving_account = SavingsAccount(Composto(), start_money, rate)
        years = 2
        saving_account.compute_interest(years)
        self.assertEqual(1210,saving_account.get_balance())

if __name__ == '__main__':
    unittest.main()
