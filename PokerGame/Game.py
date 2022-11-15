import itertools
from collections import Counter
from Cards import Deck
from Player import Player


class Game(object):
    def __init__(self, name, list_of_players):
        self.game_over = False
        self.need_raise = False
        self.active_player = Player("Hubert")
        self.possible_action = []
        self.cards = []
        self.pot = 0
        self.pot_dict = {}
        self.list_of_players = []
        self.dealer = Player('Nick')
        self.small_blind = Player('Anne')
        self.big_blind = Player('Sara')
        self.first_actor = Player('Wout')
        self.winners = []
        self.deck = Deck()
        self.score_of_possible_winners = []
        self.players_not_out = list(list_of_players)

    def create_list_of_player(self):
        player_names = []
        q = int(input('Enter amount of players'))
        if q >=9 or q <= 1:
            raise ValueError
        else:
            for i in range(0, q):
                player_names.append(input(f'Enter player {i+1} name'))

            for i in range(len(player_names)):
                self.list_of_players.append(Player(player_names[i]))

    def check_apply_settings(self):
        smallblind_amount = int(input('Small blind amount'))
        bigblind_amount = smallblind_amount*2
        chip_amount = int(input('Chip amount'))

        if chip_amount <= 0 or smallblind_amount >= chip_amount:
            raise ValueError
        else:
            Player.chips = chip_amount
            self.pot_dict['sb_stake'] = smallblind_amount
            self.pot_dict['bb_stake'] = bigblind_amount

    def possible_actions(self):
        if self.active_player.chips == 0:
            self.possible_action.append('None')
        else:
            for player in self.players_not_out:
                self.possible_action.append('fold')
            if self.active_player.stake_gap == 0:
                self.possible_action.append('check')
            if self.active_player.stake_gap != 0:
                self.possible_action.append('call')
            self.possible_action.append('raise')

    def show_comunity_cards(self):
        print(f'Comunity cards: {self.cards}')
    
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
        
    def establish_player_attr(self):
        index_assignment = 0
        self.first_actor = self.players_not_out[index_assignment]
        self.first_actor.special_attr.append('first actor')
        index_assignment += 1
        index_assignment %= len(self.players_not_out)
        self.small_blind = self.players_not_out[index_assignment]
        self.small_blind.special_attr.append('small blind')
        index_assignment += 1
        index_assignment %= len(self.players_not_out)
        self.big_blind = self.players_not_out[index_assignment]
        self.big_blind.special_attr.append('big blind')
        index_assignment += 1
        index_assignment %= len(self.players_not_out)
        self.dealer = self.players_not_out[index_assignment]
        self.dealer.special_attr.append('dealer')
        self.players_not_out.append(self.players_not_out.pop(0))

    def show_suit(self):
        return f"{self.suit}"

    def show_value(self):
        return f"{self.value}"

    def hand_ranking(self, player):
        player_community_cards_object = player.cards + self.cards
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
        best_score = max(all_possible_scores_array)
        player.score = best_score

    def score_all_players(self):
        for player in self.players_not_out:
            self.hand_ranking(self, player)

    def check_(self):
        pass

    def call_(self):
        pass

    def raise_(self):
        pass

    def allin_(self):
        pass
    
    def fold_(self):
        pass

    def roundinfo(self):
        pass

    def act_one(self):
        pass