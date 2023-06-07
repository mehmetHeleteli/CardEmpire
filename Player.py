# Define your Player class, create_deck(), shuffle_deck(), and other game logic functions here
class PlayerClass:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []
        self.fields = [['field1', []], ['field2', []], ['field3', []]]
        self.max_mana = 1
        self.manapool = 1
        self.turn_ended = False
        self.wonCount = 0
        self.fieldSum = [0, 0, 0]
        self.fieldCardCount = [0, 0, 0]

    # Create a method that draws a card from the deck
    def draw(self):
        if len(self.deck) > 0:
            self.hand.append(self.deck.pop())

    # Create a method that plays a card from the hand
    def play(self, card_index, field_index):
        if 0 <= field_index < len(self.fields) and 0 <= card_index < len(self.hand):
            card = self.hand[card_index]
            self.fields[field_index][1].append(card)
            self.hand.pop(card_index)
            self.fieldCardCount[field_index] += 1
            self.fieldSum[field_index] += card.attack
            
            # Invoke the card's function
            card.useCard(field_index, self)
