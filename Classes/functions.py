from Classes.Classes import *

def ask_4_bet(player):
    # Returns the amount bet by the player
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

    return bet_ammount


def check_lose(player):
    # Returns True if player ran out of funds or False otherwise

    if player.bankroll <= 0: # just for checking for error, i will put the '<', but the bankroll should not have negative values
        print(f'Player has {player.bankroll} dollars left.Player loses the game')
        return True

    return False

def check_cashOut():
    # Return True if player cashes out. False otherwise
    cash_out = 1
    while cash_out not in ['y', 'n']:
        cash_out = input('Do you want to cash out? (y/n): ')

        if cash_out not in ['y', 'n']:
            print('Please enter a valid option.\n')

    if cash_out == 'y':
        print('Player cashes out.\nHouse wins!')
        return True

    return False

def check_push(player):
    # Checks if both players got the same result
    if player.sum_values() == dealer.sum_values():
        print('Push!')
        player.receive_money(table.withdraw_money()) # If there is a push, player takes back the bet ammount
        table.reinit()
        return True

def check_bust_player(player):
    # returns True if it occurs "bust"
    if player.sum_values() > 21:
        print('Player busts! Player loses the round!')
        table.reinit() # Player does not recover the bet money
        return True

    return False

def check_21_player(player):
    # returns True if it occurs "21"
    if player.sum_values() == 21:
        print('21! Player wins the round!')
        player.receive_money(table.withdraw_money() * 2)  # If player wins the round, receives twice the bet ammount
        table.reinit()
        return True

    return False

def check_bust_or_21_player(player):
    # returns True if it occurs "21" or "bust" (Which are conditions for breaking any while containing this function).
    # Returns False if "no bust" occurs
    if check_bust_player(player):
        return True
    elif check_21_player(playerr):
        return True
    else:
        return False

def check_bust_dealer(dealer):
    # returns True if it occurs "bust"
    if dealer.sum_values()> 21:
        print('Dealer busts! Player wins the round!')
        player.receive_money(table.withdraw_money() * 2) # If player wins the round, receives twice the bet amount
        table.reinit()
        return True

    return False

def check_21_dealer(dealer):
    # returns True if it occurs "21", False if not, or "push" if the result is 21, but the player also scored 21
    if dealer.sum_values() == 21:
        if check_push():
            return 'push'
        else:
            print('21! Dealer wins the round!')
            table.reinit()
            return True

    return False

def check_bust_or_21_dealer(dealer):
    # returns True if it occurs "21" or "bust" (Which are conditions for breaking any while containing this function).
    # Returns False if "no bust" occurs
    if check_21_dealer(dealer):
        return True

    elif check_bust_dealer(dealer):
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



def play_again_func():
    # returns False if player does not want to play another round and True otherwise
    answer = False
    while answer not in ['y', 'n']:
        answer = input("Do you want to play again? (y/n): ")
        if answer not in ['y', 'n']:
            print("Please enter a valid value")

    if answer == 'y':
        return True

    return False

def show_cards(player, dealer, show_all_cards=False):
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

if __name__ == '__main__':
    pass