"""
Welcome to the loading module, 'loading.py'.
This module is especially composed of one function.
Which is used to initialize and feeds program parameters.
"""
# -*- coding: utf-8 -*-
from Package import mazes as maze
from Package import options as opt
from Package import window as wd
from Package import characters as ch
from Package import objects as obj


def initialize_game():
    """
    This function obtains obtains parameters concerning the folowing needed elements:
    window, MacGyver, Watchman, maze and objects.
    Each of them are formatted with their own class of settings.
    So this function is ran to concentrate these parameters first and return dict ready to use.

    :return: dict_parameters
    """
    dict_parameters = {}
    window_settings = opt.SettingsWindow()
    window_width = int(window_settings.data_file["window_width"])
    window_height = int(window_settings.data_file["window_height"])
    dict_parameters["limit_window_x"] = int(window_settings.data_file["limit_x"])
    dict_parameters["limit_window_y"] = int(window_settings.data_file["limit_y"])
    window_size = int(window_settings.data_file["window_size"])
    window = wd.Window(window_width, window_height)
    clock_settings = opt.SettingsWindow()
    dict_parameters["fps"] = int(clock_settings.data_file["fps"])
    window_displayed = window.display_window()
    window.set_background_on(window_displayed, 0, 0)
    mc_gyver_settings = opt.SettingsCharacter()
    player = ch.CharactersSprite()
    player.set_image(str(mc_gyver_settings.data_file["path_picture"]))
    dict_parameters["list_ghost"] = player.set_ghost_sprite()
    watchman_settings = opt.SettingsCharacter()
    watchman_sprite = ch.CharactersSprite()
    watchman_sprite.set_image(watchman_settings.data_file["path_picture"])
    dict_parameters["list_groups"] = player.needed_groups_for(watchman_sprite)
    the_maze = maze.Maze(window_size)
    dict_parameters["walls_group"] = the_maze.initialize_maze(window_displayed)
    ch.set_in_maze(the_maze, player, watchman_sprite)
    dict_parameters["list_objects"] = obj.set_objects(window_displayed)
    dict_parameters["window"] = window
    dict_parameters["mc_gyver_sprite"] = player
    dict_parameters["watchman_sprite"] = watchman_sprite
    dict_parameters["window_displayed"] = window_displayed
    return dict_parameters
