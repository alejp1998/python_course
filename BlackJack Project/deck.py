import random

class Deck():
    #52 cards standard deck
    deck = [1]*4 + [2]*4 + [3]*4 + [4]*4 + [5]*4 + [6]*4 + [7]*4 + [8]*4 + [9]*4 + [10]*16

    #Deck definition
    def __init__(self):
        self.cards = Deck.deck

    def new_decks(self,ndecks=1):
        self.cards = Deck.deck*ndecks

    def take_card(self):
        return self.cards.pop( random.randint( 0 , len(self.cards) ) )

    def mix(self):
        pass
