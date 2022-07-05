import math
import arcade
from constants import *

class Ship1Keys:
    """
    This will handle the ship keys
    """
    def __init__(self, ship, held_keys):
        self.ship = ship
        self.held_keys = held_keys

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle += SHIP_TURN_AMOUNT

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle -= SHIP_TURN_AMOUNT

        if arcade.key.UP in self.held_keys:
            #move the ship
            self.ship.velocity.dx += math.cos(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy += math.sin(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT

            #limit the speed of the ship
            if self.ship.velocity.dx > 10:
                self.ship.velocity.dx = 10
            
            if self.ship.velocity.dx < -10:
                self.ship.velocity.dx = -10
            
            if self.ship.velocity.dy > 10:
                self.ship.velocity.dy = 10
            
            if self.ship.velocity.dy < -10:
                self.ship.velocity.dy = -10
        
        if arcade.key.DOWN in self.held_keys:
            #move the ship
            self.ship.velocity.dx -= math.cos(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy -= math.sin(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT

            #limit the speed of the ship
            if self.ship.velocity.dx > 10:
                self.ship.velocity.dx = 10
            
            if self.ship.velocity.dx < -10:
                self.ship.velocity.dx = -10
            
            if self.ship.velocity.dy > 10:
                self.ship.velocity.dy = 10
            
            if self.ship.velocity.dy < -10:
                self.ship.velocity.dy = -10

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass

    
