# -*- coding: utf-8 -*-
import pygame as pg
import random as rd
import logging as lg
import Labyrinthe.Package.Objects as Obj


lg.basicConfig(level=lg.WARNING)


class CharactersSprite(pg.sprite.Sprite):
    """

    """
    list_status_objects = [False, False, False]

    def __init__(self, color=(0, 0, 0), width=20, height=20):
        """

        :param color:
        :param width:
        :param height:
        """
        super(CharactersSprite, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.last_x = 400
        self.last_y = 350

    def set_position(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        self.rect.x = x
        self.rect.y = y

    def reset_last_position(self):
        """

        :return:
        """
        self.rect.x = self.last_x
        self.rect.y = self.last_y
        return self.rect.x, self.rect.y

    def set_image(self, filename=None):
        """

        :param filename:
        :return:
        """
        if filename is not None:
            self.image = pg.image.load(filename)
            # self.rect = self.image.get_rect()

    def add_to_group(self, group):
        """

        :param group:
        :return:
        """
        sprite_group = group.add(self)
        return sprite_group

    def start_move_avatar(self, event, list_ghost_status=None):
        """

        :param event:
        :param list_ghost_status:
        :return:
        """
        if list_ghost_status is None:
            list_ghost_status = [True, True, True, True]
        lg.info("event -->", event)
        move_status = False
        picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_s_t_f.png"
        self.last_x = self.rect.x
        self.last_y = self.rect.y
        arrow_key = pg.key.get_pressed()
        if event.type == pg.KEYUP:
            self.set_image(picture_behavior)
        if event.type == pg.KEYDOWN:
            if arrow_key[pg.K_UP] and list_ghost_status[0]:
                mc_gyver_move_y = -50
                mc_gyver_move_x = 0
                self.rect.x += mc_gyver_move_x
                self.rect.y += mc_gyver_move_y
                chance = rd.randrange(1, 3)
                if chance == 1:
                    picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w1_t_f.png"
                else:
                    picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w2_t_f.png"
                self.set_image(picture_behavior)
                move_status = True
            elif arrow_key[pg.K_UP] and not list_ghost_status[0]:
                picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w1_t_f.png"
                self.set_image(picture_behavior)
            elif arrow_key[pg.K_RIGHT] and list_ghost_status[1]:
                mc_gyver_move_x = 50
                mc_gyver_move_y = 0
                self.rect.x += mc_gyver_move_x
                self.rect.y += mc_gyver_move_y
                chance = rd.randrange(1, 3)
                if chance == 1:
                    picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w1_r_f.png"
                else:
                    picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w2_r_f.png"
                self.set_image(picture_behavior)
                move_status = True
            elif arrow_key[pg.K_RIGHT] and not list_ghost_status[1]:
                picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w1_r_f.png"
                self.set_image(picture_behavior)
            elif arrow_key[pg.K_DOWN] and list_ghost_status[2]:
                mc_gyver_move_y = 50
                mc_gyver_move_x = 0
                self.rect.x += mc_gyver_move_x
                self.rect.y += mc_gyver_move_y
                chance = rd.randrange(1, 3)
                if chance == 1:
                    picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w1_b_f.png"
                else:
                    picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w2_b_f.png"
                self.set_image(picture_behavior)
                move_status = True
            elif arrow_key[pg.K_DOWN] and not list_ghost_status[2]:
                picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w1_b_f.png"
                self.set_image(picture_behavior)
            elif arrow_key[pg.K_LEFT] and list_ghost_status[3]:
                mc_gyver_move_x = -50
                mc_gyver_move_y = 0
                self.rect.x += mc_gyver_move_x
                self.rect.y += mc_gyver_move_y
                chance = rd.randrange(1, 3)
                if chance == 1:
                    picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w1_l_f.png"
                else:
                    picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w2_l_f.png"
                self.set_image(picture_behavior)
                move_status = True
            elif arrow_key[pg.K_LEFT] and not list_ghost_status[3]:
                picture_behavior = "./Package/Pictures/Above_MacGyver/a_mg_w1_l_f.png"
                self.set_image(picture_behavior)
            else:
                pass
        return move_status

    def standstill_avatar(self, event):
        """

        :param event:
        :return:
        """
        if event.type == 3 and event.key == 273:
            last_event = event
            lg.info("dernier appui = ", last_event)
            self.set_image("./Package/Pictures/Above_MacGyver/a_mg_s_t_f.png")
        if event.type == 3 and event.key == 275:
            last_event = event
            lg.info("dernier appui = ", last_event)
            self.set_image("./Package/Pictures/Above_MacGyver/a_mg_s_r_f.png")
        if event.type == 3 and event.key == 274:
            last_event = event
            lg.info("dernier appui = ", last_event)
            self.set_image("./Package/Pictures/Above_MacGyver/a_mg_s_b_f.png")
        if event.type == 3 and event.key == 276:
            last_event = event
            lg.info("dernier appui = ", last_event)
            self.set_image("./Package/Pictures/Above_MacGyver/a_mg_s_l_f.png")

    def be_collided(self, list_objects):
        """

        :param list_objects:
        :return:
        """
        for index, sprite_object in enumerate(list_objects):
            if pg.sprite.collide_rect(self, sprite_object):
                Obj.ObjectSprite.list_status_objects[index] = True
        total = Obj.ObjectSprite.list_status_objects.count(True)
        list_status = Obj.ObjectSprite.list_status_objects
        print("\nTOTAL picked objects = {}\nNeedle = {}\nTube = {}\nEther = {}\n"
              .format(total, list_status[0], list_status[1], list_status[2]))
        return Obj.ObjectSprite.list_status_objects

    def prepared_objects_for(self, sprite_boss):
        """

        :param sprite_boss:
        :return:
        """
        end_game_status = False
        success_status = False
        list_endgame = []
        if Obj.ObjectSprite.total_objects():
            CharactersSprite.set_image(sprite_boss, "./Package/Pictures/Above_Watchman/a_w_ss2_f.png")
            print("Catch the WatchMan !!! Man !!!")
            if pg.sprite.collide_rect(self, sprite_boss):
                CharactersSprite.set_position(sprite_boss, 750, 0)
                CharactersSprite.set_image(sprite_boss, "./Package/Pictures/Above_Watchman/a_w_ss3_f.png")
                print("GOTCHA !!! YOU WIN")
                end_game_status = True
                success_status = True
        else:
            print("Collect the Objects !!!")
            end_game_status = False
            if pg.sprite.collide_rect(self, sprite_boss):
                CharactersSprite.set_position(sprite_boss, 750, 0)
                CharactersSprite.set_image(sprite_boss, "./Package/Pictures/Above_Watchman/a_w_ss4_f.png")
                CharactersSprite.set_image(self, "./Package/Pictures/Above_Watchman/a_w_ss3_f.png")
                print("HE GOT U !!! YOU LOSE !!!")
                end_game_status = True
                success_status = False
        list_endgame.append(end_game_status)
        list_endgame.append(success_status)
        return list_endgame


def set_in_maze(maze, mc_gyver, watchman):
    """

    :param mc_gyver:
    :param watchman:
    :return:
    """
    x = 0
    y = 0
    matrix_content = open_file("./Package/good_matrix_pattern_with_characters.txt")
    matrix = "".join(matrix_content)
    matrix = matrix.replace("\n", "")
    while (y and x) < maze.window_size:
        for element in matrix:
            if x == maze.window_size:
                x = 0
                y += 50
            if element == "M":
                mc_gyver.set_position(x, y)
            elif element == "W":
                watchman.set_position(x, y)
            else:
                pass
            x += 50
        break
    return True


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
