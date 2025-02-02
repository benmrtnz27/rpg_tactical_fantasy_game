# RPG Tactical Fantasy Game

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![licence](https://img.shields.io/github/license/Grimmys/rpg_tactical_fantasy_game)](https://github.com/Grimmys/rpg_tactical_fantasy_game/blob/master/LICENSE)
[![latest release](https://img.shields.io/github/v/release/Grimmys/rpg_tactical_fantasy_game)](https://github.com/Grimmys/rpg_tactical_fantasy_game/releases/latest)
![GitHub release (latest by date)](https://img.shields.io/github/downloads/Grimmys/rpg_tactical_fantasy_game/latest/total)

**Collaborative development.**

The game is an RPG Tactical Fantasy game, turn-based and is in 2D.

## How to help development

You can submit any request you want, or notify me about any bug you encountered, by sending an e-mail to grimmys.programming@gmail.com or by opening an issue.

Alternatively, you can join the newly created community discord: https://discord.gg/CwFdXNs9Wt.

Feel free to come up with ideas whether it is about coding practices or game mechanics, this project is far from being perfect!

* Help with balancing would be greatly appreciated... I'm not really good in this kind of games even if I love them.
  All values could be found in the XML files wrapped in the data folder.
* Since I'm not a designer, some elements may be oddly placed in the UI. You can try to correct the ones you see or simply notify me.
* Contributions for sound effects / soundtracks would be really appreciated.
* Ideas about future levels could be submitted, however, I'm currently working on a scenario.

__Version__ : 1.0.4

![Main screen with possible moves and attack](/screenshots/player_moves_and_attacks.png?raw=True)
![Inventory menu](/screenshots/inventory_screen.png?raw=True)
![Status window](/screenshots/status_screen.png?raw=True)

## How to start the game

If you are using 64-bit Windows you can head over to the [releases page](https://github.com/grimmys/rpg_tactical_fantasy_game/releases) to get a prebuilt executable.

If you would rather run directly from the source \(or want to develop the game\), make sure to have [Python](https://python.org) installed and run `python -m pip install -r requirements` in the repository folder.

Then you can run `python main.py` or "./main.py" (only for for Python 3) in linux operation system to start the game.

## Keys

* Left click : Select a player, choose a case to move, select an action to do etc (main button)
* Left click (on any empty tile) : Open main menu
* Left click (on any entity that is not a player who has finished his turn) : Open a window giving information about the entity
* Right click : Deselect a player or cancel last action if possible (secondary button)
* Right click (on any entity) : Show the possible movements of the entity
