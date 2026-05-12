import pytest
from banche_RefactoringStartegy import BankAccount, SavingsAccount, Interesse,Fisso,Composto

@pytest.fixture()
def account():
    return BankAccount()
@pytest.mark.parametrize("money,expected",
                         [(100,100),
                          (200,200),
                          (1000,1000)])
def test_deposit(account,money,expected):
    account.deposit(money)
    assert expected == account.get_balance()  # add
def test_deposit_exeption(account):# assertion here
    with pytest.raises(ValueError, match = "amount must be positive"):
        account.deposit(-200)
def test_withdraw(account):
    start_balance = 1000
    account.deposit(start_balance)
    money_to_withdraw = 500
    money_rest = start_balance-money_to_withdraw
    account.withdraw(money_to_withdraw)
    assert money_rest == account.get_balance()

def test_compute_interest_fisso():
    start_money = 1000
    rate = 0.10
    saving_account = SavingsAccount(Fisso(),start_money,rate)
    years = 2
    saving_account.compute_interest(years)
    assert 1200 == saving_account.get_balance()

def test_compute_interest_composto():
    start_money = 1000
    rate = 0.10
    saving_account = SavingsAccount(Composto(), start_money, rate)
    years = 2
    saving_account.compute_interest(years)
    assert 1210 == saving_account.get_balance()


