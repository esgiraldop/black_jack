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
        player_loses_game = False
        player_cashes_out = False

        print(player)

        if check_cashOut() == False:
            player.take_two_cards(deck.deal_two(player))
            dealer.take_two_cards(deck.deal_two(dealer))
            # Checking if, upon cards are dealt, any of the players get a bust or a 21
            # To test bust --> player.take_card(Card('Hearts', 'Ace')) --> player.sum_values()
            if player.sum_values() > 21 or dealer.sum_values() > 21:
                # Neither player nor dealer cannot bust in the first two dealt cards
                # This will never happen if it is not possible the first two dealt cards add up more than 20
                print('First two dealt cards added up more than 21. Redealing again...')
                player.receive_money(table.withdraw_money())
            else: # Game continues
                # Player's turn
                bet_ammount = ask_4_bet(player)
                player.bet_money(int(bet_ammount))
                table.bet_money(int(bet_ammount))

                while player_hits:
                    # Player chooses to hit (and another card is dealt), or stay
                    show_cards(player, dealer)
                    if hit_or_stay() == False:
                        break

                    player.take_card(deck.deal_one())
                    if check_bust_player(player):
                        show_cards(player, dealer)
                        dealer_hits = False
                        player_loses_game = check_lose(player)
                        break
                    elif check_21_player(player):
                        show_cards(player, dealer, show_all_cards=True)
                        break

                while dealer_hits:
                    # If player busted, then this block is not even run
                    # Dealer randomly chooses to hit or stay
                    dealer_hits = [True, False]
                    random.shuffle(dealer_hits)
                    show_cards(player, dealer, show_all_cards=True)
                    if dealer_hits[0] == False:
                        break
                    else:
                        dealer_hits == True

                    dealer.take_card(deck.deal_one())
                    if check_bust_dealer(dealer):
                        show_cards(player, dealer, show_all_cards=True)
                        dealer_hits = False
                        break
                    elif check_21_dealer():
                        show_cards(player, dealer, show_all_cards=True)
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

                if player_loses_game:
                    break # In case player busts. there is the need to check if he lost the game
        else:
            player_cashes_out = True
            break
        # Before finishing the round, player and dealer return their cards to the deck
        # All cards to deck
        deck.take_cards(player.give_cards())
        deck.take_cards(dealer.give_cards())

        round += 1
        if round == 10:
            round = 0
            print('\n')
            print('Shuffling deck...')
            print('\n')
            deck.shuffle()

        if player_loses_game:
            break

    play_again = play_again_func()

print('Thanks for playing Black Jack!')