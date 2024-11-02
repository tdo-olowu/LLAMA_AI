#!/usr/bin/python3

"""
CHEFAI
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

    screen_manager.clear_screen()
    screen_manager.set_color('green')

    print("Welcome to ChefAI!")

    # Main loop for the application
    while True:
        try:
            # display menu and process the choice
            menu_choice = menu_manager.display_main_menu()
            command_processor.process_command(menu_choice)

        except Exception as e:
            error_handler.handle_application_error(e)
            print("An unexpected error occurred. Please try again.")

        if command_processor.exit_application:
            break

    screen_manager.reset_color()
    print("Thank you for using ChefAI. Goodbye!")



if __name__ == '__main__':
    main()
