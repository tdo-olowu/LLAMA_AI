#!/usr/bin/python3

"""
CHEFAI
"""

from console.menu_manager import MenuManager
from console.screen_manager import ScreenManager
from console.command_processor import CommandProcessor
from console.error_handler import ErrorHandler


def main():
    # Initialize the console components
    screen_manager = ScreenManager()
    menu_manager = MenuManager()
    command_processor = CommandProcessor(menu_manager, screen_manager)
    error_handler = ErrorHandler()

    # Clear the screen and set up the console appearance
    # try screen_manager.setup()
    screen_manager.clear_screen()
    screen_manager.set_color('green')  # Optional: Set the terminal color

    print("Welcome to ChefAI!")

    # Main loop for the application
    while True:
        try:
            # Display the main menu and get user choice
            menu_choice = menu_manager.display_main_menu()
            # Process the user's command
            command_processor.process_command(menu_choice)

        except Exception as e:
            error_handler.handle_application_error(e)
            print("An unexpected error occurred. Please try again.")

        # Check for exit condition
        if command_processor.exit_application:
            break

    # Reset terminal color when exiting
    screen_manager.reset_color()
    print("Thank you for using ChefAI. Goodbye!")


if __name__ == '__main__':
    main()
