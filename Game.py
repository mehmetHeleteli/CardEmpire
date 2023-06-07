import Cards
import random

# Create a function that creates a deck of cards


def create_deck():
    deck = []
    for i in range(0, 10):
        deck.append(Cards.drawable_cards[random.randint(
            0, len(Cards.drawable_cards) - 1)])
    return deck

# Create a function that shuffles a deck of cards


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Create a function that select a deck from a list of decks


def select_deck_one():  # Testing
    return Cards.deckone


def calculate_field_powers(curret_player):
    field_powers = {}

    # Calculate field powers for the current player
    current_field_sums = [sum(card.attack for card in field)
                          for field in curret_player.fields]
    field_powers[curret_player.name] = current_field_sums

    return field_powers


def get_most_powerful_card(cardslist):
    # Find the most powerful card and return index of the card
    for card in cardslist:
        if card.attack == max(card.attack for card in cardslist):
            return card


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
