import pygame as pg

STARTX = 150
STARTY = 200


class Characters:
    """
    Building in progress...
    """

    def __init__(self, name, file_png, posx=STARTX, posy=STARTY):
        """

        :param name:
        :param file_png:
        :param posx:
        :param posy:
        """
        self.name = name
        self.picture = file_png
        self.posx = posx
        self.posy = posy

    def __repr__(self):
        """
        Show the feature of a character
        :return:message
        """
        message = "*****\nType: {}\nCharacter: {}\npath picture: '{}'\nposition x = {}\nposition y = {}\n*****"\
            .format(type(self), self.name, self.picture, self.posx, self.posy)
        return message

    def display_character(self):
        """

        :return:
        """
        avatar = pg.image.load(self.picture)
        return avatar

    def load_character_picture(self):
        """

        :return:
        """
        avatar = pg.image.load(self.picture)
        return avatar

    def set_avatar(self, avatar, window):
        """

        :param avatar:
        :param window:
        :return:
        """
        avatar_set = window.blit(avatar, (self.posx, self.posy))
        return avatar_set

    def start_move_avatar(self, event):
        """

        :param event:
        :return:
        """
        mc_gyver_move_x = 0
        mc_gyver_move_y = 0
        arrow_key = pg.key.get_pressed()
        if event.type == pg.KEYUP:
            pass
        if event.type == pg.KEYDOWN:
            if arrow_key[pg.K_UP]:
                mc_gyver_move_y = -1
                mc_gyver_move_x = 0
            elif arrow_key[pg.K_DOWN]:
                mc_gyver_move_y = 1
                mc_gyver_move_x = 0
            elif arrow_key[pg.K_RIGHT]:
                mc_gyver_move_x = 1
                mc_gyver_move_y = 0
            elif arrow_key[pg.K_LEFT]:
                mc_gyver_move_x = -1
                mc_gyver_move_y = 0
        self.posx += mc_gyver_move_x
        self.posy += mc_gyver_move_y

    def stop_move_avatar(self, event, limit_x, limit_y):
        """

        :return:
        """
        arrow_key = pg.key.get_pressed()
        if event.type == pg.KEYDOWN:
            if arrow_key[pg.K_UP]:
                self.posy = 0
            elif arrow_key[pg.K_DOWN]:
                self.posy = limit_y
            elif arrow_key[pg.K_RIGHT]:
                self.posx = limit_x
            elif arrow_key[pg.K_LEFT]:
                self.posx = 0


class CharactersSprite(pg.sprite.Sprite):
    def __init__(self, color=(0, 0, 0), width=20, height=20):
        super(CharactersSprite, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, filename=None):
        if filename is not None:
            self.image = pg.image.load(filename)
            #self.rect = self.image.get_rect()

    def add_to_group(self, group):
        sprite_group = group.add(self)
        return sprite_group

    def start_move_avatar(self, event):
        """

        :param event:
        :return:
        """
        mc_gyver_move_x = 0
        mc_gyver_move_y = 0
        arrow_key = pg.key.get_pressed()
        if event.type == pg.KEYUP:
            pass
        if event.type == pg.KEYDOWN:
            if arrow_key[pg.K_UP]:
                pg.key.set_repeat(1)
                mc_gyver_move_y = -50
                mc_gyver_move_x = 0
            elif arrow_key[pg.K_DOWN]:
                pg.key.set_repeat(1)
                mc_gyver_move_y = 50
                mc_gyver_move_x = 0
            elif arrow_key[pg.K_RIGHT]:
                pg.key.set_repeat(1)
                mc_gyver_move_x = 50
                mc_gyver_move_y = 0
            elif arrow_key[pg.K_LEFT]:
                pg.key.set_repeat(1)
                mc_gyver_move_x = -50
                mc_gyver_move_y = 0
            else:
                pass
        self.rect.x += mc_gyver_move_x
        self.rect.y += mc_gyver_move_y

    def stop_move_avatar(self, event, limit_x, limit_y):
        """

        :return:
        """
        arrow_key = pg.key.get_pressed()
        if event.type == pg.KEYDOWN:
            if arrow_key[pg.K_UP]:
                self.rect.y = 0
            elif arrow_key[pg.K_DOWN]:
                self.rect.y = limit_y
            elif arrow_key[pg.K_RIGHT]:
                self.rect.x = limit_x
            elif arrow_key[pg.K_LEFT]:
                self.rect.x = 0


if __name__ == "__main__":
    import Labyrinthe.Package.Window as Wd
    pg.init()
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
    window_width = 640
    window_height = 480
    window = Wd.Window(window_width, window_height)
    window = window.display_window()
    window.fill((255, 255, 255))
    clock = pg.time.Clock()
    fps = 60
    sprite_char_group = pg.sprite.Group()
    mc_gyver_sprite = CharactersSprite()
    mc_gyver_sprite.set_position(1, 1)
    mc_gyver_sprite.set_image("./Pictures/brown_block.png")
    sprite_char_group.add(mc_gyver_sprite)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        Wd.color_window(window)
        sprite_char_group.draw(window)
        clock.tick(fps)
        pg.display.update()
    pg.quit()
