
class Card:
    def __init__(self, name, description, mana, attack, function):
        self.name = name
        self.description = description
        self.mana = mana
        self.attack = attack
        self.function = function

    def useCard(self, fieldIndex):
        self.function(fieldIndex)


cards = []


def nothing(fieldIndex):
    pass


def hurremSultan(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldOneSum += 3
        print("3 Power added to field 1")
    elif fieldIndex == 1:
        current_player.fieldTwoSum += 3
        print("3 Power added to field 2")
    elif fieldIndex == 2:
        current_player.fieldThreeSum += 3
        print("3 Power added to field 3")


def asena(fieldIndex, current_player):
    current_player.manapool += 3
    print("3 Mana added")


'''
def lagimci(fieldIndex): # Passive
        pass
    else:
        pass

def humbaraciCorps(fieldIndex, current_player):
        if fieldIndex == 0:
            for card in player2.fields[fieldIndex][1]:
                card.attack -= 1
            print("1 Power removed for each card in field 1")
        elif fieldIndex == 1:
            for card in player2.fields[fieldIndex][1]:
                card.attack -= 1
            print("1 Power removed for each card in field 2")
        elif fieldIndex == 2:
            for card in player2.fields[fieldIndex][1]:
                card.attack -= 1
            print("1 Power removed for each card in field 3")
'''


def katipCelebi(fieldIndex, current_player):
    current_player.manapool += 2
    print("2 Mana added")


def timar(fieldIndex, current_player):
    for card in cards:
        if card.name == 'Sipahi':
            for i in range(0, 3):
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
    print("3 Sipahi added to field: " + str(fieldIndex))


'''
def topcu(fieldIndex, current_player):
        if fieldIndex == 0:
            for card in player2.fields[fieldIndex][1]:
                card.attack -= 1
            print("1 Power removed for each card in field 1")
        elif fieldIndex == 1:
            for card in player2.fields[fieldIndex][1]:
                card.attack -= 1
            print("1 Power removed for each card in field 2")
        elif fieldIndex == 2:
            for card in player2.fields[fieldIndex][1]:
                card.attack -= 1
            print("1 Power removed for each card in field 3")
'''


def ahmedCevdetPasha(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldTwoSum += 5
        print("5 Power added to field 2")
    elif fieldIndex == 1:
        current_player.fieldThreeSum += 5
        print("5 Power added to field 3")
    elif fieldIndex == 2:
        print("No effect no field on the right")
        pass


def deliler(fieldIndex, current_player):
    # If the card is in the first field, add +4 to attack points
    if current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldOneSum += 4
        print("4 Power added to field 1")
    else:
        print("No effect, field is not empty")


def harem(fieldIndex, current_player):
    if fieldIndex == 0:
        if current_player.fieldCardCount[fieldIndex] > 2:
            current_player.fieldSum[fieldIndex] += 2
            print("2 Power added to field 1")
        else:
            print("No effect, field has less than 2 cards")
    elif fieldIndex == 1:
        if current_player.fieldCardCount[fieldIndex] > 2:
            current_player.fieldSum[fieldIndex] += 2
            print("2 Power added to field 2")
        else:
            print("No effect, field has less than 2 cards")
    elif fieldIndex == 2:
        if current_player.fieldCardCount[fieldIndex] > 2:
            current_player.fieldSum[fieldIndex] += 2
            print("2 Power added to field 3")
        else:
            print("No effect, field has less than 2 cards")


# 0 Cost Mana
cards.append(Card('Hurrem Sultan',
             'Give +3 point to all cards on this field.', 0, 0, hurremSultan))
cards.append(Card('Asena', 'Give +3 mana when played.', 0, 0, asena))

# 1 Cost Mana
# TODO cards.append(Card('Lagimci', 'When played goes to enemy location', 1, -3, lagimci))
cards.append(Card('Azaps', 'No function.', 1, 2, nothing))
cards.append(
    Card('Harem', 'If there are more than 2 cards on that field +2.', 1, 2, nothing))
# 2 Cost Mana
# cards.append(Card('Humbaraci Corps', 'Throws a bomb to enemy field and damage -1 power to all card', 2, 3, humbaraciCorps))
cards.append(Card('Sipahi', 'No function.', 2, 2, nothing))

# 3 Cost Mana
cards.append(Card('Umur Bey', 'No function.', 3, 4, nothing))
cards.append(
    Card('Katip Celebi', 'Gives +2 mana when played.', 3, 4, katipCelebi))
cards.append(Card('Tonyukuk', 'No function.', 3, 4, nothing))
# cards.append(Card('Topcu', 'Throws a bomb to enemy field and damage -1 power to all card.', 3, 5, topcu))
cards.append(Card('Ahmed Cevdet Pasha',
             'Gives +5 power to right of his field.', 3, -2, ahmedCevdetPasha))
cards.append(Card(
    'Deliler', 'If the first card played on the field, gives 4P to field.', 3, 2, deliler))

# 4 Cost Mana
cards.append(Card('Hayreddin Barbarossa', 'No function.', 4, 6, nothing))
cards.append(Card('Timar', 'Spawn 3 Sipahi on played field', 4, 6, timar))

# 5 Cost Mana

# 6 Cost Mana
cards.append(Card('Bumin Qaghan', 'No function.', 6, 12, nothing))
