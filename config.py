# config.py
"""
Configuration settings for the Live Game Overlay and Input System.
This file defines constants that are used throughout the application.
"""

# --------------------------
# Game Settings
# --------------------------
# Starting life total for each player
STARTING_LIFE_TOTAL = 20

# --------------------------
# Window Dimensions
# --------------------------
# Dimensions for each player window (width x height in pixels)
PLAYER_WINDOW_WIDTH = 400
PLAYER_WINDOW_HEIGHT = 600

# Dimensions for the overlay window (width x height in pixels)
OVERLAY_WINDOW_WIDTH = 800
OVERLAY_WINDOW_HEIGHT = 200

# --------------------------
# Font and Display Settings
# --------------------------
# Font settings for the overlay (used in streaming output)
OVERLAY_FONT_FAMILY = "Arial"
OVERLAY_FONT_SIZE = 24
OVERLAY_FONT_COLOR = "#FFFFFF"  # White text

# Transparency settings for the overlay window (0.0 is fully transparent, 1.0 is opaque)
OVERLAY_OPACITY = 0.8

# General GUI margins and spacing (in pixels)
WINDOW_MARGIN = 10

# --------------------------
# Network Settings (Optional / Future Enhancements)
# --------------------------
# Enable network communication for multi-device support if required
USE_NETWORK = False  # Set to True if expanding to support remote player inputs

# If networking is enabled, define host and port settings
NETWORK_HOST = "localhost"
NETWORK_PORT = 8000

# --------------------------
# Debug and Logging Settings
# --------------------------
# Enable debug mode to output additional diagnostic information
DEBUG_MODE = True

# Log file path for application logs
LOG_FILE = "app.log"

# --------------------------
# Assets and Resource Paths
# --------------------------
# Path to external assets (if any, e.g., configuration files, icons, etc.)
ASSETS_PATH = "./assets/"
