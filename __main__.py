import arcade
from constants import *
from game.directing.director import Director

def main():
    """
    This will initiate the game
    """
    # Creates the game and starts it going
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    director = Director(window)
    director.start_game()

if __name__ == "__main__":
    main() 