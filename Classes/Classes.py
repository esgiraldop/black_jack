import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def __str__(self):
        return f'this deck has {len(self.all_cards)} cards'

    def shuffle(self):
        return random.shuffle(self.all_cards)

    def deal_one(self):
        # Method to be used when any of the player selects "hit"
        return self.all_cards.pop(0)

    def deal_two(self):
        # Method to be used when dealing two cards for both players at the beginning of the match
        two_cards = []
        for i in range(2):
            two_cards.append(self.all_cards.pop(i))
        return two_cards

    def take_cards(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

class Dealer:

    def __init__(self,cards):
        # Takes the first two cards from Deck
        self.cards = cards
        self.name = 'Dealer'

    def take_card(self,card):
        # Takes one card from the deck when hits
        self.cards.append(card)

    def give_cards(self):
        cards_to_give = self.cards.copy()
        self.cards.clear()
        return cards_to_give  # returns a list, which must be appended to deck with extend() method

    def show_one_card(self):
        # shows one card only. Method only to be used for the Dealer
        print(self.cards[0])

    def show_all_cards(self):
        # shows all cards. Player can only see all Dealer's cards after hitting "stay"
        [print(i) for i in self.cards];

    def sum_values(self):
        # sum the values of all the cards the player has
        return sum([i.value for i in self.cards])

class Player(Dealer): # Inherits all the methods and attributes from Dealer

    def __init__(self,cards):
        # Takes the first two cards from Deck
        self.cards = cards
        self.name = 'Player'
        # Whn match starts, Player starts with 1000 dolars
        self.bankroll = 1000

    def __str__(self):
        return f"Player has {self.bankroll} dolars left"

    def bet_money(self,bet_money):
        self.bankroll = self.bankroll - bet_money
        print(f"Player has {self.bankroll} dolars left")

    def receive_money(self, money_in):
        self.bankroll = self.bankroll + money_in
        print(f"Player has {self.bankroll} dolars left")

class Table():

    def __init__(self):
        self.bet_ammount = 0 #Table starts with zero dolars on it

    def __str__(self):
        return f"Ammount of money in the table: {self.bet_ammount} dolars"

    def reinit(self) -> object:
        self.bet_ammount = 0

    def bet_money(self, bet_ammount):
        self.bet_ammount = bet_ammount

    def withdraw_money(self):
        money_out = self.bet_ammount
        self.reinit()
        return money_out
