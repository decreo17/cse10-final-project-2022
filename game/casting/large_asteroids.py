from constants import *
import arcade
from game.casting.asteroids import Asteroids
from game.casting.medium_asteroids import MediumAsteroids
from game.casting.small_asteroids import SmallAsteroids

class LargeAsteroids(Asteroids):
    def __init__(self,asteroid_center):
        super().__init__()
        self.rotation = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS
        self.penalty = 6
        
        self.center.x = asteroid_center.x
        self.center.y = asteroid_center.y
        
        
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
        particles[0].center.y += 50
        particles[0].velocity.dx = self.velocity.dx
        particles[0].velocity.dy = self.velocity.dy + 2 #go up

        particles[1].center.y -= 50
        particles[1].velocity.dx = self.velocity.dx
        particles[1].velocity.dy = self.velocity.dy + 2 * -1 #go down

        particles[2].center.y += 25
        particles[2].velocity.dx = self.velocity.dx + 5 #to the right
        particles[2].velocity.dy = self.velocity.dy

        return particles