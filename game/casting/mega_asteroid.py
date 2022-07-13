from constants import *
import arcade
from game.casting.asteroids import Asteroids
from game.casting.large_asteroids import LargeAsteroids
from game.casting.medium_asteroids import MediumAsteroids
from game.casting.small_asteroids import SmallAsteroids
import random

class MegaAsteroid(Asteroids):
    def __init__(self):
        super().__init__()
        #position
        self.center.x = (SCREEN_WIDTH/2)
        self.center.y = (SCREEN_HEIGHT/2)
       
        #speed
        #self.rotation = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS * 15
        # self.penalty = 10
        self.penalty = 6
        
    def draw(self):
        self.img = BIG_ROCK_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width *5
        self.height = self.texture.height *5
        
       
        self.alpha = 255
        super().draw()


    def hit(self):
        """
        split the asteroid
        """
        #create new asteroid from the current posstion of this asteroid
        particles = [LargeAsteroids(self.center), LargeAsteroids(self.center), LargeAsteroids(self.center), LargeAsteroids(self.center)]#,LargeAsteroids(self.center),LargeAsteroids(self.center)]#,MediumAsteroids(self.center), MediumAsteroids(self.center), SmallAsteroids(self.center)]
        
        #get the speed of this asteroid and pass it to the new asteriods and give them direction + speed + offset position so they don't start in the same spot
        
        particles[0].center.y += 100
        particles[0].velocity.dx = self.velocity.dx
        particles[0].velocity.dy = self.velocity.dy + 1 #go up
        #particles[0].center.y -= 50
      

        particles[1].center.y -= 100
        particles[1].velocity.dx = self.velocity.dx
        particles[1].velocity.dy = self.velocity.dy + 2 * -1 #go down
        #particles[1].center.y += 50
    

        particles[2].center.x += 100
        particles[2].velocity.dx = self.velocity.dx + 1 #to the right
        particles[2].velocity.dy = self.velocity.dy + .5
        #particles[2].center.x -= 50
        
        particles[3].center.x -= 100
        particles[3].velocity.dx = self.velocity.dx  - 1.5 #to the LEFT
        particles[3].velocity.dy = self.velocity.dy + 1 #GO UP
        #particles[3].center.x += 50
        
        # particles[4].velocity.dx = self.velocity.dx - 2 #to the right
        # particles[4].velocity.dy = self.velocity.dy - 1 #GO DOWN
        
        # particles[5].velocity.dx = self.velocity.dx + (random.randint(-2,2)) #to the right
        # particles[5].velocity.dy = self.velocity.dy + (random.randint(-2,2)) #GO DOWN


        return particles