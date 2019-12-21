import pygame as pg
import random as rd
import Labyrinthe.Package.Surroundings as Sd


class ObjectSprite(pg.sprite.Sprite):

    list_status_objects = [False, False, False]

    @classmethod
    def total_objects(cls):
        total = ObjectSprite.list_status_objects.count(True)
        if total == 3:
            return True
        else:
            return False

    def __init__(self, name, width=50, height=50):
        super(ObjectSprite, self).__init__()
        self.name = name
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.picked_status = False

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, filename=None):
        if filename is not None:
            self.image = pg.image.load(filename)

    def add_picked_object(self):
        if self.opened == 1:
            ObjectSprite.picked_objects = + 1
            return True
        else:
            return False


if __name__ == "__main__":
    import Labyrinthe.Package.Window as Wd
    pg.init()
    pg.display.set_caption("Aidez MacGyver à s'échapper !")
    window = Wd.Window(770, 770)
    window_displayed = window.display_window()
    clock = pg.time.Clock()
    fps = 60
    walls_group = pg.sprite.Group()
    list_bool = [True, False]
    y = 0
    x = 0
    end_window = 750
    window.set_background_on(window_displayed, 0, 0)
    while (y and x) < end_window:
        for element in Sd.matrix_maze:
            if x == end_window:
                x = 0
                y += 50
            if element:
                wall = Sd.SurroundigsSprite()
                wall.set_position(x, y)
                wall.set_image("./Pictures/Wall/big_brown_block.png")
                walls_group.add(wall)
                walls_group.draw(window_displayed)
            else:
                pass
            x += 50
    print(walls_group.sprites())
    print(len(walls_group))
    launched = True
    while launched:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                launched = False
        clock.tick(fps)
        pg.display.update()
    pg.quit()