# -*- coding: utf-8 -*-
import pygame as pg
import logging as lg
import random as rd
import Labyrinthe.Package.Options as Opt


lg.basicConfig(level=lg.WARNING)


class ObjectSprite(pg.sprite.Sprite):
    """

    """
    list_status_objects = [False, False, False]

    @classmethod
    def total_objects(cls):
        """

        :return:
        """
        total = ObjectSprite.list_status_objects.count(True)
        if total == 3:
            return True
        else:
            return False

    def __init__(self, name, width=50, height=50):
        """

        :param name:
        :param width:
        :param height:
        """
        super(ObjectSprite, self).__init__()
        self.name = name
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.picked_status = False

    def set_position(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        self.rect.x = x
        self.rect.y = y

    def set_image(self, filename=None):
        """

        :param filename:
        :return:
        """
        if filename is not None:
            self.image = pg.image.load(filename)

    def add_picked_object(self):
        """

        :return:
        """
        if self.opened == 1:
            ObjectSprite.picked_objects = + 1
            return True
        else:
            return False


def update_dashboard(window_displayed):
    """

    :param window_displayed:
    :return:
    """
    inventory = pg.image.load("./Package/Pictures/Inventory/area_void.png")
    status_dashboard = ObjectSprite.list_status_objects
    if status_dashboard == [False, False, False]:
        inventory = pg.image.load("./Package/Pictures/Inventory/area_void.png")
    elif status_dashboard == [True, False, False]:
        inventory = pg.image.load("./Package/Pictures/Inventory/n.png")
    elif status_dashboard == [False, True, False]:
        inventory = pg.image.load("./Package/Pictures/Inventory/t.png")
    elif status_dashboard == [False, False, True]:
        inventory = pg.image.load("./Package/Pictures/Inventory/e.png")
    elif status_dashboard == [True, True, False]:
        inventory = pg.image.load("./Package/Pictures/Inventory/nt.png")
    elif status_dashboard == [False, True, True]:
        inventory = pg.image.load("./Package/Pictures/Inventory/te.png")
    elif status_dashboard == [True, False, True]:
        inventory = pg.image.load("./Package/Pictures/Inventory/ne.png")
    elif status_dashboard == [True, True, True]:
        inventory = pg.image.load("./Package/Pictures/Inventory/s.png")
    window_displayed.blit(inventory, (210, 0))
    return inventory


def set_objects(window_displayed):
    """

    :param window_displayed:
    :return:
    """
    matrix = open_file("./Package/good_matrix_pattern_with_characters.txt")
    matrix = "".join(matrix)
    matrix = matrix.replace("\n", "")
    list_sprites = []
    list_forbidden = [15, 32, 49, 48, 127]
    list_index = [index for index, char in enumerate(matrix) if char == "_"]
    for index in list_forbidden:
        if index in list_index:
            list_index.remove(index)
    three_random_index = rd.sample(list_index, k=3)
    dict_objects = {"Needle": three_random_index[0], "Tube": three_random_index[1], "Ether": three_random_index[2]}
    y = 0
    x = 0
    end_window = 850
    objects_group = pg.sprite.Group()
    while (y and x) < end_window:
        for key, value in dict_objects.items():
            y = 0
            x = 0
            for e, element in enumerate(matrix):
                if x == end_window:
                    x = 0
                    y += 50
                if element == "_" and e == value:
                    object_settings = Opt.SettingsObject()
                    object_sprite = ObjectSprite(key)
                    object_sprite.set_position(x, y)
                    lg.info(object_sprite.rect)
                    object_sprite.set_image(str(object_settings.data_file["path_picture"]))
                    objects_group.add(object_sprite)
                    list_sprites.append(object_sprite)
                    break
                x += 50
        break
    objects_group.draw(window_displayed)
    return list_sprites


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

