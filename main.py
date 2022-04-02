import random
from Classes.functions import *


play_again = True

while play_again:
    # Game starts from scratch
    deck.shuffle()
    round = 0
    game_on = True

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
        table.bet_money(int(bet_ammount))
        # show_cards(show_all_cards=False)

        # Checking if, upon cards are dealt, any of the players get a bust or a 21
        if check_bust_or_21_player():
            if check_lose():
                break
            continue

        if check_bust_or_21_dealer():
            if check_lose():
                break
            continue

        while player_hits:
            # Player chooses to hit (and another card is dealt), or stay

            show_cards(show_all_cards=False)
            if hit_or_stay() == False:
                break

            player.take_card(deck.deal_one())
            if check_bust_or_21_player():
                show_cards(show_all_cards=True)
                dealer_hits = False
                break

        if check_lose():
            break # In case player busts. there is the need to check if he lost the game

        while dealer_hits:
            # Dealer randomly chooses to hit or stay
            dealer_hits = [True, False]
            random.shuffle(dealer_hits)
            show_cards(show_all_cards=True)
            if dealer_hits[0] == False:
                break
            else:
                dealer_hits == True

            dealer.take_card(deck.deal_one())
            if check_bust_or_21_dealer() == True:
                show_cards(show_all_cards=True)
                dealer_hits = False
                break

        # Dealer can lose a round, but never loses a game because its money is infinite

        # Battle between player and dealer

        if dealer_hits: # This means player or dealer either busted or scored a 21 so nothing inside this conditional
                            # needs to be run
            if check_push():
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

            else:
                # push! which means the round ends in a draw. player is refunded the bet ammount
                print('Push!')
                player.receive_money(table.withdraw_money())

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

        if check_lose():
            break

        if play_again() == False:
            play_again = False
            break

    if play_again == False:
        print('Thanks for playing Black Jack!')




