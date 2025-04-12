# game_state.py
"""
This module defines the GameState class, which acts as the central repository 
for all game information (player hands and life totals). It uses PyQt signals
to notify other parts of the application when changes occur.
"""

from PyQt5.QtCore import QObject, pyqtSignal
from config import STARTING_LIFE_TOTAL

class GameState(QObject):
    # Signal emitted whenever the game state is updated
    state_updated = pyqtSignal()

    def __init__(self, player_names):
        """
        Initialize the game state using the provided player names.
        
        Args:
            player_names (list of str): List containing the names of all players.
        """
        super().__init__()
        # Use the provided player names as keys
        self.hands = {name: [] for name in player_names}
        self.life_totals = {name: STARTING_LIFE_TOTAL for name in player_names}
    
    def add_card(self, player, card_name):
        if player in self.hands:
            self.hands[player].append(card_name)
            self.state_updated.emit()
    
    def play_card(self, player, card_name):
        if player in self.hands and card_name in self.hands[player]:
            self.hands[player].remove(card_name)
            self.state_updated.emit()
    
    def update_life(self, player, new_life):
        if player in self.life_totals:
            self.life_totals[player] = new_life
            self.state_updated.emit()
