"""
Welcome to the characters module, 'characters.py'.
This module is mainly composed of 'CharactersSprite'.
Eighteen methods are defined to handle the game characters through the process.
five functions are defined to control characters data's and effects .
"""
# -*- coding: utf-8 -*-
import random as rd
import logging as lg
import pygame as pg
from Package import objects as obj
lg.basicConfig(level=lg.WARNING)


class CharactersSprite(pg.sprite.Sprite):
    """
    hello
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

    def set_position(self, set_x, set_y):
        """

        :param set_x:
        :param set_y:
        :return:
        """
        self.rect.x = set_x
        self.rect.y = set_y

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
        lg.info("event --> %s", event)
        move_status = False
        picture_behavior = "./Pictures/mg/a_mg_s_t_f.png"
        self.last_x = self.rect.x
        self.last_y = self.rect.y
        arrow_key = pg.key.get_pressed()
        if event.type == pg.KEYUP:
            self.set_image(picture_behavior)
        if event.type == pg.KEYDOWN:
            if arrow_key[pg.K_UP]:
                move_status = self.go_up(list_ghost_status, move_status)
            elif arrow_key[pg.K_RIGHT]:
                move_status = self.go_right(list_ghost_status, move_status)
            elif arrow_key[pg.K_DOWN]:
                move_status = self.go_down(list_ghost_status, move_status)
            elif arrow_key[pg.K_LEFT]:
                move_status = self.go_left(list_ghost_status, move_status)
            else:
                pass
        return move_status

    def go_up(self, ghost_status, move_status):
        """

        :param ghost_status:
        :param move_status:
        :return:
        """
        if ghost_status[0]:
            mc_gyver_move_y = -50
            mc_gyver_move_x = 0
            self.rect.x += mc_gyver_move_x
            self.rect.y += mc_gyver_move_y
            chance = rd.randrange(1, 3)
            if chance == 1:
                picture_behavior = "./Pictures/mg/a_mg_w1_t_f.png"
            else:
                picture_behavior = "./Pictures/mg/a_mg_w2_t_f.png"
            self.set_image(picture_behavior)
            move_status = True
        else:
            picture_behavior = "./Pictures/mg/a_mg_w1_t_f.png"
            self.set_image(picture_behavior)
        return move_status

    def go_right(self, ghost_status, move_status):
        """

        :param ghost_status:
        :param move_status:
        :return:
        """
        if ghost_status[1]:
            mc_gyver_move_x = 50
            mc_gyver_move_y = 0
            self.rect.x += mc_gyver_move_x
            self.rect.y += mc_gyver_move_y
            chance = rd.randrange(1, 3)
            if chance == 1:
                picture_behavior = "./Pictures/mg/a_mg_w1_r_f.png"
            else:
                picture_behavior = "./Pictures/mg/a_mg_w2_r_f.png"
            self.set_image(picture_behavior)
            move_status = True
        else:
            picture_behavior = "./Pictures/mg/a_mg_w1_r_f.png"
            self.set_image(picture_behavior)
        return move_status

    def go_down(self, ghost_status, move_status):
        """

        :param ghost_status:
        :param move_status:
        :return:
        """
        if ghost_status[2]:
            mc_gyver_move_y = 50
            mc_gyver_move_x = 0
            self.rect.x += mc_gyver_move_x
            self.rect.y += mc_gyver_move_y
            chance = rd.randrange(1, 3)
            if chance == 1:
                picture_behavior = "./Pictures/mg/a_mg_w1_b_f.png"
            else:
                picture_behavior = "./Pictures/mg/a_mg_w2_b_f.png"
            self.set_image(picture_behavior)
            move_status = True
        else:
            picture_behavior = "./Pictures/mg/a_mg_w1_b_f.png"
            self.set_image(picture_behavior)
        return move_status

    def go_left(self, ghost_status, move_status):
        """

        :param ghost_status:
        :param move_status:
        :return:
        """
        if ghost_status[3]:
            mc_gyver_move_x = -50
            mc_gyver_move_y = 0
            self.rect.x += mc_gyver_move_x
            self.rect.y += mc_gyver_move_y
            chance = rd.randrange(1, 3)
            if chance == 1:
                picture_behavior = "./Pictures/mg/a_mg_w1_l_f.png"
            else:
                picture_behavior = "./Pictures/mg/a_mg_w2_l_f.png"
            self.set_image(picture_behavior)
            move_status = True
        else:
            picture_behavior = "./Pictures/mg/a_mg_w1_l_f.png"
            self.set_image(picture_behavior)
        return move_status

    def standstill_avatar(self, event):
        """

        :param event:
        :return:
        """
        if event.type == 3 and event.key == 273:
            last_event = event
            lg.info("dernier appui = %s", last_event)
            self.set_image("./Pictures/mg/a_mg_s_t_f.png")
        if event.type == 3 and event.key == 275:
            last_event = event
            lg.info("dernier appui = %s", last_event)
            self.set_image("./Pictures/mg/a_mg_s_r_f.png")
        if event.type == 3 and event.key == 274:
            last_event = event
            lg.info("dernier appui = %s", last_event)
            self.set_image("./Pictures/mg/a_mg_s_b_f.png")
        if event.type == 3 and event.key == 276:
            last_event = event
            lg.info("dernier appui = %s", last_event)
            self.set_image("./Pictures/mg/a_mg_s_l_f.png")

    def be_collided(self, list_objects):
        """

        :param list_objects:
        :return:
        """
        for index, sprite_object in enumerate(list_objects):
            if pg.sprite.collide_rect(self, sprite_object):
                obj.ObjectSprite.list_status_objects[index] = True
        total = obj.ObjectSprite.list_status_objects.count(True)
        list_status = obj.ObjectSprite.list_status_objects
        print("\nTOTAL picked objects = {}\nNeedle = {}\nTube = {}\nEther = {}\n"
              .format(total, list_status[0], list_status[1], list_status[2]))
        return obj.ObjectSprite.list_status_objects

    def prepared_objects_for(self, sprite_boss):
        """

        :param sprite_boss:
        :return:
        """
        end_game_status = False
        success_status = False
        list_endgame = []
        if obj.ObjectSprite.total_objects():
            CharactersSprite.set_image(sprite_boss, "./Pictures/wm/a_w_ss2_f.png")
            print("Catch the WatchMan !!! Man !!!")
            if pg.sprite.collide_rect(self, sprite_boss):
                CharactersSprite.set_position(sprite_boss, 750, 0)
                CharactersSprite.set_image(sprite_boss, "./Pictures/wm/a_w_ss3_f.png")
                print("GOTCHA !!! YOU WIN")
                end_game_status = True
                success_status = True
        else:
            print("Collect the Objects !!!")
            end_game_status = False
            if pg.sprite.collide_rect(self, sprite_boss):
                CharactersSprite.set_position(sprite_boss, 750, 0)
                CharactersSprite.set_image(sprite_boss, "./Pictures/wm/a_w_ss4_f.png")
                CharactersSprite.set_image(self, "./Pictures/wm/a_w_ss3_f.png")
                print("HE GOT U !!! YOU LOSE !!!")
                end_game_status = True
                success_status = False
        list_endgame.append(end_game_status)
        list_endgame.append(success_status)
        return list_endgame

    def get_move_state(self, list_ghost_status, event):
        """

        :param player_sprite:
        :param list_ghost_status:
        :param event:
        :return:
        """
        dict_state = {"last_position": [self.rect.x, self.rect.y],
                      "move_state": self.start_move_avatar(event, list_ghost_status)}
        self.standstill_avatar(event)
        return dict_state

    def set_ghost_sprite(self):
        """
        Create ghosts sprite around the referenced sprite.
        Add all the ghosts sprite and the group into the list to return.
        :return:
        """
        list_ghost = []
        top_ghost = CharactersSprite()
        bottom_ghost = CharactersSprite()
        left_ghost = CharactersSprite()
        right_ghost = CharactersSprite()
        top_ghost.set_position(self.rect.x, self.rect.y - 50)
        bottom_ghost.set_position(self.rect.x, self.rect.y + 50)
        left_ghost.set_position(self.rect.x - 50, self.rect.y)
        right_ghost.set_position(self.rect.x + 50, self.rect.y)
        ghost_group = pg.sprite.Group()
        ghost_group.add(top_ghost, bottom_ghost, right_ghost, left_ghost)
        list_ghost.append(top_ghost)
        list_ghost.append(bottom_ghost)
        list_ghost.append(right_ghost)
        list_ghost.append(left_ghost)
        list_ghost.append(ghost_group)
        return list_ghost

    def reset_ghost_sprite(self, list_ghost):
        """

        :param list_ghost:
        :return:
        """
        new_list = []
        top_ghost = list_ghost[0]
        bottom_ghost = list_ghost[1]
        right_ghost = list_ghost[2]
        left_ghost = list_ghost[3]
        ghost_group = list_ghost[4]
        top_ghost.set_position(self.rect.x, self.rect.y - 50)
        bottom_ghost.set_position(self.rect.x, self.rect.y + 50)
        left_ghost.set_position(self.rect.x - 50, self.rect.y)
        right_ghost.set_position(self.rect.x + 50, self.rect.y)
        pg.sprite.Group.update(ghost_group)
        new_list.append(top_ghost)
        new_list.append(right_ghost)
        new_list.append(bottom_ghost)
        new_list.append(left_ghost)
        return new_list

    def attitude(self, dict_state, boss_sprite, sprite_char_group, list_objects):
        """

        :param dict_state:
        :param boss_sprite:
        :param sprite_char_group:
        :param list_objects:
        :return:
        """
        track_sprite = remove_track(dict_state["move_state"], dict_state["last_position"])
        self.be_collided(list_objects)
        sprite_char_group.add(track_sprite)
        list_end_game_status = self.prepared_objects_for(boss_sprite)
        return list_end_game_status

    def browsing_maze(self, sprite_group, sprite_name="sprite"):
        """

        :param sprite:
        :param sprite_group:
        :param sprite_name:
        :return:
        """
        blocks_hit_list = pg.sprite.spritecollide(self, sprite_group, False)
        lg.info("*\nEvent of the sprite : %s\n*", sprite_name)
        for index, block in enumerate(blocks_hit_list):
            lg.info(index, block)
            if block:
                return False
            return True
        lg.info("***")
        lg.info("*" * 100)
        return True

    def needed_groups_for(self, watchman_sprite):
        """

        :return:
        """
        list_group = []
        for group in range(0, 3):
            group = pg.sprite.Group()
            list_group.append(group)
        watchman_sprite.add_to_group(list_group[0])
        self.add_to_group(list_group[1])
        watchman_sprite.add_to_group(list_group[2])
        return list_group


def set_in_maze(maze, mc_gyver, watchman):
    """

    :param maze:
    :param mc_gyver:
    :param watchman:
    :return:
    """
    a_x = 0
    a_y = 0
    matrix_content = open_file("./Package/good_matrix_pattern_with_characters.txt")
    matrix = "".join(matrix_content)
    matrix = matrix.replace("\n", "")
    while (a_y and a_x) < maze.window_size:
        for element in matrix:
            if a_x == maze.window_size:
                a_x = 0
                a_y += 50
            if element == "M":
                mc_gyver.set_position(a_x, a_y)
            elif element == "W":
                watchman.set_position(a_x, a_y)
            else:
                pass
            a_x += 50
        break
    return True


def remove_track(move_status, last_position):
    """

    :param move_status:
    :param last_position:
    :return:
    """
    track_sprite = CharactersSprite()
    if move_status:
        track_sprite.set_position(last_position[0], last_position[1])
        track_sprite.set_image("./Pictures/w/pyramid_sample.png")
        lg.info("MOVEMENT !!!!!!")
        return track_sprite
    return track_sprite


def handle_collision(list_ghost, walls_group):
    """

    :param list_ghost:
    :param walls_group:
    :return:
    """
    list_ghost_status = []
    list_ghost_name = ["top_ghost", "right_ghost", "bottom_ghost", "left_ghost"]
    for index, ghost in enumerate(list_ghost):
        collision_status = ghost.browsing_maze(walls_group, list_ghost_name[index])
        list_ghost_status.append(collision_status)
    return list_ghost_status


def draw_characters(sprite_char_group, mc_gyver_group, watchman_group, window_displayed):
    """

    :param sprite_char_group:
    :param mc_gyver_group:
    :param watchman_group:
    :param window_displayed:
    :return:
    """
    sprite_char_group.draw(window_displayed)
    mc_gyver_group.draw(window_displayed)
    watchman_group.draw(window_displayed)
    obj.update_dashboard(window_displayed)
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
