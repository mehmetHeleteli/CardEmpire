# CardEmpire

Welcome to the Card Empire! This is a card game developed using Flask.

## Description

The Card Game is a turn-based strategy card game where players compete against each other to build powerful decks and defeat their opponents. The game features a variety of cards with different abilities, mana costs, and attack values. Players take turns playing cards from their hand to the field, strategically using their mana pool and managing their resources to gain an advantage over their opponents.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
https://github.com/mehmetHeleteli/CardEmpire

2. Install the required dependencies:
pip install -r requirements.txt


### How to Play

1. Start the game by running the `app.py` file.
python app.py

2. Open your web browser and navigate to `http://localhost:5000`.

3. Choose the deck that you desired.

5. Enter your nickname and click "Submit" to log in.

5. Follow the on-screen instructions and use the available commands to play the game.

### Gameplay Commands

- `play <card_index> <field_index>` - Plays a card from your hand to the specified field.
- `hand` - Shows the cards in your hand.
- `fields` - Shows the cards in the fields.
- `mana` - Shows your current mana pool.
- `end` - Ends your turn.
- `help` - Shows the list of available commands.

## Development

### Folder Structure

- `templates/` - Contains HTML templates for rendering the web pages.
- `static/` - Contains static files such as CSS and JavaScript.
- `Game.py` - Implements the core game logic and functions.
- `Player.py` - Defines the player class and its properties.
- `Cards.py` - Defines the cards and their functions.
- `app.py` - Flask application file for running the game.

### Contributing

Contributions to the Card Game are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Commit your changes and push them to your forked repository.
5. Submit a pull request detailing your changes.

### License

The Card Game is released under the [MIT License](LICENSE).
