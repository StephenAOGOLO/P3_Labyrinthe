"""
Welcome to the main program 'main.py'.
When it starts the program process is following the steps below:
- The initialization
- The provided parameters
- The player management
- The endgame:
"""
# -*- coding: utf-8 -*-
import logging as lg
import pygame as pg
from Package import loading as ld
from Package import characters as ch


lg.basicConfig(level=lg.WARNING)


def main():
    """
     the function main() uses PYGAME module to start,
     manage and stop each events of the game session.
     It obtains the following parameters
     given by the function initialize_game():
     The MacGyver player, The Watchman player,
     the game objects and the graphical window.
     Once the game is running, each event of the session game
     is analysed to change the behaviour of the player.
     So the program is looping on MacGyver's methods,
     until the his sprite collide with the watchman one.
     The program stops either when it happens
     or once the user left-click on the dedicated button to close the window.
    """
    pg.init()
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
    list_state = []
    dict_parameters = ld.initialize_game()
    player = dict_parameters["mc_gyver_sprite"]
    watchman_sprite = dict_parameters["watchman_sprite"]
    window_displayed = dict_parameters["window_displayed"]
    list_objects = dict_parameters["list_objects"]
    list_groups = dict_parameters["list_groups"]
    char_group = list_groups[0]
    player_group = list_groups[1]
    watchman_group = list_groups[2]
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
            ghost_reset = player.reset_ghost_sprite(dict_parameters["list_ghost"])
            ghost_state = ch.handle_collision(ghost_reset, dict_parameters["walls_group"])
            dict_state = player.get_move_state(ghost_state, event)
            list_state = player.attitude(dict_state, watchman_sprite, char_group, list_objects)
            ch.draw_characters(char_group, player_group, watchman_group, window_displayed)
            if list_state[0] is True:
                launched = False
                break
        pg.time.Clock().tick(dict_parameters["fps"])
        pg.display.update()
    dict_parameters["window"].game_over(list_state[1], window_displayed)
    pg.quit()


if __name__ == "__main__":
    main()
