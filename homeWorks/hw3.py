class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        usermoney = int(input('Enter your money '))
        self._balance += usermoney

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _join_balance(self, username):
        self._balance += username._balance


user1 = Bank('John', 1000)
user2 = Bank('Jack', 1000)
user3 = Bank('Bob', 1000)

user3.moneyX()

user3._kill()

user1._Bank__jackpot()

user2._join_balance(user1)
