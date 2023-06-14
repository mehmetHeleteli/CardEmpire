class Card:
    def __init__(self, name, description, mana, attack, function):
        self.name = name
        self.description = description
        self.mana = mana
        self.attack = attack
        self.function = function

    def useCard(self, fieldIndex, current_player):
        self.function(fieldIndex, current_player)


drawable_cards = []
undrawable_cards = []

deckone = []
decktwo = []
deckthree = []
deckfour = []
deckfive = []


def nothing(fieldIndex, current_player):
    pass


def hurrem(fieldIndex, current_player):

    if fieldIndex == 0:
        for _ in range(0, current_player.fieldCardCount[fieldIndex]):
            current_player.fieldSum[fieldIndex] += 3
    elif fieldIndex == 1:
        for _ in range(0, current_player.fieldCardCount[fieldIndex]):
            current_player.fieldSum[fieldIndex] += 3
    elif fieldIndex == 2:
        for _ in range(0, current_player.fieldCardCount[fieldIndex]):
            current_player.fieldSum[fieldIndex] += 3


def asena(fieldIndex, current_player):
    current_player.manapool += 3
    print("3 Mana added")


def orkhonInscriptions(fieldIndex, current_player):
    current_player.manapool += 1
    current_player.fieldSum[fieldIndex] += 1
    print("1 Mana added to manapool and 1 Power added to all fields")


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


def lagimci(fieldIndex, current_player):
    if fieldIndex == 0 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 1")
    elif fieldIndex == 1 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 2")
    elif fieldIndex == 2 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 3")


def babur(fieldIndex, current_player):
    current_player.manapool += 1
    print("1 Mana added to manapool")


def nasreddinHoca(fieldIndex, current_player):
    if fieldIndex == 0:
        for card in undrawable_cards:
            if card.name == 'Donkey':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Donkey played to field 1")
    elif fieldIndex == 1:
        for card in undrawable_cards:
            if card.name == 'Donkey':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Donkey played to field 2")
    elif fieldIndex == 2:
        for cards in undrawable_cards:
            if card.name == 'Donkey':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Donkey played to field 3")


def silahdarAgasi(fieldIndex, current_player):
    if fieldIndex == 0:
        for _ in current_player.fields[fieldIndex][1]:
            print(_.name)
            if _.mana == 1:
                current_player.fieldSum[fieldIndex] += 2
                print("2 Power added to field 1")
    elif fieldIndex == 1:
        for _ in current_player.fields[fieldIndex][1]:
            if _.mana == 1:
                current_player.fieldSum[fieldIndex] += 2
                print("2 Power added to field 2")
    elif fieldIndex == 2:
        for _ in current_player.fields[fieldIndex][1]:
            if _.mana == 1:
                current_player.fieldSum[fieldIndex] += 2
                print("2 Power added to field 3")


def janissary(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldSum[fieldIndex+1] += 2
        current_player.fieldSum[fieldIndex+2] += 2
        print("2 Power added to field 2 and 3")
    elif fieldIndex == 1:
        current_player.fieldSum[fieldIndex-1] += 2
        current_player.fieldSum[fieldIndex+1] += 2
        print("2 Power added to field 1 and 3")
    elif fieldIndex == 2:
        current_player.fieldSum[fieldIndex-1] += 2
        current_player.fieldSum[fieldIndex-2] += 2
        print("2 Power added to field 1 and 2")


def humbaraci(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldSum[fieldIndex] += 3
        print("3 Power added to field 1")
        for _ in current_player.fields[fieldIndex][1]:
            if _.name == "Humbaraci Corps":
                _.remove()
                print("Humbaraci Corps removed from field 1")
    elif fieldIndex == 1:
        current_player.fieldSum[fieldIndex] += 3
        print("3 Power added to field 2")
        for _ in current_player.fields[fieldIndex][1]:
            if _.name == "Humbaraci Corps":
                _.remove()
                print("Humbaraci Corps removed from field 2")
    elif fieldIndex == 2:
        current_player.fieldSum[fieldIndex] += 3
        print("3 Power added to field 3")
        for _ in current_player.fields[fieldIndex][1]:
            if _.name == "Humbaraci Corps":
                _.remove()
                print("Humbaraci Corps removed from field 3")


def dragut(fieldIndex, current_player):
    if fieldIndex == 0:
        for card in undrawable_cards:
            if card.name == 'Ship':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Donkey played to field 1")
    elif fieldIndex == 1:
        for card in undrawable_cards:
            if card.name == 'Ship':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Donkey played to field 2")
    elif fieldIndex == 2:
        for card in undrawable_cards:
            if card.name == 'Ship':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Donkey played to field 3")


def sanjar(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldSum[fieldIndex+1] += 1
        current_player.fieldSum[fieldIndex+2] += 1
        print("1 Power added to field 2 and 3")
    elif fieldIndex == 1:
        current_player.fieldsSum[fieldIndex-1] += 1
        current_player.fieldSum[fieldIndex+1] += 1
        print("1 Power added to field 1 and 3")
    elif fieldIndex == 2:
        current_player.fieldSum[fieldIndex-1] += 1
        current_player.fieldSum[fieldIndex-2] += 1
        print("1 Power added to field 1 and 2")


def hafizAhmedPasha(fieldIndex, current_player):
    current_player.manapool += 2


def umur(fieldIndex, current_player):
    if fieldIndex == 0:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 2):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("1 ship played to field: " + str(fieldIndex))
    elif fieldIndex == 1:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 2):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("2 ships played to field: " + str(fieldIndex))
    elif fieldIndex == 2:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 2):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("3 ships played to field: " + str(fieldIndex))


def mehteran(fieldIndex, current_player):
    cardCount = 0
    if fieldIndex == 0:
        for _ in current_player.fieldCardCount[fieldIndex]:
            cardCount += 1
        current_player.fieldSum[fieldIndex] += cardCount
        print("Power added to field 1")
    elif fieldIndex == 1:
        for _ in current_player.fieldCardCount[fieldIndex]:
            cardCount += 1
        current_player.fieldSum[fieldIndex] += cardCount
        print("Power added to field 2")
    elif fieldIndex == 2:
        for _ in current_player.fieldCardCount[fieldIndex]:
            cardCount += 1
        current_player.fieldSum[fieldIndex] += cardCount
        print("Power added to field 3")


def deliler(fieldIndex, current_player):
    if fieldIndex == 0 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 1")
    elif fieldIndex == 1 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 2")
    elif fieldIndex == 2 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 3")
    else:
        print("No effect")


def katipCelebi(fieldIndex, current_player):
    current_player.manapool += 2
    print("2 Mana added")


def ahmedCevdet(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldSum[fieldIndex+1] += 2
        print("2 Power added to right field")
    elif fieldIndex == 1:
        current_player.fieldSum[fieldIndex+1] += 2
        print("2 Power added to right field")
    else:
        print("No effect")


def alpErTunga(fieldIndex, current_player):
    if fieldIndex == 0:
        print("No effect")
    elif fieldIndex == 1:
        current_player.fieldSum[fieldIndex-1] += 3
        print("1 Power added to left field")
    elif fieldIndex == 2:
        current_player.fieldSum[fieldIndex-1] += 3
        print("1 Power added to left field")


def ibrahim(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldSum[fieldIndex+1] += 4
        current_player.fieldSum[fieldIndex+2] += 4
        print("4 Power added to field 2 and 3")
    elif fieldIndex == 1:
        current_player.fieldSum[fieldIndex-1] += 4
        current_player.fieldSum[fieldIndex+1] += 4
        print("4 Power added to field 1 and 3")
    elif fieldIndex == 2:
        current_player.fieldSum[fieldIndex-1] += 4
        current_player.fieldSum[fieldIndex-2] += 4
        print("4 Power added to field 1 and 2")


def barbaros(fieldIndex, current_player):
    if fieldIndex == 0:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 3):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("1 ship played to field: " + str(fieldIndex))
    elif fieldIndex == 1:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 3):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("2 ships played to field: " + str(fieldIndex))
    elif fieldIndex == 2:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 3):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("3 ships played to field: " + str(fieldIndex))


def sokulluMehmed(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 1")
    elif fieldIndex == 1:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 2")
    elif fieldIndex == 2:
        current_player.fieldSum[fieldIndex] += 4
        print("4 Power added to field 3")


def timar(fieldIndex, current_player):  # WORKS
    for card in drawable_cards:
        if card.name == 'Sipahi':
            for i in range(0, 3):
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
    print("3 Sipahi added to field: " + str(fieldIndex))


def piriReis(fieldsIndex, current_player):
    if fieldsIndex == 0:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 3):
                    current_player.fields[fieldsIndex][1].append(card)
                    current_player.fieldCardCount[fieldsIndex] += 1
                    current_player.fieldSum[fieldsIndex] += card.attack
                    print("1 ship played to field: " + str(fieldsIndex))
    elif fieldsIndex == 1:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 3):
                    current_player.fields[fieldsIndex][1].append(card)
                    current_player.fieldCardCount[fieldsIndex] += 1
                    current_player.fieldSum[fieldsIndex] += card.attack
                    print("2 ships played to field: " + str(fieldsIndex))
    elif fieldsIndex == 2:
        for card in undrawable_cards:
            if card.name == 'Ship':
                for i in range(0, 3):
                    current_player.fields[fieldsIndex][1].append(card)
                    current_player.fieldCardCount[fieldsIndex] += 1
                    current_player.fieldSum[fieldsIndex] += card.attack
                    print("3 ships played to field: " + str(fieldsIndex))


def ummuhan(fieldIndex, current_player):
    current_player.manapool += 2


def kultigun(fieldIndex, current_player):
    current_player.manapool += 3


def mimarSinan(fieldIndex, current_player):
    if fieldIndex == 0:
        for card in undrawable_cards:
            if card.name == 'Topkapi Palace':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Topkapi Palace played to field: " + str(fieldIndex))
    elif fieldIndex == 1:
        for card in undrawable_cards:
            if card.name == 'Topkapi Palace':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Topkapi Palace played to field: " + str(fieldIndex))
    elif fieldIndex == 2:
        for card in undrawable_cards:
            if card.name == 'Topkapi Palace':
                current_player.fields[fieldIndex][1].append(card)
                current_player.fieldCardCount[fieldIndex] += 1
                current_player.fieldSum[fieldIndex] += card.attack
                print("Topkapi Palace played to field: " + str(fieldIndex))


def osman(fieldIndex, current_player):
    if fieldIndex == 0 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 7
        print("7 Power added to field 1")
    elif fieldIndex == 1 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 7
        print("7 Power added to field 2")
    elif fieldIndex == 2 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 7
        print("7 Power added to field 3")
    else:
        print("No effect")


def mihrimah(fieldIndex, current_player):
    if fieldIndex == 0 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 5
        print("5 Power added to field 1")
    elif fieldIndex == 1 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 5
        print("5 Power added to field 2")
    elif fieldIndex == 2 & current_player.fieldCardCount[fieldIndex] == 0:
        current_player.fieldSum[fieldIndex] += 5
        print("5 Power added to field 3")


def pargali(fieldIndex, current_player):
    current_player.manapool += 3


def suleiman(fieldIndex, current_player):
    if fieldIndex == 0:
        cardCount = current_player.fieldCardCount[fieldIndex]
        current_player.fieldSum[fieldIndex] += cardCount
        print(str(cardCount) + " Power added to field 1")
    elif fieldIndex == 1:
        cardCount = current_player.fieldCardCount[fieldIndex]
        current_player.fieldSum[fieldIndex] += cardCount
        print(str(cardCount) + " Power added to field 2")
    elif fieldIndex == 2:
        cardCount = current_player.fieldCardCount[fieldIndex]
        current_player.fieldSum[fieldIndex] += cardCount
        print(str(cardCount) + " Power added to field 3")


def fsm(fieldIndex, current_player):
    if fieldIndex == 0:
        for card in undrawable_cards:
            if card.name == 'Army':
                for i in range(0, 2):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("2 Army played to field: " + str(fieldIndex))
    elif fieldIndex == 1:
        for card in undrawable_cards:
            if card.name == 'Army':
                for i in range(0, 2):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("2 Army played to field: " + str(fieldIndex))
    elif fieldIndex == 2:
        for card in undrawable_cards:
            if card.name == 'Army':
                for i in range(0, 2):
                    current_player.fields[fieldIndex][1].append(card)
                    current_player.fieldCardCount[fieldIndex] += 1
                    current_player.fieldSum[fieldIndex] += card.attack
                    print("2 Army played to field: " + str(fieldIndex))


def alparslan(fieldIndex, current_player):
    if fieldIndex == 0:
        for card in undrawable_cards:
            if card.name == 'Army':
                # for 2. field
                current_player.fields[fieldIndex + 1][1].append(card)
                current_player.fieldCardCount[fieldIndex + 1] += 1
                current_player.fieldSum[fieldIndex + 1] += card.attack
                print("1 Army played to field: " + str(fieldIndex + 1))
                # for 3. field
                current_player.fields[fieldIndex + 2][1].append(card)
                current_player.fieldCardCount[fieldIndex + 2] += 1
                current_player.fieldSum[fieldIndex + 2] += card.attack
                print("1 Army played to field: " + str(fieldIndex + 1))
    elif fieldIndex == 1:
        for card in undrawable_cards:
            if card.name == "Army":
                # for 1. field
                current_player.fields[fieldIndex - 1][1].append(card)
                current_player.fieldCardCount[fieldIndex - 1] += 1
                current_player.fieldSum[fieldIndex - 1] += card.attack
                print("1 Army played to field: " + str(fieldIndex - 1))
                # for 3. field
                current_player.fields[fieldIndex + 1][1].append(card)
                current_player.fieldCardCount[fieldIndex + 1] += 1
                current_player.fieldSum[fieldIndex + 1] += card.attack
                print("1 Army played to field: " + str(fieldIndex + 1))
    elif fieldIndex == 2:
        for card in undrawable_cards:
            if card.name == "Army":
                # for 1. field
                current_player.fields[fieldIndex - 1][1].append(card)
                current_player.fieldCardCount[fieldIndex - 1] += 1
                current_player.fieldSum[fieldIndex - 1] += card.attack
                print("1 Army played to field: " + str(fieldIndex - 1))
                # for 2. field
                current_player.fields[fieldIndex - 2][1].append(card)
                current_player.fieldCardCount[fieldIndex - 2] += 1
                current_player.fieldSum[fieldIndex - 2] += card.attack
                print("1 Army played to field: " + str(fieldIndex - 2))


def timur(fieldIndex, current_player):

    current_player.fieldSum[0] += current_player.fieldCardCount[0]
    current_player.fieldSum[1] += current_player.fieldCardCount[1]
    current_player.fieldSum[2] += current_player.fieldCardCount[2]
    print("Field 1: " + str(current_player.fieldCardCount[0]) + " Power added")
    print("Field 2: " + str(current_player.fieldCardCount[1]) + " Power added")
    print("Field 3: " + str(current_player.fieldCardCount[2]) + " Power added")


def atilla(fieldIndex, current_player):
    if fieldIndex == 0:
        print("No fields on the left")
    elif fieldIndex == 1:
        current_player.fieldSum[fieldIndex-1] += 5
        print("3 Power added to left field")
    elif fieldIndex == 2:
        current_player.fieldSum[fieldIndex-1] += 5
        print("3 Power added to left field")


def metehan(fieldIndex, current_player):
    if fieldIndex == 0:
        current_player.fieldSum[fieldIndex + 1] += 5
    elif fieldIndex == 1:
        current_player.fieldSum[fieldIndex + 1] += 5
        print("3 Power added to left field")
    elif fieldIndex == 2:
        print("No fields on the right")


def bilgeQagan(fieldIndex, current_player):
    pass


# 0 Cost Mana
drawable_cards.append(Card('Hurrem',
                           'Give +3 point to all cards on this field.', 0, 0, hurrem))
drawable_cards.append(Card('Asena', 'Give +3 mana when played.', 0, 0, asena))
drawable_cards.append(Card('Orkhon Inscriptions',
                           'Give +1 M and +1 P when played.', 0, 0, asena))

# 1 Cost Mana
drawable_cards.append(
    Card('Harem', 'If there are more than 2 cards on that field +2.', 1, 2, harem))
drawable_cards.append(Card('Marquee', 'No function.', 1, 2, nothing))
drawable_cards.append(Card('Lagimci', 'When played gives +1 M', 1, 2, lagimci))
drawable_cards.append(Card('Azaps', 'No function.', 1, 2, nothing))
drawable_cards.append(Card('Ay Yiltiz', 'No function.', 1, 2, nothing))
drawable_cards.append(Card('Babur', 'When played gives +1 M', 1, 3, babur))
drawable_cards.append(Card('Nasreddin', 'Spawns donkey', 1, 0, nasreddinHoca))

# 2 Cost Mana
drawable_cards.append(Card('Ket Buga', 'No function', 2, 4, nothing))
drawable_cards.append(
    Card('Silahtar Agha', 'Gives +3P to 6 cost card', 2, 3, silahdarAgasi))
drawable_cards.append(
    Card('Janissary', 'Gives one by one P other fields', 2, 2, janissary))
drawable_cards.append(Card('Sipahi', 'No function.', 2, 2, nothing))
drawable_cards.append(Card('Humbaraci Corps', 'No function', 2, 0, humbaraci))
drawable_cards.append(Card('Dragut', 'Spawns 1 ship', 2, 1, dragut))
drawable_cards.append(Card('Sanjar', 'gives +1 P other fields', 2, 3, sanjar))


# 3 Cost Mana
drawable_cards.append(
    Card('Hafiz Ahmed', 'Gives +1 Mana', 3, 4, hafizAhmedPasha))
drawable_cards.append(Card('Omar Khayyam', 'No function', 3, 3, nothing))
drawable_cards.append(Card('Umur Bey', 'Spawns 2 ship', 3, 2, umur))
drawable_cards.append(Card(
    'Mehteran', 'Gives + 1P acording to numbers of cards in field.', 3, 2, mehteran))
drawable_cards.append(Card(
    'Deliler', 'If the first card played on the field, gives 4P to field.', 3, 2, deliler))
drawable_cards.append(Card('Topcu', 'No function', 3, 5, nothing))
drawable_cards.append(
    Card('Katip Celebi', 'gives +2 mana when played.', 3, 3, katipCelebi))
drawable_cards.append(Card('Ahmed Cevdet',
                           'Gives +5 power to right of his field.', 3, -2, ahmedCevdet))
drawable_cards.append(Card('Evliya Celebi', 'No function.', 3, 3, nothing))
drawable_cards.append(Card('Tonyukuk', 'No function.', 3, 4, nothing))
drawable_cards.append(Card('Mirim Celebi', 'No function.', 3, 4, nothing))
drawable_cards.append(
    Card('Alp Er Tunga', 'provides +3 P left field.', 3, 2, alpErTunga))
drawable_cards.append(Card('Lala Mustafa', 'No function.', 3, 5, nothing))
drawable_cards.append(
    Card('Ibrahim', 'provides +4p other fields.', 3, -5, ibrahim))


# 4 Cost Mana
drawable_cards.append(Card('Barbarossa', 'Spawns 3 ship.', 4, 3, barbaros))
drawable_cards.append(
    Card('Sokullu Mehmed', '-4 P oppenents field', 4, 4, sokulluMehmed))
drawable_cards.append(Card('Timar', 'Spawns 3 sipahi', 4, 2, timar))
drawable_cards.append(Card('Piri Reis', 'Spawns 3 ship', 4, 2, piriReis))
drawable_cards.append(Card('Ummuhan', '+2 Mana.', 4, 6, ummuhan))
drawable_cards.append(Card('Kosem', 'No function.', 4, 8, nothing))
drawable_cards.append(Card('Kul Tigin', '+3 Mana', 4, 4, kultigun))

# 5 Cost Mana
drawable_cards.append(Card('Aleaddin', 'No function', 5, 9, nothing))
drawable_cards.append(Card('Mimar Sinan', 'Spawns Topkapi', 5, 1, mimarSinan))
drawable_cards.append(Card(
    'Osman', 'If the first card played on the field, gives 7P to field.', 5, 2, osman))
