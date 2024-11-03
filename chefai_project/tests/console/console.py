#!/usr/bin/python3

"""
CHEFAI CONSOLE - this may end up being the entry point
"""

from menu_manager import MenuManager
from screen_manager import ScreenManager
from command_processor import CommandProcessor
from error_handler import ErrorHandler


def main():
    screen_manager = ScreenManager()
    menu_manager = MenuManager()
    command_processor = CommandProcessor(menu_manager, screen_manager)
    error_handler = ErrorHandler()

    screen_manager.setup_screen()
    active = True
    while active:
        try:
            # the main menu is the first menu
            menu_choice = menu_manager.display_main_menu()
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
