#!/usr/bin/env python3

from console.ScreenManager import ScreenManager
import time

def main():
    # Initialize ScreenManager
    screen_manager = ScreenManager()
    
    # Simulate application startup
    screen_manager.setup_screen()
    
    # Simulate application running
    print("The application is now running...")
    time.sleep(2)  # This simulates some activity; you can replace it with real operations

    main_menu = {
            '1': 'Start New Chat',
            '2': 'Load Existing Chat',
            '3': 'Configure Settings',
            '4': 'Exit Application'
        }

    # display the main menu
    screen_manager.display_menu(main_menu)

    time.sleep(3)

    # Simulate application exit
    screen_manager.teardown_screen()

if __name__ == "__main__":
    main()
