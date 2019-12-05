# coding: utf-8

import pygame as pg
import configparser as cp
import Labyrinthe.Package.Window as Wd
import Labyrinthe.Package.Characters as Character


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


class SettingsWindow(Settings):
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.data_file = self.get_data_file_ini("window_main")


class SettingsCharacter(Settings):
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.data_file = self.get_data_file_ini("window_main")


class SettingsObject(Settings):
    """
    Building in progress...
    """
    def __init__(self):
        """
        Building in progress...
        """
        super().__init__()
        self.data_file = self.get_data_file_ini("window_main")


def main():
    """
    All the main operations are handle into this function.
    When this funtion is running, a green window is launched.
    Two pictures are loaded and set.
    """

    watchman_settings = SettingsWindow()
    mc_gyver_settings = SettingsWindow()
    window_settings = SettingsWindow()
    window_base = Wd.Window(int(window_settings.data_file["window_width"]),
                            int(window_settings.data_file["window_height"]))
    mc_gyver = Character.Characters("Mac Gyver", "./Package/Pictures/MacGyver.png", 150, 200)
    watchman = Character.Characters("WatchMan", "./Package/Pictures/Gardien.png", 300, 200)
    mc_gyver_avatar = mc_gyver.load_character_picture()
    watchman_avatar = watchman.load_character_picture()
    surface = window_base.display_window()
    Wd.color_window(surface)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        mc_gyver.set_avatar(mc_gyver_avatar, surface)
        watchman.set_avatar(watchman_avatar, surface)
        pg.display.update()
    pg.quit()


if __name__ == "__main__":

    main()
