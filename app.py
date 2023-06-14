from flask import Flask, render_template, request, jsonify, redirect, url_for
import Game
import Player

app = Flask(__name__)
app.static_folder = 'templates/img'

current_turn = 1
global player
global ai_bot
cheat_enabled = False


def start_game(deck):
    global player
    global ai_bot
    ai_bot = Player.PlayerClass('AI')
    player = Player.PlayerClass('Player')

    deck = int(deck)
    print(deck)
    # Create a deck for each player

    player.deck = Game.select_deck(deck)
    ai_bot.deck = Game.select_deck_for_ai()

    for _ in player.deck:
        print(_.name)

    # Shuffle each player's deck
    player.deck = Game.shuffle_deck(player.deck)
    ai_bot.deck = Game.shuffle_deck(ai_bot.deck)

    for _ in range(4):
        player.draw()

    for _ in range(3):
        ai_bot.draw()
    print("Game started")


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/chat', methods=['POST'])
def chat():
    global deck
    nickname = request.form['nickname']
    deck = request.form['deck']
    start_game(deck)

    return render_template('index.html', nickname=nickname, deck=deck)


@app.route('/send_message', methods=['POST'])
def send_message():
    global current_turn
    global player
    global ai_bot
    global cheat_enabled
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

                # Check if the card index is valid
                if 0 <= card_index < len(player.hand):
                    card = player.hand[card_index]

                    # Check if the player has enough mana to play the card
                    if player.manapool >= card.mana:
                        # Get the name of the played card
                        card_name = card.name

                        response = nickname + " Played %s" % card_name
                        response += response_end

                        # Perform the play action using the received card_index and field_index
                        player.play(card_index, field_index)
                        player.manapool -= card.mana

                        # Writes player and AI's fields to the response
                        response += "\nFields:\n"

                        # Print player's fields and field sums
                        response += nickname + "'s Fields:\n"
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

                    else:
                        response = "Not enough mana to play %s" % card.name
                else:
                    response = "Invalid card index provided"
            except (ValueError, IndexError):
                response = "Invalid indices provided"
                response += response_end
        else:
            response = "Invalid command format. Please provide both card index and field index."

    elif message.lower() == "hand":
        response = "\n" + nickname + "'s Hand:\n"
        for card_index, card in enumerate(player.hand):
            response += f"\t{card_index + 1}. {card.name:<15} | {card.description:<30} | Mana: {card.mana:<5} | Atk: {card.attack}\n"
        response += response_end

    elif message.lower() == "fields":
        response = "\nFields:\n"

        # Print player's fields and field sums
        response += nickname + "'s Fields:\n"
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

    elif message.lower() == "help":
        response = "\nCommands:\n" \
            "\tplay 'card_number' 'field_number' - Plays a card from hand to field\n" \
            "\thand                              - Shows the cards in hand\n" \
            "\tfields                            - Shows the cards in fields\n" \
            "\tmana                              - Shows the mana pool\n" \
            "\tend                               - Ends the turn\n" \
            "\treset                             - Resets the game\n" \
            "\thelp                              - Shows the commands\n"

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

        # Increase max mana by 1
        player.max_mana += 1
        player.manapool = player.max_mana
        ai_bot.max_mana += 1
        ai_bot.manapool = ai_bot.max_mana

        # Player draws a card
        player.draw()

        # Check game end
        if ai_bot.max_mana == 7:  # If AI's max mana is 7, end the game
            response += "\nGame ended."

            ai_win_Counter = 0
            player_win_Counter = 0
            # Calculate the winner
            for i in range(0, 3):
                if player.fieldSum[i] > ai_bot.fieldSum[i]:
                    # Writing which fields that player wins
                    response += f"\nPlayer won field {i + 1}!"
                    player_win_Counter += 1
                elif player.fieldSum[i] < ai_bot.fieldSum[i]:
                    # Writing which fields that AI wins
                    response += f"\nAI won field {i + 1}!"
                    ai_win_Counter += 1
                elif player.fieldSum[i] == ai_bot.fieldSum[i]:
                    response += f"\nField {i + 1} is a draw!"
                    ai_win_Counter += 1
                    player_win_Counter += 1

            # If player wins more fields than AI, player wins the game
            if player_win_Counter > ai_win_Counter:
                response += "\nPlayer wins!"
            # If AI wins more fields than player, AI wins the game
            elif player_win_Counter < ai_win_Counter:
                response += "\nAI wins!"
            # If both player and AI wins the same amount of fields, calculate the field sums
            elif player_win_Counter == ai_win_Counter:
                player_field_sum = 0
                ai_field_sum = 0
                for i in range(0, 3):
                    player_field_sum += player.fieldSum[i]
                    ai_field_sum += ai_bot.fieldSum[i]
                # If player's field sum is greater than AI's field sum, player wins the game
                if player_field_sum > ai_field_sum:
                    response += "\nPlayer wins!"
                # If AI's field sum is greater than player's field sum, AI wins the game
                elif player_field_sum < ai_field_sum:
                    response += "\nAI wins!"
                # If both player's and AI's field sums are equal, the game is a draw
                elif player_field_sum == ai_field_sum:
                    response += "\nGame is a draw!"

            response += response_end

            response += "\nGame ended."
            response += response_end
            return redirect('http://cardempire.me')

    elif message.lower() == "cheat_enable":
        response = "Cheat enabled"
        cheat_enabled = True
        response += response_end

    elif message.lower() == "cheat_disable":
        response = "Cheat disabled"
        cheat_enabled = False
        response += response_end


