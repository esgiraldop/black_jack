import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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

    def deal_one(self, obj):
        # Method to be used when any of the player selects "hit"
        # "obj" can be player or dealer
        card = self.all_cards.pop(0)
        if card.rank == 'Ace':
            card.value = self.ask_ace_value(obj)

        return card

    def deal_two(self, obj):
        # Method to be used when dealing two cards for both players at the beginning of the match
        two_cards = []
        for i in range(2):
            two_cards.append(self.all_cards.pop(i))
        return two_cards

    def ask_ace_value(self, obj):
        # If obj is player, asks to choose 11 or 1 for the value of Ace. If obj is dealer, randomly chooses the value
            # for ace
        if obj.name == 'Player':
            # Player is asked to choose between '1' or '11' for ace
            value = 0
            while value not in [1, 11]:
                try:
                    value = int(input('Please chose between \'1\' or \'11\' for the value of Ace: '))
                except:
                    print('Only numerical integer values can be entered')
                    value = 0
                else:
                    if value not in [1, 11]:
                        print('Only \'1\' or \'11\' can be entered.')
                        value = 0

        elif obj.name == 'Dealer':
            # Dealer randomly chooses between 1 or 11
            values = [1, 11]
            random.shuffle(values)
            value = values[0]

        return value

    def take_cards(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

class Dealer:

    def __init__(self):
        self.name = 'Dealer'

    def take_two_cards(self, cards):
        # Takes the first two cards from Deck
        self.cards = cards

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

    def __init__(self):
        self.name = 'Player'
        # When match starts, Player starts with 1000 dollars
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

if __name__ == '__main__':
    pass