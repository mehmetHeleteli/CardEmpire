import Cards
import random

# Create a function that creates a deck of cards


def create_deck():
    deck = []
    for i in range(0, 10):
        deck.append(Cards.cards[random.randint(0, len(Cards.cards) - 1)])
    return deck

# Create a function that shuffles a deck of cards


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Create a function that calculates the sum of the cards on the field


def calculate_field_powers(curret_player):
    field_powers = {}

    # Calculate field powers for the current player
    current_field_sums = [sum(card.attack for card in field)
                          for field in curret_player.fields]
    field_powers[curret_player.name] = current_field_sums

    return field_powers


def get_most_powerful_card(cardslist):
    # Find the most powerful card and return index of the card
    most_powerful_card = cardslist[0]
    for card in cardslist:
        if card.attack > most_powerful_card.attack:
            most_powerful_card = card
    return most_powerful_card


def get_hand_card_list(player):
    hand_card_list = []
    for card in player.hand:
        hand_card_list.append(card.name)
    return hand_card_list


def ask_for_card(player):
    card = input("Which card do you want to play? ")
    for card in player.hand:
        if card.name == card:
            return card
    return None
