import itertools
from collections import Counter
from Cards import Deck
from Player import Player


class Game(object):
    def __init__(self, name, list_of_players):
        self.game_over = False
        self.need_raise = False
        self.active_player = Player("a")
        self.possible_actions = []
        self.cards = []
        self.pot = 0
        self.pot_dict = {}
        self.list_of_players = []
        self.dealer = Player('a')
        self.small_blind = Player('a')
        self.big_blind = Player('a')
        self.first_actor = Player('a')
        self.winners = []
        self.deck = Deck()
        self.score_of_possible_winners = []
        self.players_not_out = list(list_of_players)
        
    def show_comunity_cards(self):
        print('Comunity cards: {}'.format(self.cards))
    
    def shuffle_deck(self):
        self.deck.shuffle()
    
    def deal_hole(self):
        count = 0
        while count < 2:
            for player in self.players_not_out:
                self.deck.deal(player, 1)
            count += 1
    
    def deal_flop(self):
        self.deck.burn()
        self.deck.deal(self, 3)
        
    def deal_turn(self):
        self.deck.burn()
        self.deck.deal(self, 1)

    def deal_river(self):
        self.deck.burn()
        self.deck.deal(self, 1)
        
    def establish_player_attr(list_players_in_game):
        index_assignment = 0
        dealer = list_players_in_game[index_assignment]
        dealer.special_attr.append('dealer')
        index_assignment += 1
        index_assignment %= len(list_players_in_game)
        small_blind = list_players_in_game[index_assignment]
        small_blind.special_attr.append('small blind')
        index_assignment += 1
        index_assignment %= len(list_players_in_game)
        big_blind = list_players_in_game[index_assignment]
        big_blind.special_attr.append('big blind')
        index_assignment += 1
        index_assignment %= len(list_players_in_game)
        first_actor = list_players_in_game[index_assignment]
        first_actor.special_attr.append('first actor')
        list_players_in_game.append(list_players_in_game.pop(0))

    def show_suit(self):
        return f"{self.suit}"

    def show_value(self):
        return f"{self.value}"

    def hand_ranking(self):
        player_community_cards = Player.cards, self.cards
        all_possible_combi = itertools.combinations(player_community_cards, 5)
        score1 = 0
        score2 = 0

        for i in all_possible_combi:
            suit_list = []
            value_list = []
            for card in i :
                suit_list.append(card.suit)
                value_list.append(card.value)

        value_counter = dict(Counter(value_list))
        suit_counter = dict(Counter(suit_list))
        value_sorted_set = sorted(set(int(value_list)))

        #2 of a kind, 1
        pair_values = []
        pair_value = int
        pair_present = False
        for v, count in value_counter.items():
            if count == 2:
                pair_values.append(v)
                pair_value = v
                pair_present = True

    #3 of a kind, 2
        three_pair_value = int
        three_pair_present = False
        for v, count in value_counter.items():
            if count == 3:
                three_pair_value = v
                three_pair_present = True

    #straight, 3
#    for i in range(len(value_sorted_set)):
 #       for card in value_sorted_set:
  #         if card[i] - card[i-1] == 1 and card[i-1] - card[i-2] == 1 and card[i-2] - card[i-3] == 1 and card[i-3] - card[i-4] == 1:
   #             print('straight')

    #flush, 4
    #full house, 5
    #4 of a kind, 6
        four_pair_value = int
        four_pair_present = False
        for v, count in value_counter.items():
            if count == 4:
                four_pair_value = v
                four_pair_present = True

    #straight flush, 7
    #royal flush, 8