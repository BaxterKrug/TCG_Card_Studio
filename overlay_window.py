# overlay_window.py
"""
This module defines the PlayerOverlayWindow class for live streaming overlays.
Each overlay window (one per player) displays:
    - Deck Name (bold)
    - Player Name (in smaller font)
    - Life Total (prefixed with "Life Total:")
    - A bold header "Cards In Hand"
    - A vertical list of cards in hand
The window is frameless, mostly transparent, and draggable.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QPoint
from config import OVERLAY_FONT_FAMILY, OVERLAY_FONT_SIZE, OVERLAY_FONT_COLOR, OVERLAY_OPACITY

class PlayerOverlayWindow(QWidget):
    def __init__(self, game_state, player_name, deck_name):
        super().__init__()
        self.game_state = game_state
        self.player_name = player_name
        self.deck_name = deck_name
        self._is_dragging = False
        self._drag_position = QPoint()
        self.init_ui()
        self.game_state.state_updated.connect(self.refresh_overlay)

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(OVERLAY_OPACITY)
        
        self.layout = QVBoxLayout()
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.layout)
        
        self.refresh_overlay()

    def refresh_overlay(self):
        # Remove all widgets.
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Deck Name in bold.
        deck_label = QLabel(self.deck_name)
        deck_label.setStyleSheet(
            f"font-family: {OVERLAY_FONT_FAMILY}; font-size: {OVERLAY_FONT_SIZE}px; font-weight: bold; color: {OVERLAY_FONT_COLOR};"
        )
        self.layout.addWidget(deck_label)
        
        # Player Name in a smaller font.
        player_label = QLabel(self.player_name)
        player_label.setStyleSheet(
            f"font-family: {OVERLAY_FONT_FAMILY}; font-size: {OVERLAY_FONT_SIZE - 4}px; color: {OVERLAY_FONT_COLOR};"
        )
        self.layout.addWidget(player_label)
        
        # Life total.
        life = self.game_state.life_totals.get(self.player_name, 0)
        life_label = QLabel(f"Life Total: {life}")
        life_label.setStyleSheet(
            f"font-family: {OVERLAY_FONT_FAMILY}; font-size: {OVERLAY_FONT_SIZE}px; color: {OVERLAY_FONT_COLOR};"
        )
        self.layout.addWidget(life_label)
        
        # Bold header for the cards section.
        header = QLabel("Cards In Hand")
        header.setStyleSheet(
            f"font-family: {OVERLAY_FONT_FAMILY}; font-size: {OVERLAY_FONT_SIZE}px; font-weight: bold; color: {OVERLAY_FONT_COLOR};"
        )
        self.layout.addWidget(header)
        
        # List cards vertically.
        hand = self.game_state.hands.get(self.player_name, [])
        if hand:
            for card in hand:
                card_label = QLabel(card)
                card_label.setStyleSheet(
                    f"font-family: {OVERLAY_FONT_FAMILY}; font-size: {OVERLAY_FONT_SIZE - 2}px; color: {OVERLAY_FONT_COLOR};"
                )
                self.layout.addWidget(card_label)
        else:
            no_cards = QLabel("No Cards")
            no_cards.setStyleSheet(
                f"font-family: {OVERLAY_FONT_FAMILY}; font-size: {OVERLAY_FONT_SIZE - 2}px; color: {OVERLAY_FONT_COLOR};"
            )
            self.layout.addWidget(no_cards)
        self.layout.addStretch()

    # Enable dragging of the window.
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._is_dragging and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._is_dragging = False
        event.accept()
