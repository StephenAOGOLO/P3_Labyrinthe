"""
Welcome to the maze module, 'mazes.py'.
This module is mainly composed of 'Maze' class.
Two methods are defined to draw all the maze respecting an external file.
one function is defined to open that external file.
"""
# -*- coding: utf-8 -*-
import pygame as pg
from Package import surroundings as sd


class Maze:
    """
    Building in progress...
    """
    def __init__(self, window_size):
        """
        Building in progress...
        """
        self.window_size = window_size
        self.limit_window_x = self.set_limit_window_size(100)
        self.limit_window_y = self.set_limit_window_size(100)

    def set_limit_window_size(self, limit):
        """

        :param limit:
        :return:
        """

        return self.window_size - limit

    def initialize_maze(self, window_displayed):
        """

        :param window_displayed:
        :return:
        """
        a_x = 0
        a_y = 0
        walls_group = pg.sprite.Group()
        matrix = open_file("./Package/good_matrix_pattern_with_characters.txt")
        matrix = "".join(matrix)
        matrix = matrix.replace("\n", "")
        while (a_y and a_x) < self.window_size:
            for element in matrix:
                if a_x == self.window_size:
                    a_x = 0
                    a_y += 50
                if element == "#":
                    wall = sd.SurroundingsSprite()
                    wall.set_position(a_x, a_y)
                    wall.set_image("./Package/Pictures/Wall/big_brown_block.png")
                    walls_group.add(wall)
                    walls_group.draw(window_displayed)
                else:
                    pass
                a_x += 50
            break
        return walls_group


def open_file(path_file):
    """ This function open the file with the path
    provided as argument. The content file is returned
    into list.
    :param path_file:
    :return list_file: """

    with open(path_file, "rt") as file:
        list_file = file.readlines()
    print("=" * 150)
    print("\nThere is the file content : {}\n".format(path_file))
    for index, line in enumerate(list_file):
        print("line {} : {}".format(index, line))
    print("=" * 150)
    print("\nEnd of file\n")
    print("=" * 150)
    return list_file
