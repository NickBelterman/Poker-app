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
        self.list_of_special_attr = ['sb', 'bb', 'd', 'fa']

    def __repr__(self):
        return f'Player: {self.name}, Attribute: {self.special_attr}, Cards: {self.cards}, Chips: {self.chips}, Stake: {self.stake}'
        
    def show_hand(self, name):
        print(f'{self.name}, {self.cards}')

    def show_special_attr(self, name):
        print(f'{self.special_attr}, {self.name}')

