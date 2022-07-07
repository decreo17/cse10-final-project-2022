from constants import *
import arcade
from game.casting.asteroids import Asteroids
from game.casting.medium_asteroids import MediumAsteroids
from game.casting.small_asteroids import SmallAsteroids
import random

class LargeAsteroids(Asteroids):
    def __init__(self):
        super().__init__()
        #position
        self.center.x = random.uniform(0,SCREEN_HEIGHT)
        self.center.y = random.uniform(SCREEN_HEIGHT,SCREEN_WIDTH)
        #speed
        self.velocity.dx = random.uniform(-BIG_ROCK_SPEED,BIG_ROCK_SPEED)
        self.velocity.dy = random.uniform(-BIG_ROCK_SPEED,BIG_ROCK_SPEED)
        self.rotation = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS
        # self.penalty = 10
        self.penalty = 6
        
    def draw(self):
        self.img = BIG_ROCK_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255
        super().draw()


    def hit(self):
        """
        split the asteroid
        """
        #create new asteroid from the current posstion of this asteroid
        particles = [MediumAsteroids(self.center), MediumAsteroids(self.center), SmallAsteroids(self.center)]
        
        #get the speed of this asteroid and pass it to the new asteriods and give them direction + speed
        particles[0].velocity.dx = self.velocity.dx
        particles[0].velocity.dy = self.velocity.dy + 2 #go up

        particles[1].velocity.dx = self.velocity.dx
        particles[1].velocity.dy = self.velocity.dy + 2 * -1 #go down

        particles[2].velocity.dx = self.velocity.dx + 5 #to the right
        particles[2].velocity.dy = self.velocity.dy

        return particles