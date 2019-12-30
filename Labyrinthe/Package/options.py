"""
Welcome to the option module, 'options.py'.
This module is used to pick some parameters from an external file.
It contains four classes whose an abstract class and three concrete ones.
Each concrete class are called for the program initialization.
"""
# -*- coding: utf-8 -*-
import configparser as cp


class Settings:
    """
    This class manage data parameters stored in a external file.
    """
    def __init__(self):
        """
        This constructor create a instance which contains all the data from a file ini.
        """
        self.file_ini = ".\\Package\\settings.ini"
        self.all_sections_file = self.get_all_sections_file_ini()

    def get_data_file_ini(self, section):
        """
        This method picks all data of a specified section from 'settings.ini'.


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
        This method picks all options of a specified section from 'settings.ini'.

        :param section:
        :return config.options(section):
        """
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        return config.options(section)

    def get_all_sections_file_ini(self):
        """
        This method picks all sections from 'settings.ini'.

        :return:
        """
        config = cp.RawConfigParser()
        config.read(self.file_ini)
        return config.sections()

    def get_particular_sections(self, pattern):
        """
        This method picks all options from a given section 'pattern'
        :param pattern:
        :return:
        """
        list_particular_section = []
        for section in self.all_sections_file:
            if pattern in section:
                list_particular_section.append(section)
        return list_particular_section


class SettingsWindow(Settings):
    """
    Base class : Settings
    This concrete class manage data parameters stored in a external file concerning Window instance.
    """
    def __init__(self):
        """
        This constructor create a instance which contains all the Window data from a file ini.
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("window_")
        self.data_file = self.get_data_file_ini("window_main")
        self.all_sections = self.get_all_sections_file_ini()


class SettingsCharacter(Settings):
    """
    Base class : Settings
    This concrete class manage data parameters stored in a external file concerning Character instance.
    """
    CREATION = 0

    def __init__(self):
        """
        This constructor create a instance which contains all the Character data from a file ini.
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("character_")
        self.characters = self.sort_all_characters()
        if self.CREATION == 0:
            self.data_file = self.get_data_file_ini("character_mac_gyver")
        elif self.CREATION == 1:
            self.data_file = self.get_data_file_ini("character_watchman")
        SettingsCharacter.CREATION += 1

    def sort_all_characters(self):
        """
        This function automatically picks data concerning an implicit given section.
        :return:
        """
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
    Base class : Settings
    This concrete class manage data parameters stored in a external file concerning Object instance.
    """
    CREATION = 0

    def __init__(self):
        """
        This constructor create a instance which contains all the Object data from a file ini.
        """
        super().__init__()
        self.particular_sections = self.get_particular_sections("object_")
        if self.CREATION == 0:
            self.data_file = self.get_data_file_ini("object_needle")
        elif self.CREATION == 1:
            self.data_file = self.get_data_file_ini("object_tube")
        elif self.CREATION == 2:
            self.data_file = self.get_data_file_ini("object_ether")
        SettingsObject.CREATION += 1
