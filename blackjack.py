import cards
import random

PLAYER_INDEX = 0
ACES_INDEX = 1
SCORE_INDEX = 2
player_hand = [{"player": "player"}, {"aces": 0}, {'score': 0}]

dealer_hand = [{"player": "dealer"}, {"aces": 0}, {'score': 0}]
deck = cards.deck
aces = cards.aces


def shuffle_deck(deck_arg):
    """
    Shuffles the given deck.

    :param deck_arg: The deck of cards to be shuffled.
    :return: None
    """
    random.shuffle(deck_arg)


def deal(num_cards, deck_arg, hand):
    """
    :param num_cards: The number of cards to be dealt from the deck.
    :param deck_arg: The deck from which the cards will be dealt.
    :param hand: The hand to which the cards will be added.

    :return: None

    This method deals the specified number of cards from the deck to the
    hand. It removes the dealt cards from the deck.

    If the player in the hand is the dealer, it will print the dealer's card
    that is showing and their known score. If the player in the hand is the
    player, it will print the current state of the player's hand.
    """
    for i in range(num_cards):
        card = deck_arg[0]
        hand.append(card)
        hand[SCORE_INDEX]['score'] += card["value"]
        if card["value"] == 1:
            hand[ACES_INDEX]['aces'] += 1
            check_aces(hand)
        del deck_arg[0]

    if hand[PLAYER_INDEX]["player"] == "dealer":
        print(f"Dealer has {hand[3]['name']} showing.")
        print(f"His known score is {hand[3]['value']}")
    elif hand[PLAYER_INDEX]["player"] == "player":
        print(f"Player has {hand_to_string(hand)} ")


# def calculate_hand_value(hand):
#     """
#     Calculate the total value of a hand in a card game.
#
#     :param hand: A list representing the hand of cards.
#     :return: The total value of the hand.
#
#     The method calculates the score of the player's hand by summing the
#     values of each card in the hand. If there are any aces present in the
#     hand, the method keeps track of the number of aces. If the player is the
#     one with the hand, the method asks the player if they want their ace
#     card to count as 11. If so, it increases the score by 10 but checks for
#     a possible bust. If the player is the dealer, the method randomly
#     decides whether to increase the score by 10. It also checks for a
#     possible bust in this case.
#
#     Note: The method assumes the existence of certain variables: aces,
#     SCORE, ACES, PLAYER.
#
# Example usage: hand = [{'name': 'ace', 'value': 1}, {'name': '9', 'value':
# 9}, {'name': 'king', 'value': 10}] value = calculate_hand_value(hand)
# print(value)  # Output: 20 """ for card in range(3, len(player_hand)):
# hand[SCORE_INDEX]['score'] += player_hand[card]['value'] if player_hand[
# card]['name'] in aces: hand[ACES_INDEX]['aces'] += 1 if hand[SCORE_INDEX][
# 'score'] + 10 <= 21 and hand[ACES_INDEX]['aces'] and \ hand[PLAYER_INDEX][
# "player"] == 'player':
#
# choice = input("Would you like your ace card to count as 11? y or n ")
# while choice != 'y' and choice != 'n': choice = input('Please input y or
# n.') if choice == 'y': hand[SCORE_INDEX]['score'] += 10 if hand[
# SCORE_INDEX]['score'] > 21: print("This will result in a bust. Ace will
# count as a 1") hand[SCORE_INDEX]['score'] -= 10 elif (hand[SCORE_INDEX][
# 'score'] + 10 <= 21 and hand[ACES_INDEX]['aces'] and hand[PLAYER_INDEX][
# "player"] == "dealer"): choice = random.choice(['y', 'n']) if choice ==
# 'y': hand[SCORE_INDEX]['score'] += 10 if hand[SCORE_INDEX]['score'] > 21:
# hand[SCORE_INDEX]['score'] -= 10 return hand[SCORE_INDEX]['score']


def hand_to_string(hand):
    """
    Converts a hand of cards to a string representation

    :param hand: A list of cards in the hand
    :return: A string representation of the hand

    """

    hand_string = ""
    for card in range(3, len(hand)):
        hand_string += "".join(hand[card]['name'])
        if card < len(hand) - 1:
            hand_string += ", "
    return hand_string


def check_aces(hand):
    if hand[ACES_INDEX]['aces'] and hand[SCORE_INDEX]['score'] < 12:
        hand[SCORE_INDEX]['score'] += 10


