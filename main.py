# main.py
"""
Main entry point for the Live Game Overlay and Input System.

1. Shows a setup dialog to collect each player's info:
   - Player Name
   - Deck Name
   - Decklist (pasted text)

2. Initializes GameState using the custom player names.

3. Creates a PlayerWindow for game input per player.

4. Creates an overlay window per player (using PlayerOverlayWindow).  
   Each overlay displays:
      - Deck Name (bold)
      - Player Name (smaller font)
      - Life Total
      - A bold header "Cards In Hand"
      - A vertical list of cards in hand

Each overlay window is frameless and draggable.
"""

import sys
from PyQt5.QtWidgets import QApplication
from config import PLAYER_WINDOW_WIDTH, PLAYER_WINDOW_HEIGHT, OVERLAY_WINDOW_WIDTH, OVERLAY_WINDOW_HEIGHT
from game_state import GameState
from player_window import PlayerWindow
from overlay_window import PlayerOverlayWindow
from setup_dialog import SetupDialog
from utils import init_logger

logger = init_logger()

def main():
    app = QApplication(sys.argv)

    # Run setup dialog to collect players' details and decklists.
    setup_dialog = SetupDialog()
    if setup_dialog.exec_() != setup_dialog.Accepted:
        sys.exit("Setup cancelled.")

    setup_data = setup_dialog.get_setup_data()
    players_info = setup_data.get("players")
    
    # Verify we have players and at least one decklist.
    if not players_info or not players_info[0].get("decklist"):
        sys.exit("No decklist loaded. Exiting.")

    # Create list of custom player names.
    player_names = [player["player_name"] for player in players_info]

    # Initialize game state with these names.
    game_state = GameState(player_names)
    logger.debug("GameState initialized with players: %s", player_names)

    # Create game input windows for each player.
    player_windows = []
    for player in players_info:
        player_name = player["player_name"]
        deck_name = player["deck_name"]
        player_decklist = player.get("decklist") or {}
        p_window = PlayerWindow(player_name, game_state, player_decklist)
        p_window.setWindowTitle(f"{player_name} - {deck_name}")
        p_window.resize(PLAYER_WINDOW_WIDTH, PLAYER_WINDOW_HEIGHT)
        p_window.show()
        player_windows.append(p_window)
        logger.debug("Created input window for %s", player_name)

    # Create an overlay window for each player.
    overlay_windows = []
    for player in players_info:
        player_name = player["player_name"]
        deck_name = player["deck_name"]
        overlay_window = PlayerOverlayWindow(game_state, player_name, deck_name)
        overlay_window.setWindowTitle(f"{player_name} Overlay")
        overlay_window.resize(OVERLAY_WINDOW_WIDTH, OVERLAY_WINDOW_HEIGHT)
        overlay_window.show()
        overlay_windows.append(overlay_window)
        logger.debug("Created overlay window for %s", player_name)

    logger.debug("All overlay windows created and displayed")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
