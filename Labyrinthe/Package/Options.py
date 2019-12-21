# -*- coding: utf-8 -*-

import configparser as cp


class Settings:
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        self.file_ini = ".\\Package\\settings.ini"
        self.all_sections_file = self.get_all_sections_file_ini()

    def get_data_file_ini(self, section):
        """
        This function picks all data of a specified section from 'settings.ini'.


        :param section:
        :return data:
        """
        data = {}
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        for j in config.options(section):
            data[str(j)] = str(config.get(section, j))
        return data

    def get_option_file_ini(self, section):
        """
        This function picks all options of a specified section from 'settings.ini'.

        :param section:
        :return config.options(section):
        """
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        return config.options(section)

    def get_all_sections_file_ini(self):
        """
        This function picks all sections from 'settings.ini'.

        :return:
        """
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        return config.sections()

    def get_particular_sections(self, pattern):
        list_particular_section = []
        for section in self.all_sections_file:
            if pattern in section:
                list_particular_section.append(section)
        return list_particular_section


class SettingsWindow(Settings):
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("window_")
        self.data_file = self.get_data_file_ini("window_main")
        self.all_sections = self.get_all_sections_file_ini()


class SettingsCharacter(Settings):
    """
    Building in progress...
    """
    CREATION = 0

    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("character_")
        self.characters = self.sort_all_characters()
        if self.CREATION == 0:
            self.data_file = self.get_data_file_ini("character_mac_gyver")
        elif self.CREATION == 1:
            self.data_file = self.get_data_file_ini("character_watchman")
        SettingsCharacter.CREATION += 1


    def __repr__(self):
        """
        Show the feature of a window
        :return:message
        """
        message = "*****\nType: {}\nsections: {}\n*****"\
            .format(type(self), [item for item in self.characters.items()])
        return message

    def sort_all_characters(self):

        dict_characters = {}
        mac_gyver = "mac_gyver"
        watchman = "watchman"
        for section in self.particular_sections:
            if str(section[10:]) == mac_gyver:
                dict_characters[mac_gyver] = self.get_data_file_ini(section)
            elif str(section[10:]) == watchman:
                dict_characters[watchman] = self.get_data_file_ini(section)
        return dict_characters


class SettingsObject(Settings):
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("object_")
        self.data_file = self.get_data_file_ini("window_main")


class SettingsSurroundings(Settings):
    """
    Building in progress...
    """
    CREATION = 0
    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("surroundings_")
        self.element = self.sort_all_elements()
        if self.CREATION == 0:
            self.data_file = self.get_data_file_ini("surroundings_brown_block")
        elif self.CREATION == 1:
            pass

    def sort_all_elements(self):

        dict_elements = {}
        brown_block = "mac_gyver"
        add_another_block = "add_another_block"
        for section in self.particular_sections:
            if str(section[13:]) == brown_block:
                dict_elements[brown_block] = self.get_data_file_ini(section)
            elif str(section[13:]) == add_another_block:
                dict_elements[add_another_block] = self.get_data_file_ini(section)
        return dict_elements
