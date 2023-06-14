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


def select_deck_for_ai():
    ai_deck = []
    deck_Index = random.randint(0, 4)
    if deck_Index == 0:
        for card in Cards.deckone:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            ai_deck.append(new_card)
        return ai_deck
    elif deck_Index == 1:
        for card in Cards.decktwo:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            ai_deck.append(new_card)
        return ai_deck
    elif deck_Index == 2:
        for card in Cards.deckthree:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            ai_deck.append(new_card)
        return ai_deck
    elif deck_Index == 3:
        for card in Cards.deckfour:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            ai_deck.append(new_card)
        return ai_deck
    elif deck_Index == 4:
        for card in Cards.deckfive:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            ai_deck.append(new_card)
        return ai_deck


def write_deck(deck):
    for card_index, card in enumerate(deck):
        print(card_index, card.name)


def select_deck(deck_Index):
    player_deck = []
    if deck_Index == 0:
        for card in Cards.deckone:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            player_deck.append(new_card)
        return player_deck
    elif deck_Index == 1:
        for card in Cards.decktwo:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            player_deck.append(new_card)
        return player_deck
    elif deck_Index == 2:
        for card in Cards.deckthree:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            player_deck.append(new_card)
        return player_deck
    elif deck_Index == 3:
        for card in Cards.deckfour:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            player_deck.append(new_card)
        return player_deck
    elif deck_Index == 4:
        for card in Cards.deckfive:
            new_card = Cards.Card(card.name, card.description,
                                  card.mana, card.attack, card.function)
            player_deck.append(new_card)
        return player_deck


def find_least_powerful_field(curret_player):
    smallest_value = min(curret_player.fieldSum)
    smallest_indices = [i for i, value in enumerate(
        curret_player.fieldSum) if value == smallest_value]

    # If there are multiple smallest indices, choose one randomly
    random_index = random.choice(smallest_indices)
    return random_index


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
