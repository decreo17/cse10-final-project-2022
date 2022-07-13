from game.directing.game_screens import GameInplay
from constants import *
import arcade

class Director():

    def __init__(self, window):
        self.window = window
    
    def start_game(self):
        # Creates the game and starts it going
        start_view = GameInplay()
        self.window.show_view(start_view)
        arcade.run()
