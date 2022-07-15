import arcade
from matplotlib.pyplot import title
#from pyray import set_window_icon #
from constants import *
from game.directing.director import Director
from pyglet.image import load as pyglet_load

def main():
    """
    This will initiate the game
    """
    # Creates the game and starts it going
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, title = "Attack the Death Star")
    window.set_icon(pyglet_load("assets/images/favicon.ico"))
    # "assets/images/favicon.ico"
   
    #assets/images/favicon.ico
    director = Director(window)
    director.start_game()

if __name__ == "__main__":
    main() 