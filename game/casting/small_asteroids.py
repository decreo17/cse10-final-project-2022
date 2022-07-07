from constants import *
import arcade
from game.casting.asteroids import Asteroids

class SmallAsteroids(Asteroids):
    def __init__(self,asteroid_center):
        super().__init__()
        self.rotation = SMALL_ROCK_SPIN
        self.radius = SMALL_ROCK_RADIUS
        self.center.x = asteroid_center.x
        self.center.y = asteroid_center.y
        # self.penalty = 3
        self.penalty = 1
  
    def draw(self):
        self.img = SMALL_ROCK_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255
        super().draw()

    def hit(self):
        """
        split the asteroid
        """
        #no new asteroid will be created
        particles = []
        return particles