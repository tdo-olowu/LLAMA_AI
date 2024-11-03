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

    # Simulate application exit
    screen_manager.teardown_screen()

if __name__ == "__main__":
    main()
