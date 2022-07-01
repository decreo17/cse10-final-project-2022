import arcade
import math
from constants import *
from game.casting.large_asteroids import LargeAsteroids
from game.casting.ship import Ship
from game.casting.bullet import Bullet

class GameInplay(arcade.View):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    def __init__(self):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__()
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.ship = Ship()
        self.score = 0
        self.bullets = []
        self.asteroids = []
        self.background = arcade.load_texture(BG_IMAGE)
        #create asteroids
        for i in range(5):
            asteroid = LargeAsteroids()
            self.asteroids.append(asteroid)        

        # my add on: Load sounds. Sounds from kenney.nl
        self.fire_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav") 
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion1.wav")
        
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # TODO: draw each object
        #draw bullets
        for bullet in self.bullets:
            bullet.draw()        

        #draw asteroids
        for asteroid in self.asteroids:
            asteroid.draw()
       
        #do this when ship is alive
        if self.ship.alive:
            #draw the ship
            self.ship.draw()
            #draw the score
            self.draw_score()
            #draw the mini ships representing the ship life
            self.draw_ship_life()

        #if the ship has no more lives it will die
        if self.ship.life <= 0:
            self.ship.alive = False

        #if all the asteroids were cleared show congratulations if the ship died show game over
        if len(self.asteroids) == 0 or self.ship.alive == False:
            view = GameOver() #create and instance of gameover class
            view.score = self.score #copy the score to the gameoverclass
            view.asteroids = self.asteroids #copy the asteroids to the gameoverclass
            self.window.show_view(view) #show the gameoverview
            self.ship.alive = False #hide the ship
  
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collisions()

        # TODO: Tell everything to advance or move forward one step in time
        self.ship.advance()
        self.ship.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
        #move the bullets
        for bullet in self.bullets:
            bullet.advance()
            bullet.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)   

        #move the asterois
        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)

        #add score while the ship alive
        if self.ship.alive:   
            self.score += delta_time

        # TODO: Check for collisions
    def check_collisions(self):
        """
        Checks to see if bullets have hit asteroids.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your asteroids list "asteroids"
        #on progress this should bounce the asteroid when it hit ship and other asteroid
        #ship and asteroid
        for asteroid in self.asteroids:

            # Make sure they are both alive before checking for a collision
            if self.ship.alive and asteroid.alive:
                    too_close = self.ship.radius + asteroid.radius

                    if (abs(self.ship.center.x - asteroid.center.x) < too_close and
                                abs(self.ship.center.y - asteroid.center.y) < too_close):
                        
                            asteroid.alive = False
                            self.ship.life -= 1
                            self.ship.alpha = 1
                            self.score += asteroid.penalty #add the penalty score
                            self.asteroids += asteroid.hit() #add the new asteroids to current list
                            arcade.play_sound(self.hit_sound) #play the sound
                            
        #asteroid to asteroid
        for asteroid1 in self.asteroids:
            for asteroid in self.asteroids:
            # Make sure they are both alive before checking for a collision
            #This will make the asteroid bounce when they hit eachother
                if asteroid1.alive and asteroid.alive:
                        too_close = asteroid1.radius + asteroid.radius

                        if (abs(asteroid1.center.x - asteroid.center.x) < too_close and
                                    abs(asteroid1.center.y - asteroid.center.y) < too_close):        
                    
                            if asteroid.center.x > asteroid1.center.x and asteroid.velocity.dx > asteroid1.velocity.dx:
                                asteroid.bounce_horizontal()
                            
                            if asteroid.center.x < asteroid1.center.x and asteroid.velocity.dx < asteroid1.velocity.dx:
                                asteroid.bounce_horizontal()
                            
                            if asteroid.center.y > asteroid1.center.y and asteroid.velocity.dy > asteroid1.velocity.dy:
                                asteroid.bounce_horizontal()
                            
                            if asteroid.center.y < asteroid1.center.y and asteroid.velocity.dy < asteroid1.velocity.dy:
                                asteroid.bounce_horizontal()
    
        #bullets and asteroid
        for bullet in self.bullets:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                abs(bullet.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False #kill the bullet
                        asteroid.alive = False #kill the asteroid
                        self.asteroids += asteroid.hit() #add the new asteroids to current list
                        arcade.play_sound(self.hit_sound) #play sound

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or asteroids from the list.
        :return:
        """
        #clean up bullets
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        #clean up asteroids
        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

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

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                # Fire!
                ship = self.ship

                #get the instance of bullet then align it with the ship's location and angle
                bullet = Bullet()
                bullet.fire(ship)
                #my addtional sound
                arcade.play_sound(self.fire_sound) #playsound
                self.bullets.append(bullet) #add the new bullet to the list

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
            #slow down the ship but will still  looks like floating
            self.ship.velocity.dx = math.cos(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy = math.sin(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = f"Time Lapse: {self.score}"
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.WHITE_SMOKE)

    def draw_ship_life(self):
        """
        Draw the mini ships that represent the lives of the ship
        """
        x = 10 #position it to the left
        y = SCREEN_HEIGHT - 30 #position this to the top - 30
        for i in range(self.ship.life):
            img = SHIP_IMAGE
            texture = arcade.load_texture(img)
            width = texture.width // 4 #reduce the size
            height = texture.height // 4 #reduce the size
            angle = 0 
            alpha = 255
            arcade.draw_texture_rectangle(x, y, width, 
                    height, texture, angle, alpha)
            x += width #add the new mini ship beside the last ship created

class GameOver(arcade.View):
    """ View to show when game is over """
    def __init__(self):

        super().__init__()

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.asteroids = []

        self.score = 0.00
        
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        if len(self.asteroids) > 0:
            self.draw_game_over()
        else:
            self.draw_congratulations()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameInplay()
        self.window.show_view(game_view)

    def draw_congratulations(self):
        """
        Print the message "Congratulations" and show the score(time lapse) 
        """
        self.background = arcade.load_texture(WIN_IMAGE)
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        lapse = f"Time Lapse: {self.score:.2f}"
        start_x = CENTER_X
        start_y = CENTER_Y
        arcade.draw_text(lapse, start_x=start_x, start_y=start_y, font_size= 20, color=arcade.color.WHITE, anchor_x="center")  
        
    def draw_game_over(self):
        """
        Print the message "Game over" and show the score(time lapse) 
        """
        self.background = arcade.load_texture(GAME_OVER_IMAGE)
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        lapse = f"Time Lapse: {self.score:.2f}"
        start_x = CENTER_X
        start_y = CENTER_Y
        arcade.draw_text(lapse, start_x=start_x, start_y=start_y, font_size= 20, color=arcade.color.WHITE, anchor_x="center")