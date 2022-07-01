from constants import *
from game.casting.flyingObject import FlyingObject
import arcade
import math

class Bullet(FlyingObject):
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.travel = 0
        self.angle = self.angle + 90

    def draw(self):
        self.img = BULLET_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255
        super().draw()
    
    def advance(self):
        super().advance()
        #travel represents the frame, it will die in 60 frames
        self.travel += 1
        if self.travel == BULLET_LIFE:
            self.alive = False

    def fire(self, ship):
        """
        This will give the movement for our bullet and angel for its direction
        """
        #get the position of the ship and angle
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.angle += ship.angle
        #speed and angle of bullet when fired
        self.velocity.dx = math.cos(math.radians(ship.angle - 270)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(ship.angle - 270)) * BULLET_SPEED
        self.velocity.dx += ship.velocity.dx
        self.velocity.dy += ship.velocity.dy  