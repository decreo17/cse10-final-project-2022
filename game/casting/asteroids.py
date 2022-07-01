from game.casting.flyingObject import FlyingObject
from abc import ABC, abstractmethod

class Asteroids(FlyingObject, ABC):
    def __init__(self):
        """
        Base class for asteroids
        """
        super().__init__()
        self.rotation = 0.00 #spin
        self.penalty = 0 #this will be added to the score when the asteroid hit the ship

    def advance(self):
        """
        This will help in the movement of the object
        """
        self.angle += self.rotation #spin
        self.center.x += self.velocity.dx #initial position += new possition
        self.center.y += self.velocity.dy #initial position += new possition    
    
    @abstractmethod
    def hit(self):
        """
        
        """
        return

    def bounce_horizontal(self):
        """
        The asteroid will bounce when they hit each other
        """
        self.velocity.dx *= -1 #inverse the movement of the ball
        

    def bounce_vertical(self):
        """
        The asteroid will bounce when they hit each other
        """
        self.velocity.dy *= -1 #inverse the movement of the ball
        