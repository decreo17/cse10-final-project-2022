# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 
import random
import os
# KEYS

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
#Background
BG_IMAGE = "./assets/background_images/bgu.jpg"
BG_IMAGE1 = "./assets/background_images/retro_background.jpg"
BG_IMAGE2 = "./assets/background_images/wp8368533.jpg"
BG_IMAGE3 = "./assets/background_images/51oGSP+OBnL._AC_.jpg"
BG_IMAGE4 = "./assets/background_images/bg_image4.jpg"

BG_IMAGES = [BG_IMAGE, BG_IMAGE1, BG_IMAGE2, BG_IMAGE3, BG_IMAGE4]

background = random.choice(BG_IMAGES)

#Game Over
GAME_OVER_IMAGE = "./assets/background_images/game_over.png"
WIN_IMAGE = "./assets/background_images/congrats.png"
LEFT_BOARDER = 0
RIGHT_BOARDER = SCREEN_WIDTH

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 5
MAXIMUM_LIVES = DEFAULT_LIVES

# BULLETS
BULLET_RADIUS = 20
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_IMAGE = "./assets/images/laserBlue01.png"



# SHIPS
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 20
SHIP_IMAGE = "./assets/spaceships/playerShip1_orange.png"
SHIP_1_IMAGE = "./assets/spaceships/playerShip1_orange.png"
SHIP_2 = "./assets/images/favpng_starship-enterprise-uss-enterprise-ncc-1701-star-trek_25.png"

# ROCKS
INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 0
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15
BIG_ROCK_IMAGE = "assets/images/asteroid (2).png"

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5
MEDIUM_ROCK_IAMGE = "assets/images/asteroid_medium.png"

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2
SMALL_ROCK_IMAGE = "assets/images/asteroid (1).png"

# DIALOGS
