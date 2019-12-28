"""hello"""
# -*- coding: utf-8 -*-
import pygame as pg
import Labyrinthe.Package.surroundings as sd


class Maze:
    """
    Building in progress...
    """
    def __init__(self, window_size):
        """
        Building in progress...
        """
        state = True
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
        x = 0
        y = 0
        walls_group = pg.sprite.Group()
        matrix_content = open_file("./Package/good_matrix_pattern_with_characters.txt")
        matrix = "".join(matrix_content)
        matrix = matrix.replace("\n", "")
        while (y and x) < self.window_size:
            for element in matrix:
                if x == self.window_size:
                    x = 0
                    y += 50
                if element == "#":
                    wall = sd.SurroundigsSprite()
                    wall.set_position(x, y)
                    wall.set_image("./Package/Pictures/Wall/big_brown_block.png")
                    walls_group.add(wall)
                    walls_group.draw(window_displayed)
                else:
                    pass
                x += 50
            break
        return walls_group


def open_file(path_file):
    """ This function open the file with the path
    provided as argument. The content file is returned
    into list.
    :param path_file:
    :return list_file: """

    with open(path_file,"rt") as file:
        list_file = file.readlines()
    print("=" * 150)
    print("\nThere is the file content : {}\n".format(path_file))
    for index, line in enumerate(list_file):
        print("line {} : {}".format(index, line))
    print("=" * 150)
    print("\nEnd of file\n")
    print("=" * 150)
    return list_file










