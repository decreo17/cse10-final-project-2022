import arcade
from matplotlib.pyplot import title
from constants import *
from game.directing.director import Director

def main():
    """
    This will initiate the game
    """
    # Creates the game and starts it going
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, title = "Attack the Death Star")
    director = Director(window)
    director.start_game()

if __name__ == "__main__":
    main() 