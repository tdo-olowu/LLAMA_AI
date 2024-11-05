#!/usr/bin/python3

"""
CHEFAI CONSOLE - this may end up being the entry point
"""

from MenuManager import MenuManager
from ScreenManager import ScreenManager
from CommandProcessor import CommandProcessor
from ErrorHandler import ErrorHandler


def main():
    screen_manager = ScreenManager()
    menu_manager = MenuManager()
    command_processor = CommandProcessor(menu_manager, screen_manager)
    error_handler = ErrorHandler()

    screen_manager.setup_screen()
    active = True
    # initialize the main menu somewhere here.
    menu = menu_manager._main_menu # this is a class attr so fix the code
    while active:
        try:
            # the main menu is the first menu
            menu_choice = menu_manager.get_user_choice()
            # think of this as its own inner loop
            command_processor.process_command(menu_choice)
        except Exception as e:
            error_handler.handle_error(e)
        if (command_processor.should_exit()):
            command_processor.cleanup()
            active = False
    screen_manager.teardown_screen()


if __name__ == '__main__':
    main()