################################### TESTIING##############################################
    elif message.lower() == "bothand" and cheat_enabled is True:
        response = "\nHand:\n"
        for card_index, card in enumerate(ai_bot.hand):
            response += f"\t{card_index + 1}. {card.name} | Mana: {card.mana} | Attack: {card.attack}\n"
        response += response_end

    elif message.lower() == "botdraw" and cheat_enabled is True:
        response = "\nAI drew a card"
        ai_bot.draw()
        response += response_end

    elif message.lower() == "deck":
        response = "\nDeck:\n"
        for card_index, card in enumerate(player.deck):
            response += f"\t{card_index + 1}. {card.name} | Mana: {card.mana} | Attack: {card.attack}\n"
        response += response_end

    elif message.lower() == "botaddmana" and cheat_enabled is True:
        response = "\n1 mana added to AI"
        ai_bot.manapool += 1
        response += response_end

    elif message.lower() == "draw" and cheat_enabled is True:
        response = "\n" + nickname + " drew a card"
        player.draw()
        response += response_end

    elif message.lower() == "addmana" and cheat_enabled is True:
        response = "\n1 mana added to " + nickname
        player.manapool += 6
        response += response_end

    elif message.lower() == "botmana" and cheat_enabled is True:
        response = f"\nAI Mana: {ai_bot.manapool}/{ai_bot.max_mana}"
################################### TESTIING##############################################
    else:
        response = "Invalid command"
        response += response_end

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
        for card in ai_bot.hand:
            # Add playable cards to a list
            if ai_bot.manapool >= card.mana:
                playable_cards.append(card)

        if len(playable_cards) > 0:
            for card in playable_cards:
                print(card.name)
        else:
            response = "\nAI has no playable cards"
            switch_turns()
            print(len(playable_cards))
            ai_bot.draw()
            return response

        while len(playable_cards) > 0 and ai_bot.manapool > 0:
            # Get most powerful card from playable cards
            card = Game.get_most_powerful_card(playable_cards)
            # Find the index of the card in AI's hand
            card_index = ai_bot.hand.index(card)

            # Check if AI has enough mana to play the card
            if ai_bot.manapool >= card.mana:
                # Play the card on the field with the lowest sum
                field_index = Game.find_least_powerful_field(ai_bot)
                ai_bot.play(card_index, field_index)

                # Send the response to the client
                response += "\tAI Bot played " + card.name + \
                    " on field " + str(field_index + 1) + "\n"

                # Update AI's mana
                ai_bot.manapool -= card.mana

                # Remove the played card from playable cards
                playable_cards.remove(card)

                # Writes player and AI's fields to the response
                response += "\nFields:\n"

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
            else:
                break
    switch_turns()
    ai_bot.draw()
    return response


if __name__ == '__main__':
    app.run(port=5001, debug=True)
