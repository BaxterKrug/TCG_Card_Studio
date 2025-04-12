# utils.py
"""
Utility functions for the Live Game Overlay and Input System.
This module includes helper functions for logging, time formatting, and file name sanitization.
"""

import logging
import os
import re
from config import DEBUG_MODE, LOG_FILE


def init_logger():
    """
    Initialize and return a logger configured to output messages to both the console and a file.
    The logging level is set to DEBUG if DEBUG_MODE is True in the config.
    
    Returns:
        logger (logging.Logger): Configured logger instance.
    """
    logger = logging.getLogger("LiveOverlayApp")
    # Avoid adding multiple handlers if the logger is already configured
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)

    # File handler configuration
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    
    # Console handler configuration
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.debug("Logger initialized")
    return logger


def format_time(seconds):
    """
    Format a given time in seconds into a string in the format HH:MM:SS.
    
    Args:
        seconds (int or float): Number of seconds to format.
        
    Returns:
        str: Formatted time string.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def safe_filename(filename):
    """
    Sanitize a string to be a safe filename by replacing any non-alphanumeric character (except
    underscores, hyphens, and periods) with an underscore.
    
    Args:
        filename (str): The original filename.
        
    Returns:
        str: Sanitized filename.
    """
    return re.sub(r'[^A-Za-z0-9_.-]', '_', filename)


def ensure_dir(directory):
    """
    Ensure that the given directory exists. If not, create it.
    
    Args:
        directory (str): The path of the directory to ensure.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
