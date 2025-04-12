# TCG Card Studio: Live Game Overlay & Input System

**TCG Card Studio** is a Python-based, multi-window application designed to help streamers and event organizers track and display the state of trading card game matches in real time. It provides individual input windows for players and corresponding, draggable overlay windows for live streaming.

## Overview

This project enables you to:

- **Collect Player Information:**  
  Enter each player's name, deck name, and decklist (pasted in standard format).

- **Manage Game State:**  
  The application maintains a central game state (hands and life totals) using PyQt signals for real-time updates.

- **Player Input Windows:**  
  Each player gets an individual input window where they can:
  - Select cards from a drop-down (populated from their decklist) to add to their hand.
  - Remove cards when played.
  - Update their life totals.

- **Individual Overlay Windows:**  
  For each player, a dedicated overlay window is available for live streaming. Each overlay window displays:
  - **Deck Name** (bold)  
  - **Player Name** (in a slightly smaller font)  
  - **Life Total:** the current life total  
  - **Cards In Hand:** a header followed by cards listed vertically  
  The overlays are frameless, mostly transparent, and draggable, so you can position them wherever best on your screen.

## Features

- **Setup Dialog:**  
  Input per-player details (name, deck name, and decklist pasted directly in text).

- **Real-Time Game State Management:**  
  Uses PyQt’s signal/slot mechanism to propagate changes instantly across all windows.

- **Customizable Input & Overlay Windows:**  
  Allows players to update game state through a user-friendly interface and provides streamer-friendly overlays that can be repositioned as needed.

- **Draggable Overlays:**  
  The overlay windows implement custom mouse events to allow repositioning via drag and drop.

## Installation

### Clone the Repository

```bash
git clone https://github.com/BaxterKrug/TCG_Card_Studio.git
cd TCG_Card_Studio

### Set Up a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

## Usage
### Launch the Application:

    python main.py

### Setup Dialog:
    A setup dialog will appear for each player. Enter the following details:

        Player Name

        Deck Name

        Decklist: Paste the decklist in the standard format (with "Deck" and "Sideboard" sections)

    Click OK when complete.

    Player Input Windows & Overlays:

        The application creates a separate input window for each player to update life totals and manage cards.

        An overlay window is also created for each player. This overlay displays their deck name, player name, life total, and the cards currently in hand.

        You can drag the overlay windows to any position on your screen for optimal streaming layout.

## Project Structure

TCG_Card_Studio/
├── config.py              # Configuration constants (window sizes, fonts, etc.)
├── game_state.py          # Central game state management
├── main.py                # Application entry point
├── overlay_window.py      # Contains PlayerOverlayWindow class for streamer overlays
├── player_window.py       # Window for player input operations
├── setup_dialog.py        # Setup dialog for entering player info and decklists
├── utils.py               # Utility functions (logging, formatting, etc.)
├── requirements.txt       # List of project dependencies (e.g., PyQt5)
└── LICENSE                # License file (MIT License)

## Contributing

Contributions, suggestions, and bug reports are welcome! Please open an issue or submit a pull request. When contributing, ensure adherence to standard code style and include proper documentation with your changes.
License

This project is released under the MIT License. See the LICENSE file for more details.
Additional Documentation

## Usage Tips:

    For best results during live streaming, experiment with the overlay window positions and transparency settings in config.py.

## Final Words

Thank you for checking out TCG Card Studio: Live Game Overlay & Input System! Your contributions and feedback help improve this project. If you have any questions or need additional support, please open an issue in the repository.
