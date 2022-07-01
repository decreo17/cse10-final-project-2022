from asteroids import FlyingObject
from constants import *
import arcade
from game.casting.flyingObject import FlyingObject

class Ship1(FlyingObject):
    """
    This will have the ship functions and basic attributes
    """
    def __init__(self):
        super().__init__()
        self.angle = 0.00
        self.radius = SHIP_RADIUS
        self.center.x = CENTER_X
        self.center.y = CENTER_Y
        self.life = MAXIMUM_LIVES


    def draw(self):
        self.img = SHIP_1_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height  
        super().draw() 
    
    def advance(self):
        super().advance()
        #this will make the help looks blinking when hit by the asteroid, collission will set the alpha to 1
        if self.alpha <= 5:
            self.alpha += 1
            if self.alpha >= 5:
                self.alpha = 255