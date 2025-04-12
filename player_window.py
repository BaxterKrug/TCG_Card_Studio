# player_window.py
"""
This module defines the PlayerWindow class.
Each instance represents an interactive touch-screen panel for a player,
allowing them to add cards to their hand by selecting from the decklist,
remove played cards, and view/update their current life total.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel, QComboBox, QHBoxLayout
from config import STARTING_LIFE_TOTAL
from PyQt5.QtCore import Qt

class PlayerWindow(QWidget):
    def __init__(self, player_name, game_state, decklist):
        """
        Initialize the player window.

        Args:
            player_name (str): Identifier/name of the player.
            game_state (GameState): Shared game state instance.
            decklist (dict): The decklist dictionary (we use the "main_deck" portion).
        """
        super().__init__()
        self.player_name = player_name
        self.game_state = game_state
        # Load available card names from the main deck portion
        self.available_cards = list(decklist.get("main_deck", {}).keys())
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Title label showing player name
        title_label = QLabel(self.player_name)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.layout.addWidget(title_label)

        # Life total label and control buttons
        self.life_label = QLabel(f"Life Total: {self.game_state.life_totals[self.player_name]}")
        self.life_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.life_label)
        
        # Horizontal layout for life control buttons
        life_buttons_layout = QHBoxLayout()
        self.increase_life_btn = QPushButton("Increase Life")
        self.increase_life_btn.clicked.connect(self.increase_life)
        life_buttons_layout.addWidget(self.increase_life_btn)

        self.decrease_life_btn = QPushButton("Decrease Life")
        self.decrease_life_btn.clicked.connect(self.decrease_life)
        life_buttons_layout.addWidget(self.decrease_life_btn)
        self.layout.addLayout(life_buttons_layout)

        # Label for the hand section
        self.hand_label = QLabel("Your Hand:")
        self.layout.addWidget(self.hand_label)

        # List widget to display the current hand
        self.hand_list = QListWidget()
        self.layout.addWidget(self.hand_list)

        # Combo box for selecting a card (instead of typing)
        self.card_combo = QComboBox()
        self.card_combo.addItems(sorted(self.available_cards))
        self.layout.addWidget(self.card_combo)

        # Button to add the selected card to the hand
        add_button = QPushButton("Add Card")
        add_button.clicked.connect(self.add_card)
        self.layout.addWidget(add_button)

        # Button to remove the selected card (simulate playing the card)
        remove_button = QPushButton("Remove Selected Card")
        remove_button.clicked.connect(self.remove_card)
        self.layout.addWidget(remove_button)

        self.setLayout(self.layout)
        # Connect to game state updates
        self.game_state.state_updated.connect(self.refresh_hand)

    def add_card(self):
        """
        Add the card selected in the combo box to the player's hand.
        """
        card_name = self.card_combo.currentText()
        if card_name:
            self.game_state.add_card(self.player_name, card_name)

    def remove_card(self):
        """
        Remove the selected card from the player's hand.
        """
        selected = self.hand_list.currentItem()
        if selected:
            card_name = selected.text()
            self.game_state.play_card(self.player_name, card_name)

    def increase_life(self):
        current_life = self.game_state.life_totals[self.player_name]
        self.game_state.update_life(self.player_name, current_life + 1)

    def decrease_life(self):
        current_life = self.game_state.life_totals[self.player_name]
        self.game_state.update_life(self.player_name, current_life - 1)

    def refresh_hand(self):
        self.hand_list.clear()
        for card in self.game_state.hands[self.player_name]:
            self.hand_list.addItem(card)
        self.life_label.setText(f"Life Total: {self.game_state.life_totals[self.player_name]}")
