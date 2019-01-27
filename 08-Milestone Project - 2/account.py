class Account:
    def __init__(self):
        self.mymoney = 50

    def add_money(self, money):
        self.mymoney += money

    def remove_money(self, money):
        if money <= self.mymoney:
            self.mymoney -= money
            return "success"
        else:
            self.mymoney = 0
            return "failure"
