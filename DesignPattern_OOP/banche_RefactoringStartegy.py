# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from abc import ABC,abstractmethod

class BankAccount:
    def __init__(self,balance = 0):
        assert balance >= 0, "start balance must be positive "
        self.balance_ = balance
    @property
    def balance(self):
        return self.balance_

    def deposit(self, amount):
        assert amount >= 0, "amount must be positive "
        self.balance_ += amount
    def withdraw(self, amount):
        if amount > self.balance_:
            raise ValueError("amount must be less than balance")
        self.balance_ -= amount
    def get_balance(self):
        return self.balance


class interesse(ABC):
    @abstractmethod
    def compute_interest(self):
        pass
class composto(interesse):
    def compute_interest(self,start : float,rate : float,anni : int) -> float:
        if (start < 0 or anni < 0 or rate < 0):
            raise ValueError("start, anni and rate must be positive ")
        saldo = start
        for i in range(anni):
             saldo += (saldo*rate)
        return saldo-start
class fisso(interesse):
    def compute_interest(self,start : float,rate : float,anni : int) -> float:
        if (start < 0 or anni < 0 or rate < 0):
            raise ValueError("start, anni and rate must be positive ")
        return start*rate*anni

class SavingsAccount(BankAccount):
    def __init__(self, StrategyInteresse, balance = 0, rate = 1):
        assert rate >= 0 , "rate must be grater than 1 "
        super().__init__(balance)
        self.rate_ = rate
        self.inter = StrategyInteresse

    @property
    def rate(self):
        return self.rate_
    @rate.setter
    def rate(self,rate):
        self.rate_ = rate
    def compute_interest(self,years:int=0):
        add = self.inter.compute_interest(start= self.get_balance(), rate = self.rate,anni = years)
        self.balance_ += add
        pass
