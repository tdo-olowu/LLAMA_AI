#!/usr/bin/env python3

"""
SCREEN MANAGER TEST
Manages the terminal screen.
Its has three jobs right now:
    - keep track of screen state when asked (for later restoration)
    - clear the screen
    - color the screen and text
    - position the cursor
    - restore the state of the screen when asked
    - intro and outro screens
That seems like a lot, but I don't want too many clases.
The ScreenManager to primarily manage look and feel, not functionality, but I will allow it to also clear the screen, memorize the screen and do greetings.
"""

import unittest
from unittest.mock import patch, call
import time
from console.ScreenManager import ScreenManager

class TestScreenManager(unittest.TestCase):

    @patch("console.ScreenManager.time.sleep", return_value=None)
    @patch("console.ScreenManager.ScreenManager._clear_screen")
    @patch("builtins.print")
    def test_setup_screen(self, mock_print, mock_clear_screen, mock_sleep):
        # Create an instance of ScreenManager
        screen_manager = ScreenManager()

        # Call setup_screen to test its behavior
        screen_manager.setup_screen()

        # Assert clear_screen is called
        mock_clear_screen.assert_called_once()

        # Assert intro is printed
        mock_print.assert_called_once_with(ScreenManager.intro_screen)

        # Assert sleep is called
        mock_sleep.assert_called_once_with(ScreenManager.wait_time)

    @patch("console.ScreenManager.time.sleep", return_value=None)
    @patch("console.ScreenManager.ScreenManager._clear_screen")
    @patch("builtins.print")
    def test_teardown_screen(self, mock_print, mock_clear_screen, mock_sleep):
        screen_manager = ScreenManager()

        # Call teardown_screen to test its behavior
        screen_manager.teardown_screen()

        # Assert outro is printed
        mock_print.assert_called_once_with(ScreenManager.goodbye_screen)

        # Assert sleep is called
        mock_sleep.assert_called_once_with(ScreenManager.wait_time)

    @patch("console.ScreenManager.os.system")
    def test_clear_screen(self, mock_os_system):
        screen_manager = ScreenManager()

        # Call _clear_screen to test its behavior
        screen_manager._clear_screen()

        # Assert os.system is called with the correct command based on OS
        mock_os_system.assert_called_once_with('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    unittest.main()

