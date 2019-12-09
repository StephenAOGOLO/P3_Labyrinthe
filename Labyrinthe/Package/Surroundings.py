import pygame as pg


class SurroundingsElement:
    """
    Building in progress...
    """
    def __init__(self, name, file_png, posx, posy):
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

    def load_element_picture(self):
        """

        :return:
        """
        picture_element = pg.image.load(self.picture)
        return picture_element

    def set_element(self, element, window):
        """

        :param element:
        :param window:
        :return:
        """
        element_set = window.blit(element, (self.posx, self.posy))
        return element_set

    def initialize_landscape(self, element, surface, window):
        """

        :param element:
        :param surface:
        :param window:
        :return:
        """
        for y in range(10, window.height - 10, 21):
            for x in range(10, window.width - 10, 20):
                landscape = surface.blit(element, (x, y))
                # print("x = {}\ny = {}\n".format(x, y))
        return landscape


class SurroundigsSprite(pg.sprite.Sprite):
    def __init__(self, color=(0, 0, 0), width=50, height=50):
        super(SurroundigsSprite, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, filename=None):
        if filename is not None:
            self.image = pg.image.load(filename)
            self.rect = self.image.get_rect()


if __name__ == "__main__":
    import Labyrinthe.Package.Window as Wd
    window = Wd.Window(600, 600)
    window = window.display_window()
    window.fill((255, 255, 255))
    clock = pg.time.Clock()
    fps = 60
    sprites_group = pg.sprite.Group()
    sprites_landscape = pg.sprite.Group()
    wall = SurroundigsSprite((192, 192, 192))
    wall.set_image("./Pictures/brown_block.png")
    first_sprite = SurroundigsSprite()
    second_sprite = SurroundigsSprite((0, 0, 128))
    first_sprite.set_position(50, 50)
    second_sprite.set_position(75, 75)
    wall.set_position(210, 210)
    sprites_group.add(first_sprite, second_sprite, wall)
    sprites_group.draw(window)
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        clock.tick(fps)
        pg.display.update()
    pg.quit()
