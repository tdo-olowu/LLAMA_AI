#!/usr/bin/env python3

"""
MENU MANAGER
    This has the following duties:
    -   Keep track of all possible menus in the application
    -   Represent the menus as some sort of data structure
    -   Keep track of what choice the user has made
    -   Keep track of the current menu
"""

class MenuManager:
    # menu data structures
    _all_menus = {
        'main_menu': {
            '1': 'Start New Chat',
            '2': 'Load Existing Chat',
            '3': 'Configure Settings',
            '4': 'Exit Application'
        },
        # Add other menus here as needed
    }

    @classmethod
    def get_menu(cls, menu_name):
        """Retrieve the options dictionary for a specific menu by name."""
        return cls._all_menus.get(menu_name, {})

    @classmethod
    def get_option(cls, menu_name, option_number):
        """Retrieve a specific option from a menu, if it exists."""
        menu = cls._all_menus.get(menu_name, {})
        return menu.get(option_number)
