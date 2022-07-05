import arcade
from abc import ABC, abstractmethod
from game.shared.point import Point
from game.shared.velocity import Velocity
import constants

class FlyingObject(ABC):
    """
    This will be the base class for flying objects
    """
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True #check if the object is still alive
        self.radius = 0.0
        self.angle = 0 #facing 

        self.img = constants.BG_IMAGE
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 0
    
    @abstractmethod
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, 
                self.height, self.texture, self.angle, self.alpha) 
  
    def advance(self):

        """
        This will help in the movement of the object
        """
        self.center.x += self.velocity.dx #initial position += new possition
        self.center.y += self.velocity.dy #initial position += new possition
    
    def is_off_screen(self,width,height):
        """
        This will check if the object is off screen, sample, if an object goes off the right edge of the screen, 
        it should appear on the left edge.
        """        
        if self.center.x > width:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = width
        elif self.center.y > height:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = height