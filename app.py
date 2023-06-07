from flask import Flask, render_template, request, jsonify
import Game
import Player
import AIBehavior

app = Flask(__name__)

current_turn = 1
global player
global ai_bot


def start_game():
    global player
    global ai_bot
    player = Player.PlayerClass('Player')
    ai_bot = Player.PlayerClass('AI')

    # Create a deck for each player
    player.deck = Game.create_deck()
    ai_bot.deck = Game.create_deck()

    # Shuffle each player's deck
    player.deck = Game.shuffle_deck(player.deck)
    ai_bot.deck = Game.shuffle_deck(ai_bot.deck)

    # Draw 2 cards for each player
    for i in range(0, 3):
        player.draw()
        ai_bot.draw()

    print("Game started")


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/chat', methods=['POST'])
def chat():
    nickname = request.form['nickname']
    return render_template('index.html', nickname=nickname)


@app.route('/send_message', methods=['POST'])
def send_message():
    global current_turn
    global player
    global ai_bot
    message = request.form['message']
    nickname = request.form['nickname']
    response = ""
    response_end = "\n----------------------------------------"

    card_index = 0
    field_index = 0

    # Perform actions based on the command
    if message.lower().startswith("play "):
        # Split the message to extract the card index and field index
        indices = message[5:].split()
        if len(indices) == 2:
            try:
                card_index = int(indices[0]) - 1
                field_index = int(indices[1]) - 1

                # Get the name of the played card
                card_name = player.hand[card_index].name

                response = "Played %s" % card_name

                # Perform the play action using the received card_index and field_index
                player.play(card_index, field_index)

            except (ValueError, IndexError):
                response = "Invalid indices provided"
                response += response_end
        else:
            response = "Invalid command format. Please provide both card index and field index."

    elif message.lower() == "hand":
        response = "\nHand:\n"
        for card_index, card in enumerate(player.hand):
            response += f"\t{card_index + 1}. {card.name} | Mana: {card.mana} | Attack: {card.attack}\n"
        response += response_end

    elif message.lower() == "fields":
        response = "\nFields:\n"

        # Print player's fields and field sums
        response += " Player's Fields:\n"
        for field_index, field in enumerate(player.fields):
            response += f"\t  Field {field_index + 1} (Field Sum: {player.fieldSum[field_index]})\n"
            for card in field[1]:
                response += f"\t\t{card.name} | Mana: {card.mana} | Attack: {card.attack}\n"

        # Print AI's fields and field sums
        response += " AI's Fields:\n"
        for field_index, field in enumerate(ai_bot.fields):
            response += f"\t  Field {field_index + 1} (Field Power: {ai_bot.fieldSum[field_index]})\n"
            for card in field[1]:
                response += f"\t\t{card.name} | Mana: {card.mana} | Attack: {card.attack}\n"
        response += response_end

    elif message.lower() == "mana":
        response = f"\nMana: {player.manapool}/{player.max_mana}"
        response += response_end

    elif message.lower() == "end":
        response = "Ended turn"
        response += response_end
        response += "\nAI's turn\n"
        switch_turns()
        ai_response = ""
        while current_turn == 0:
            ai_response = ai_bot_turn()
            if ai_response is not None:
                response += ai_response
        response += response_end
################################### TESTIING##############################################
    elif message.lower() == "bothand":
        response = "\nHand:\n"
        for card_index, card in enumerate(ai_bot.hand):
            response += f"\t{card_index + 1}. {card.name} | Mana: {card.mana} | Attack: {card.attack}\n"
        response += response_end

    elif message.lower() == "botdraw":
        response = "\nAI drew a card"
        ai_bot.draw()
        response += response_end

    elif message.lower() == "botaddmana":
        response = "\nAI added 1 mana"
        ai_bot.manapool += 1
        response += response_end
################################### TESTIING##############################################
    else:
        response = "Invalid command"

    return jsonify({'message': response})


def switch_turns():
    global current_turn  # Declare current_turn as a global variable
    current_turn = 1 - current_turn  # Switch turns


def ai_bot_turn():
    global current_turn
    global player
    global ai_bot
    playable_cards = []
    response = ""
    response_end = "\n----------------------------------------"

    # Simulate AI's turn
    if ai_bot.manapool > 0:
        # Check cards in hand
        for card_index, card in enumerate(ai_bot.hand):
            # Add playable cards to a list
            if card.mana <= ai_bot.manapool:
                playable_cards.append(card)
            else:
                response = "\nAI has no playable cards"
                switch_turns()
                return response
        while len(playable_cards) > 0 and ai_bot.manapool > 0:
            # Get most powerful card from playable cards
            card = Game.get_most_powerful_card(playable_cards)
            # Find index of card in playable cards
            card_index = playable_cards.index(card)
            # Find index of the card with lowest sum

            # Check if AI has enough mana to play the card
            if ai_bot.manapool >= card.mana:
                # Play the card on the field with the lowest sum
                ai_bot.play(card_index, 0)

                # Send the response to the client
                response += "\tAI Bot played " + card.name + \
                    " on field " + str(1) + "\n"

                # Update AI's mana
                ai_bot.manapool -= card.mana

                # Remove the played card from playable cards
                playable_cards.remove(card)
            else:
                break
    switch_turns()
    print(current_turn)
    return response


if __name__ == '__main__':
    start_game()
    app.run(debug=True)
