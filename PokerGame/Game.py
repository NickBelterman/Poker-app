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

    def hand_ranking(game, player):
        player_community_cards_object = player.cards + game.cards
        all_possible_5_card_combination = list(itertools.combinations(player_community_cards_object, 5))
        low_value_cards = []
        all_possible_scores_array = []


        for i in all_possible_5_card_combination:
            suit_list = []
            value_list = []
            for card in i:
                suit_list.append(card.suit)
                value_list.append(card.value)
            value_counter = dict(Counter(value_list))
            score1 = 0
            score2 = 0
            score3 = 0
            score4 = 0
            score5 = 0
            score6 = 0
            score7 = 0
            score8 = 0

            #2 of a kind, 1
            pair_values = []
            pair_value = int
            pair_present = False
            for v, count in value_counter.items():
                if count == 2:
                    pair_values.append(v)
                    pair_value = v
                    pair_present = True

            if pair_present:
                for v in value_list:
                    if v not in pair_values:
                        low_value_cards.append(v)

                low_value_cards = list(reversed(sorted(low_value_cards)))
                if len(pair_values) == 1:
                    score1 = 1
                    score2 = pair_value
                    try:
                        score3 = low_value_cards.pop(0)
                        score4 = low_value_cards.pop(0)
                        score5 = low_value_cards.pop(0)
                        score6 = low_value_cards.pop(0)
                        score7 = low_value_cards.pop(0)
                        score8 = low_value_cards.pop(0)
                    except IndexError:
                        pass
        
                if len(set(pair_values)) == 2:
                    pair_values = list(reversed(sorted(pair_values)))
                    score1 = 2
                    score2 = pair_values.pop(0)
                    score3 = pair_values.pop(0)
                    try:
                        score4 = low_value_cards.pop(0)
                        score5 = low_value_cards.pop(0)
                        score6 = low_value_cards.pop(0)
                        score7 = low_value_cards.pop(0)
                        score8 = low_value_cards.pop(0)                    
                    except IndexError:
                        pass


                #3 of a kind, 2
                three_pair_value = int
                three_pair_present = False
                for v, count in value_counter.items():
                    if count == 3:
                        three_pair_value = v
                        three_pair_present = True
                        score1 = 3
                        score2 = three_pair_value
                        if three_pair_present:
                            for v in value_list:
                                if v != three_pair_value:
                                    low_value_cards.append(v)
                                    low_value_cards = reversed(sorted(low_value_cards))
                                    try:
                                        score3 = low_value_cards.pop(0)
                                        score4 = low_value_cards.pop(0)
                                        score5 = low_value_cards.pop(0)
                                        score6 = low_value_cards.pop(0)
                                        score7 = low_value_cards.pop(0)
                                        score8 = low_value_cards.pop(0)   
                                    except IndexError:
                                        pass

                    #straight, 3 
                straight_present = False
                if sorted(value_list) == list(range(min(value_list), max(value_list) + 1)):
                    straight_present = True
                    score1 = 4
                    score2 = max(value_list)

                    #flush, 4
                flush_present = False
                if len(set(suit_list)) == 1:
                    flush_present = True
                    score1 = 5
                    score2 = max(value_list)
            
                    #full house, 5
                if pair_present and three_pair_present:
                    score1 = 6
                    score2 = three_pair_value
                    score3 = pair_value

                    #4 of a kind, 6
                four_pair_value = int
                four_pair_present = False
                for v, count in value_counter.items():
                    if count == 4:
                        four_pair_value = v
                        four_pair_present = True
                        score1 = 7
                        score2 = four_pair_value
                        for v in four_pair_value:
                            if v not in four_pair_value:
                                low_value_cards.append(v)
                                low_value_cards = reversed(sorted(low_value_cards))
                                try:
                                    score3 = low_value_cards.pop(0)
                                    score4 = low_value_cards.pop(0)
                                    score5 = low_value_cards.pop(0)
                                except IndexError:
                                    pass
                
                    #straight flush, 7
                if straight_present and flush_present:
                    score1 = 8
                    score2 = max(value_list)
                    #royal flush, 8
                if flush_present and value_list == [11, 12, 13, 14, 15]:
                    score1 = 9

            all_possible_scores_array.append([score1, score2, score3, score4, score5, score6, score7, score8])
        return all_possible_scores_array