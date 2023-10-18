from pico2d import load_image


class Grass:
    def __init__(self, y2):
        self.image = load_image('grass.png')
        self.y = y2

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass
