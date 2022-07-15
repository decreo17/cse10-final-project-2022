from constants import *
import arcade
from game.casting.asteroids import Asteroids
from game.casting.small_asteroids import SmallAsteroids

class MediumAsteroids(Asteroids):
    def __init__(self,asteroid_center):
        super().__init__()
        self.rotation = MEDIUM_ROCK_SPIN
        self.radius = MEDIUM_ROCK_RADIUS
        self.center.x = asteroid_center.x
        self.center.y = asteroid_center.y
        # self.penalty = 6  
        self.penalty = 3
        
    def draw(self):    
        self.img = MEDIUM_ROCK_IAMGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width / 3
        self.height = self.texture.height /3
        self.alpha = 255
        super().draw()

    def hit(self):
        """
        split the asteroid
        """
        #create new asteroid from the current posstion of this asteroid
        particles = [SmallAsteroids(self.center), SmallAsteroids(self.center)]
        
        #get the speed of this asteroid and pass it to the new asteriods and give then direction + speed
        particles[0].center.y += 25
        particles[0].velocity.dx = self.velocity.dx + 1.5
        particles[0].velocity.dy = self.velocity.dy + 1.5
        particles[1].center.y -= 25
        particles[1].velocity.dx = self.velocity.dx + 1.5 * -1
        particles[1].velocity.dy = self.velocity.dy + 1.5 * -1

        return particles