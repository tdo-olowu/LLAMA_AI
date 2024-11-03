#!/usr/bin/env python3

"""
SCREEN MANAGER
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

import os
import time

class ScreenManager:
    # wait_time in seconds
    wait_time = 2
    intro_screen = "Welcome to ChefAI, your culinary assistant!"
    outro_screen = "Thank you for using chefAI. Goodbye"

    def __init__(self):
        """what arguments may this need in future?"""
        pass

    def setup_screen(self):
        self._clear_screen()
        self._intro()
        time.sleep(ScreenManager.wait_time) # or let user exit by themselves.

    def teardown_screen(self):
        self._outro()
        time.sleep(ScreenManager.wait_time) # also let user quit if they wanna
        self._restore_screen()

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _intro(self):
        print(ScreenManager.intro_screen)
        # input("Press Enter to continue")

    def _outro(self):
        self._clear_screen()
        print(ScreenManager.outro_screen)

    def _set_color(self):
        pass

    def _restore_screen(self):
        """intended to restore previous state of screen.
        not sure if this is needed but will leave it in for now
        """
        pass

    def display_menu(self, menu_data):
        """Given data representing the menu, ScreenManager object
        decides how to present it to the user.
        Currently, a menu is a dictionary of the form
            Serial_no : option_name
        """
        self._clear_screen()
        for sn, opt_name in menu_data.items():
            print(sn, opt_name)
