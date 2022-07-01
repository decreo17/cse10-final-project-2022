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


    def draw(self):
        self.img = SHIP_1_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height  
        super().draw()