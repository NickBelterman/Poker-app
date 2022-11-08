class Player(object):
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = []
        self.chips = 0
        self.stake = 0
        self.stake_gap = 0
        self.fold = False
        self.ready = False
        self.all_in = False
        self.win = False
        self.special_attr = []
        
    def show_hand(self, name):
        print("{}'s hand: {}".format(self.name, self.cards))