import random

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit 
        self.value = value
        
    def __repr__(self):
        return self.show_all()
        
    def show_all(self):
        return f"{self.value}{self.suit}"

class Deck(list):
    def __init__(self):
        self.build()

    def build(self):
        [self.append(Card(suit, value)) for suit in ['S', 'C', 'D', 'H'] for value in range(2, 15)]

    def show_deck(self):
        [card.show_all() for card in self]

    def shuffle(self):
        for i in range(len(self)-1, 0, -1):
            r = random.randint(0, i)
            self[i], self[r] = self[r], self[i]

    def deal(self, location, times=1):
        [location.append(self.pop(0)) for i in range(times)]