def turn(hand):
    """
    :param hand: A list representing the current player's hand :return: If
    the player wins, returns True. Otherwise, returns the calculated hand
    value.

    This method is used to simulate a turn in a blackjack game. It takes in
    the current hand of the player and performs various actions based on the
    game logic.

    The method first checks if it's the player's turn and prints a message
    accordingly. It then displays the current hand of the player and
    calculates the hand value. The hand value is stored * in the SCORE_INDEX
    of the hand list.

    If the player's hand value is 21, a message is printed indicating that
    the player has a blackjack and the method returns True to signify a
    player win.

    If the player's hand value is less than 21, the method enters a loop
    where the player is prompted to choose whether to hit or stand. If the
    player chooses to hit, a card is dealt to * the player's hand and the
    updated hand and hand value are printed. If the hand value exceeds 21,
    a message is printed indicating that the player has busted and the
    method sets player *_bust to True.

    If the player's hand value is equal to or exceeds 21, the method exits
    the loop and enters another loop where the dealer's hand is updated
    until the hand value is greater than or equal * to 18. A card is dealt
    to the dealer's hand in each iteration and the updated hand and hand
    value are printed. If the dealer's hand value exceeds 21, a message is
    printed indicating * that the dealer has busted and the method returns
    True to signify a player win.

    Finally, if none of the win conditions are met, the method returns the
    calculated hand value of the player's hand.

    Note: The method assumes the existence of the functions
    `calculate_hand_value(hand)` and `deal(num_cards, deck, hand)`. The
    function `hand_to_string(hand)` is used for printing the hand *, but its
    implementation is not provided.

    Example usage:
        hand = [
            {"player": "player"},
            {"score": 0},
            # Add other elements of the hand as per the required format
        ]
        result = turn(hand)
        if result == True:
            print("Player wins!")
        else:
            print("Player's hand value:", result)
    """
    player_bust = False
    result = ""
    play = ""
    if hand[PLAYER_INDEX]["player"] == "player":
        print("It's your play.")
        print(f"Your current hand is:{hand_to_string(hand)}")
        print(f"That gives you a {hand[SCORE_INDEX]['score']}")

        if hand[SCORE_INDEX]['score'] == 21:
            print(f"Your hand is {hand_to_string(hand)}")
            print({"You got a blackjack! You win!"})

            result = "player wins"
        # while the players hand is < 21 give the option to hit or stand
        while (hand[SCORE_INDEX]['score'] < 21 and not player_bust and play
               != "stand"):

            play = input("Would you like to hit or stand? (hit or stand): ")
            if play == 'hit':
                deal(1, deck, hand)

                print(f"Your hand is {hand_to_string(hand)}")
                print(f"That give you a {hand[SCORE_INDEX]['score']}")
            if hand[SCORE_INDEX]["score"] > 21:
                print("You busted! Dealer wins!")
                player_bust = True
                result = "player bust"
    # dealers turn
    else:
        while hand[SCORE_INDEX]['score'] < 18:
            print("Dealer takes a card.")
            deal(1, deck, hand)
            print(f"Dealer's hand is {hand_to_string(hand)}")
            print(f"That gives dealer a {hand[SCORE_INDEX]['score']}")
            if hand[SCORE_INDEX]['score'] > 21:
                print("Dealer busted! You win!")
                result = "dealer bust"

    return result


def calculate_winner(dealer_hand, player_hand):
    """
    Calculate the winner of the game based on the scores of the dealer's
     and player's hands and prints the resu.

    :param dealer_hand: The dealer's hand.
    :param player_hand: The player's hand.
    :return: None
    """
    print(f"Dealer has {dealer_hand[SCORE_INDEX]['score']}. You have "
          f"{player_hand[SCORE_INDEX]['score']}. ")
    if dealer_hand[SCORE_INDEX]['score'] < player_hand[SCORE_INDEX]['score'] < 22:

        print("player wins")
    elif player_hand[SCORE_INDEX]['score'] < dealer_hand[SCORE_INDEX][
        'score'] < 22:
        print("Dealer wins")
    elif dealer_hand[SCORE_INDEX]['score'] == player_hand[SCORE_INDEX][
        'score']:
        print("It's a draw")
    elif player_hand[SCORE_INDEX]['score'] > 21:
        print("You busted! Dealer wins!")
    elif dealer_hand[SCORE_INDEX]['score'] > 21:
        print("Dealer busted! You win!")

def reset_game(dealer_hand, player_hand, deck):
    # return cards from both hands to deck. reset scores and ace counts to zero

    for card in range(3, len(dealer_hand)):
        deck.append(dealer_hand[card])

    for card in range(3, len(player_hand)):
        deck.append(player_hand[card])

    for card in range(3, len(player_hand)):
        del player_hand[3]

    for card in range(3, len(dealer_hand)):
        del dealer_hand[3]


    player_hand[ACES_INDEX]['aces'] = 0
    dealer_hand[ACES_INDEX]['aces'] = 0

    player_hand[SCORE_INDEX]['score'] = 0
    dealer_hand[SCORE_INDEX]['score'] = 0


def main():
    print("Welcome to Blackjack!")
    shuffle_deck(deck)
    deal(2, deck, player_hand)
    deal(2, deck, dealer_hand)

    result = turn(player_hand)
    if result != "player wins" and result != "player bust":
        result = turn(dealer_hand)
    if result != "dealer bust":
        calculate_winner(dealer_hand, player_hand)
    play_again = ""
    while play_again != "y" and play_again != "n":
        play_again = input("Do you want to play again? y or n")
        play_again = play_again.lower()
    if play_again == "y":
        reset_game(dealer_hand, player_hand, deck)
        main()
    else:
        print("Thanks for playing!")


main()
