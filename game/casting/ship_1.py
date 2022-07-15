from constants import *
import arcade
from game.casting.ship import Ship

class Ship1(Ship):
    """
    This will be the player 2
    This will have the ship functions and basic attributes
    """
    def __init__(self):
        super().__init__()
        self.center.x = RIGHT_BOARDER - SHIP_RADIUS

    def draw(self):
        self.img = SHIP_2_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width /3
        self.height = self.texture.height  /3
        super().draw()