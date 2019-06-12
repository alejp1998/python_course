class Player():

    def __init__(self,name,balance,dealer=False):
        self.name = name
        self.balance = balance
        self.dealer = dealer
        self.betamount = 0
        self.cards = []
        self.hit = True

    def __str__(self):
        return 'Player {}'.format(self.name)

    def bet(self,money):
        if self.balance >= money:
            self.betamount = money
            return self.bet
        return 0

    def win(self):
        self.balance += self.betamount

    def lose(self):
        self.balance -= self.betamount

    def cards_sum(self):
        sum = 0
        for value in self.cards:
            sum += value
        return sum
