# setup_dialog.py
import sys
import re
from PyQt5.QtWidgets import (
    QDialog, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTextEdit, QApplication, QGroupBox, QFormLayout
)

def parse_decklist(text):
    """
    Parse a decklist text and return a dictionary for main deck and sideboard.
    Expected format example:
    
    Deck
    4 Emberheart Challenger
    4 Heartfire Hero
    4 Hired Claw
    3 Monastery Swiftspear
    ...
    Sideboard
    2 Witchstalker Frenzy
    2 Sunspine Lynx
    ...
    """
    main_deck = {}
    sideboard = {}
    current_section = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.lower() == "deck":
            current_section = main_deck
            continue
        elif line.lower() == "sideboard":
            current_section = sideboard
            continue
        
        match = re.match(r'^(\d+)\s+(.*)$', line)
        if match and current_section is not None:
            count = int(match.group(1))
            card_name = match.group(2)
            current_section[card_name] = count
    return {"main_deck": main_deck, "sideboard": sideboard}

class SetupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Setup Game Configuration")
        self.setup_ui()
        # Will hold parsed decklist and player info for each player as dictionaries
        self.players_info = []

    def setup_ui(self):
        layout = QVBoxLayout()

        # Create group boxes for each player's inputs.
        # Player 1 Group
        player1_group = QGroupBox("Player 1 Configuration")
        player1_layout = QFormLayout()

        self.player1_name_edit = QLineEdit()
        self.player1_name_edit.setPlaceholderText("Enter Player 1 Name")
        player1_layout.addRow("Player 1 Name:", self.player1_name_edit)

        self.player1_deck_edit = QLineEdit()
        self.player1_deck_edit.setPlaceholderText("Enter Player 1 Deck Name")
        player1_layout.addRow("Player 1 Deck Name:", self.player1_deck_edit)

        self.player1_decklist_edit = QTextEdit()
        self.player1_decklist_edit.setPlaceholderText(
            "Paste Player 1 Decklist here:\n"
            "Deck\n"
            "4 Emberheart Challenger\n"
            "4 Heartfire Hero\n"
            "4 Hired Claw\n"
            "3 Monastery Swiftspear\n"
            "...\n\n"
            "Sideboard\n"
            "2 Witchstalker Frenzy\n"
            "2 Sunspine Lynx\n"
            "..."
        )
        player1_layout.addRow("Player 1 Decklist:", self.player1_decklist_edit)

        player1_group.setLayout(player1_layout)
        layout.addWidget(player1_group)

        # Player 2 Group
        player2_group = QGroupBox("Player 2 Configuration")
        player2_layout = QFormLayout()

        self.player2_name_edit = QLineEdit()
        self.player2_name_edit.setPlaceholderText("Enter Player 2 Name")
        player2_layout.addRow("Player 2 Name:", self.player2_name_edit)

        self.player2_deck_edit = QLineEdit()
        self.player2_deck_edit.setPlaceholderText("Enter Player 2 Deck Name")
        player2_layout.addRow("Player 2 Deck Name:", self.player2_deck_edit)

        self.player2_decklist_edit = QTextEdit()
        self.player2_decklist_edit.setPlaceholderText(
            "Paste Player 2 Decklist here:\n"
            "Deck\n"
            "4 Emberheart Challenger\n"
            "4 Heartfire Hero\n"
            "4 Hired Claw\n"
            "3 Monastery Swiftspear\n"
            "...\n\n"
            "Sideboard\n"
            "2 Witchstalker Frenzy\n"
            "2 Sunspine Lynx\n"
            "..."
        )
        player2_layout.addRow("Player 2 Decklist:", self.player2_decklist_edit)

        player2_group.setLayout(player2_layout)
        layout.addWidget(player2_group)

        # Dialog Buttons
        buttons_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        buttons_layout.addWidget(ok_button)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        buttons_layout.addWidget(cancel_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def get_setup_data(self):
        """
        Processes the data from the dialog and returns a dictionary with players' information.
        Each player's dictionary includes their name, deck name, and parsed decklist data.
        """
        players_info = []

        # Process Player 1 inputs
        p1_name = self.player1_name_edit.text().strip() or "Player 1"
        p1_deck = self.player1_deck_edit.text().strip() or "Deck 1"
        p1_decklist_text = self.player1_decklist_edit.toPlainText().strip()
        if p1_decklist_text:
            p1_decklist = parse_decklist(p1_decklist_text)
        else:
            p1_decklist = None

        players_info.append({
            "player_name": p1_name,
            "deck_name": p1_deck,
            "decklist": p1_decklist
        })

        # Process Player 2 inputs
        p2_name = self.player2_name_edit.text().strip() or "Player 2"
        p2_deck = self.player2_deck_edit.text().strip() or "Deck 2"
        p2_decklist_text = self.player2_decklist_edit.toPlainText().strip()
        if p2_decklist_text:
            p2_decklist = parse_decklist(p2_decklist_text)
        else:
            p2_decklist = None

        players_info.append({
            "player_name": p2_name,
            "deck_name": p2_deck,
            "decklist": p2_decklist
        })

        self.players_info = players_info
        return {"players": self.players_info}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = SetupDialog()
    if dialog.exec_() == QDialog.Accepted:
        setup_data = dialog.get_setup_data()
        print(setup_data)
    sys.exit(0)
