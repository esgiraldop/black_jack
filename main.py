import random
from Classes.functions import *
from Classes.Classes import *

deck = Deck()
table = Table()

play_again = True

while play_again:
    # Game starts from scratch
    deck.shuffle()
    round = 1
    game_on = True
    # Initializing player and dealer
    player = Player()
    dealer = Dealer()

    while game_on:
        # Dealer or Player has won and another round starts
        print(f'$$$$$$$$$$$')
        print(f'Round {round}')
        print(f'$$$$$$$$$$$')

        player_hits = True
        dealer_hits = True

        print(player)
        bet_ammount = -1

        while bet_ammount < 0 or bet_ammount > player.bankroll or bet_ammount != int(bet_ammount):

            try:
                bet_ammount = float(input("How much do you want to bet: "))
            except:
                print('Only numerical values can be entered')
                bet_ammount = -1
            else:
                if bet_ammount != int(bet_ammount):
                    print('Only integer values can be entered')
                    continue

                elif bet_ammount < 0:
                    print('Please enter a positive number')
                    continue

                elif bet_ammount > player.bankroll:
                    print('Not enough funds!')
                    print(player)
                    continue
                print('\n')
                print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                print(f'$$$$ Player has bet {bet_ammount} dollars $$$$')
                print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                print('\n')

        player.bet_money(int(bet_ammount))
        player.take_two_cards(deck.deal_two())
        dealer.take_two_cards(deck.deal_two())
        table.bet_money(int(bet_ammount))

        # Checking if, upon cards are dealt, any of the players get a bust or a 21
        # To test bust --> player.take_card(Card('Hearts', 'Ace')) --> player.sum_values()
        if player.sum_values() > 21:
            # Neither player nor dealer cannot bust in the first two dealt cards
            # This will never happen if it is not possible the first two dealt cards add up more than 20
            print('First two dealt cards added up more than 21. Redealing again...')
            player.receive_money(table.withdraw_money())
        elif check_21_player(player):
            # Player can actually score a 21 in the first two dealt cards, but this will never happen if it is not
                # possible the first two dealt cards add up more than 20
            if check_21_dealer(dealer):
                if check_21_dealer(dealer):
                    break
            elif check_bust_dealer(dealer):
                player_hits = False
                dealer_hits = False
        else: # Game continues
            while player_hits:
                # Player chooses to hit (and another card is dealt), or stay

                show_cards(show_all_cards=False, player, dealer)
                if hit_or_stay() == False:
                    break

                player.take_card(deck.deal_one())
                if check_bust_player(player):
                    show_cards(show_all_cards=True, player, dealer)
                    dealer_hits = False
                    break
                elif check_21_player(player):
                    show_cards(show_all_cards=True, player, dealer)
                    break

            if check_lose(player):
                break # In case player busts. there is the need to check if he lost the game

            while dealer_hits:
                # Dealer randomly chooses to hit or stay
                dealer_hits = [True, False]
                random.shuffle(dealer_hits)
                show_cards(show_all_cards=True, player, dealer)
                if dealer_hits[0] == False:
                    break
                else:
                    dealer_hits == True

                dealer.take_card(deck.deal_one())
                if check_bust_dealer(dealer):
                    show_cards(show_all_cards=True, player, dealer)
                    dealer_hits = False
                    break
                elif check_21_dealer():
                    show_cards(show_all_cards=True, player, dealer)
                    break

            # Dealer can lose a round, but never loses a game because its money is infinite

            # Battle between player and dealer
            if dealer_hits: # This means player or dealer either busted or scored a 21 so nothing inside this conditional
                                # needs to be run
                if check_push(player):
                    break
                elif player.sum_values() > dealer.sum_values():
                    # player wins the round. player earns twice the bet ammount
                    print('Player wins the round!')
                    player.receive_money(table.withdraw_money()*2)
                    table.reinit()

                elif player.sum_values() < dealer.sum_values():
                    # dealer wins the round. player loses the bet ammount.
                    print('Player loses the round!')
                    table.reinit() # As the money was already extracted from the bankroll,

        # Before finishing the round, player and dealer return their cards to the deck

        deck.take_cards(player.give_cards())
        deck.take_cards(dealer.give_cards())

        round += 1
        if round == 10:
            round = 0
            print('\n')
            print('Shuffling deck...')
            print('\n')
            deck.shuffle()

        if check_lose(player):
            break

        if play_again_func() == False:
            play_again = False
            break

    if play_again == False:
        print('Thanks for playing Black Jack!')




