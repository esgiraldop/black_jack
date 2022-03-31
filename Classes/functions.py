from Classes.Classes import *

deck = Deck()
deck.shuffle()
table = Table()
player = Player(deck.deal_two())
dealer = Dealer(deck.deal_two())

def check_lose():
    # Returns True if player ran out of funds or False otherwise

    if player.bankroll <= 0: # just for checking for error, i will put the '<', but the bankroll should not have negative values
        print(f'Player has {player.bankroll} dollars left.Player loses the game')
        return True

    return False

def check_push():
    # Checks if both players got the same result
    if player.sum_values() == dealer.sum_values():
        print('Push!')
        player.receive_money(table.withdraw_money()) # If there is a push, player takes back the bet ammount
        table.reinit()
        return True

def check_bust_or_21_player():
    # returns True if it occurs "21" or "bust" (Which are conditions for breaking any while containing this function).
    # Returns False if "no bust" occurs
    if player.sum_values() > 21:
        if check_push(): # Checking push in case the other player has also busted
            return False
        print('Player busts! Player loses the round!')
        table.reinit()
        return True

    elif player.sum_values() == 21:
        if check_push(): # Checking push in case the other player has also scored exactly 21
            return False
        print('21! Player wins the round!')
        player.receive_money(table.withdraw_money() * 2) # If player wins the round, receives twice the bet ammount
        table.reinit()
        return True

    else:
        return False

def check_bust_or_21_dealer():
    # returns True if it occurs "21" or "bust" (Which are conditions for breaking any while containing this function).
    # Returns False if "no bust" occurs
    if dealer.sum_values()> 21:
        print('Dealer busts! Player wins the round!')
        player.receive_money(table.withdraw_money() * 2) # If player wins the round, receives twice the bet ammount
        table.reinit()
        return True

    elif dealer.sum_values() == 21:
        print('21! Dealer wins the round!')
        table.reinit()
        return True

    else:
        return False

def hit_or_stay():
    # returns True if player or dealer chooses to hit or False if decides to stay (False breaks any outter loop)
    loop = True

    while loop:
        hit_or_stay = input("Do you want to hit or stay? (h/s):")

        if hit_or_stay not in ['h', 's']:
            print('Please enter a correct value')
            loop = True
            continue

        loop = False

    if hit_or_stay == 'h':
        print('Player hits')
        return True

    print('Player stays')
    return False



def play_again():
    # returns False if player does not want to play another round and True otherwise
    answer = False
    while answer not in ['y', 'n']:

        answer = input("Do you want to play again? (y/n): ")
        if answer not in ['y', 'n']:
            print("Please enter a valid value")

    if answer == 'y':
        return True
    print('Thanks for playing Black Jack 21!')
    return answer

def show_cards(show_all_cards):
    # Function to display cards in table. If option = False, displays one card of the dealer only, if True, displays all cards
    print("------------------------")
    print("Player cards on table: ")
    player.show_all_cards()
    print("Value of the player cards is: ", player.sum_values())
    print("------------------------")
    print("Dealer cards on table: ")
    if show_all_cards == False:
        dealer.show_one_card()

    elif show_all_cards == True:
        dealer.show_all_cards()
        print("Value of the dealer cards is: ", dealer.sum_values())
    print('\n')