drawable_cards.append(
    Card('Mihrimah', 'if the card played on first field, gives 5P.', 5, 5, mihrimah))
drawable_cards.append(Card('Pargali', '+3 Mana', 5, 7, pargali))
drawable_cards.append(Card('Orhan Gazi', 'No function', 5, 10, nothing))
drawable_cards.append(
    Card('Suleiman', '-3 P to the card oppenent field.', 5, 8, suleiman))

# 6 Cost Mana
drawable_cards.append(Card('FSM', 'Spawns 2 army', 6, 7, fsm))
drawable_cards.append(Card('Bumin Qaghan', 'No function.', 6, 12, nothing))
drawable_cards.append(
    Card('Alparslan', 'Spawns army to other fields', 6, 5, alparslan))
drawable_cards.append(
    Card('Timur', '-1 P acoring to oppenent cards', 6, 7, timur))
drawable_cards.append(Card('Atilla', '+9 P to left field', 6, 6, atilla))
drawable_cards.append(Card('Metehan', 'No function.', 6, 6, metehan))
drawable_cards.append(Card('Bilge Qaghan', 'No function.', 6, 12, bilgeQagan))

# Unique Cards
undrawable_cards.append(Card('Topkapi Palace', 'No function.', 0, 8, nothing))
undrawable_cards.append(Card('Ship', 'No function.', 0, 2, nothing))
undrawable_cards.append(Card('Army', 'No function.', 0, 3, nothing))
undrawable_cards.append(Card('Donkey', 'No function.', 0, 2, nothing))

# DECK ONE
deckone = [
    drawable_cards[0],  # Hurrem
    drawable_cards[6],  # Azaps
    drawable_cards[8],  # Babur
    drawable_cards[11],  # Silahtar Agha
    drawable_cards[20],  # Mehteran
    drawable_cards[21],  # Deliler
    drawable_cards[23],  # Katip Celebi
    drawable_cards[34],  # Piri Reis
    drawable_cards[38],  # Aleaddin Pasha
    drawable_cards[48]  # Timur
]


# DECK TWO
decktwo = [
    drawable_cards[1],  # Asena
    drawable_cards[3],  # Harem
    drawable_cards[9],  # Nasreddin
    drawable_cards[12],  # Janissary
    drawable_cards[18],  # Omar Khayyam
    drawable_cards[22],  # Topcu
    drawable_cards[24],  # Ahmed Cevdet Pasha
    drawable_cards[43],  # Orhan Gazi
    drawable_cards[39],  # Mimar Sinan
    drawable_cards[45]  # FSM
]

# DECK THREE
deckthree = [
    drawable_cards[0],  # Hurrem
    drawable_cards[4],  # Marquee
    drawable_cards[10],  # Ket Buga
    drawable_cards[13],  # Sipahi
    drawable_cards[19],  # Umur Bey
    drawable_cards[26],  # Tonyukuk
    drawable_cards[32],  # Sokullu Mehmed
    drawable_cards[31],  # Barbarossa
    drawable_cards[41],  # Mihrimah
    drawable_cards[46]  # Bumin Qaghan
]

# DECK FOUR
deckfour = [
    drawable_cards[1],  # Asena
    drawable_cards[5],  # Lagimci
    drawable_cards[6],  # Azaps
    drawable_cards[15],  # Dragut
    drawable_cards[17],  # Hafiz Ahmed Pasha
    drawable_cards[28],  # Alp Er Tunga
    drawable_cards[37],  # Kul Tigin
    drawable_cards[44],  # Suleiman The Magnificent
    drawable_cards[43],  # Orhan Gazi
    drawable_cards[49]  # Atilla
]

# DECK FIVE
deckfive = [
    drawable_cards[2],  # Orkhon Inscriptions
    drawable_cards[9],  # Nasreddin
    drawable_cards[8],  # Babur
    drawable_cards[16],  # Sanjar
    drawable_cards[11],  # Silahtar Agha
    drawable_cards[30],  # Ibrahim The Mad
    drawable_cards[33],  # Timar
    drawable_cards[42],  # Pargali
    drawable_cards[40],  # Osman Bey
    drawable_cards[47]  # Alparslan
]
