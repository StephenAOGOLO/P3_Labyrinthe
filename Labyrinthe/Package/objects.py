"""
Welcome to the object module, 'objects.py'.
This module is used to create and manage the objects in the game.
One class method inform on total picked game objects.
Three methods help to create and handle each game object.
Four functions allow to display each object in the game.
"""
# -*- coding: utf-8 -*-
import logging as lg
import random as rd
import pygame as pg
from Package import options as opt


lg.basicConfig(level=lg.WARNING)


class ObjectSprite(pg.sprite.Sprite):
    """
    This class is a concrete class of Sprite which is the base class.
    This class manage each game object as pygame sprite's.
    """
    list_status_objects = [False, False, False]

    @classmethod
    def total_objects(cls):
        """
        This class method is the main counter of the collected game objects.
        :return:
        """
        total_state = False
        total = ObjectSprite.list_status_objects.count(True)
        if total == 3:
            total_state = True
        return total_state

    def __init__(self, name, width=50, height=50):
        """
        This constructor calls the Sprite class constructor to inherit it.
        the instance needs a name and dimension to be created.
        A fifty per fifty pixels square is created by default.
        :param name:
        :param width:
        :param height:
        """
        super(ObjectSprite, self).__init__()
        self.name = name
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.picked_status = False

    def set_position(self, a_x, a_y):
        """
        This method is called to set the instance on the window.
        The parameters are integers.
        :param a_x:
        :param a_y:
        :return:
        """
        self.rect.x = a_x
        self.rect.y = a_y

    def set_image(self, filename=None):
        """
        This method is use to change the picture of the instance.
        :param filename:
        :return:
        """
        if filename is not None:
            self.image = pg.image.load(filename)

    def add_picked_object(self):
        """
        This method is the sub counter of the collected game objects.
        :return:
        """
        object_state = False
        if self.opened == 1:
            ObjectSprite.picked_objects = + 1
            object_state = True
        return object_state


def update_dashboard(window_displayed):
    """
    This function creates a dashboard at the top of the game.
    It shows which game object is collected.
    :param window_displayed:
    :return:
    """
    inventory = pg.image.load("./Pictures/i/area_void.png")
    status_dashboard = ObjectSprite.list_status_objects
    if status_dashboard == [False, False, False]:
        inventory = pg.image.load("./Pictures/i/area_void.png")
    elif status_dashboard == [True, False, False]:
        inventory = pg.image.load("./Pictures/i/n.png")
    elif status_dashboard == [False, True, False]:
        inventory = pg.image.load("./Pictures/i/t.png")
    elif status_dashboard == [False, False, True]:
        inventory = pg.image.load("./Pictures/i/e.png")
    elif status_dashboard == [True, True, False]:
        inventory = pg.image.load("./Pictures/i/nt.png")
    elif status_dashboard == [False, True, True]:
        inventory = pg.image.load("./Pictures/i/te.png")
    elif status_dashboard == [True, False, True]:
        inventory = pg.image.load("./Pictures/i/ne.png")
    elif status_dashboard == [True, True, True]:
        inventory = pg.image.load("./Pictures/i/s.png")
    window_displayed.blit(inventory, (210, 0))
    return inventory


def set_objects(window_displayed):
    """
    This function set all the game objects into the maze.
    It is called at the initialization of the program.
    :param window_displayed:
    :return:
    """
    var_y = 0
    var_x = 0
    list_sprites = []
    dict_shuffle = shuffle_objects()
    dict_objects = dict_shuffle["dict_objects"]
    matrix = dict_shuffle["matrix"]
    objects_group = pg.sprite.Group()
    while (var_y and var_x) < 850:
        for key, value in dict_objects.items():
            var_y = 0
            var_x = 0
            for var_e, element in enumerate(matrix):
                if var_x == 850:
                    var_x = 0
                    var_y += 50
                if element == "_" and var_e == value:
                    object_settings = opt.SettingsObject()
                    object_sprite = ObjectSprite(key)
                    object_sprite.set_position(var_x, var_y)
                    lg.info(object_sprite.rect)
                    object_sprite.set_image(str(object_settings.data_file["path_picture"]))
                    objects_group.add(object_sprite)
                    list_sprites.append(object_sprite)
                    break
                var_x += 50
        break
    objects_group.draw(window_displayed)
    return list_sprites


def shuffle_objects():
    """
    This function generates random postion for each game object.
    these positions will be use to set each game object in the maze.
    :return:
    """
    matrix = open_file("./Package/good_matrix_pattern_with_characters.txt")
    matrix = "".join(matrix)
    matrix = matrix.replace("\n", "")
    list_forbidden = [15, 32, 49, 48, 127]
    list_index = [index for index, char in enumerate(matrix) if char == "_"]
    for index in list_forbidden:
        if index in list_index:
            list_index.remove(index)
    random_values = rd.sample(list_index, k=3)
    dict_objects = {"Needle": random_values[0], "Tube": random_values[1], "Ether": random_values[2]}
    dict_shuffle = {"dict_objects": dict_objects, "matrix": matrix}
    return dict_shuffle


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
