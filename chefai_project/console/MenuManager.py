#!/usr/bin/env python3

"""
MENU MANAGER
    This has the following duties:
    -   Keep track of all possible menus in the application
    -   Represent the menus as some sort of data structure
    -   Keep track of what choice the user has made
    -   Keep track of the current menu
"""
from ChatManager import ChatManager

class MenuManager:
    # menu data structures
    _main_menu = ["Start New Chat", "Load Existing Chat",
            "Configuration/Settings", "Exit Application"]
    _settings_menu = ["Color Theme", "Directory Configuration"]
    _all_menus = {
        'main_menu': MenuManager._enumerate_options(
                        MenuManager._main_menu),
        'settings': MenuManager._enumerate_options(
                        MenuManager._settings_menu),
        'chats': ChatManager.see_chats()
    }

    # data for keeping track
    previous_menu = "" # for keeping track of prev state.
    prev_choice = ""
    menu_choice = ""

    @classmethod
    def get_menu(cls, menu_name):
        """Retrieve the options dictionary for a specific menu by name."""
        return cls._all_menus.get(menu_name, {})

    @classmethod
    def get_option(cls, menu_name, option_number):
        """Retrieve a specific option from a menu, if it exists."""
        menu = cls._all_menus.get(menu_name, {})
        return menu.get(option_number)

    def select_option(self, menu_data, opt_number):
        """This returns the name of the option given its number,
        that the CommandProcessor may decide what command to execute.
        """
        # f:menu_data, opt_number -> name
        # make sure to validate the opt_number
        # also, where's 'back'?
        pass

    def get_user_choice(self, menu, index):
        """When a menu is displayed, this lets the user input a number
        corresponding ot an option, then returns the name of the option
        which COmmandProcessor will then use for further processing
        """
        pass

    @classmethod
    def _enumerate_options(cls, options_list):
        """Given a list of menu options e.g. 'Save', etc. will return a dict
        whose keys are a serial number and values are list items.
        """
        resulting_dict = {}
        for index, item in enumerate(options_list):
            resulting_dict[index] = item
        return resulting_dict
