import arcade
import math
from constants import *
from game.casting.large_asteroids import LargeAsteroids
from game.casting.mega_asteroid import MegaAsteroid
from game.casting.ship import Ship
from game.casting.ship_1 import Ship1
from game.casting.bullet import Bullet
from game.services.ship_keys import ShipKeys
from game.services.ship1_keys import Ship1Keys
from game.shared.bounce import Bounce

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

        # declare anything here you need the game class to track
        self.ship = Ship()
        self.ship1 = Ship1()
        self.score = 0
        self.bullets = []
        self.bullets1 = []
        self.asteroids = []
        self.aliens = []
        self.background = arcade.load_texture(background)
        #create asteroids
        for i in range(1):
            asteroid = MegaAsteroid()
            
            # asteroid = LargeAsteroids()
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

        # draw each object
        #draw bullets
        for bullet in self.bullets:
            bullet.draw()

        for bullet1 in self.bullets1:
            bullet1.draw()        

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

        if self.ship1.alive:
            #draw the ship
            self.ship1.draw()
            #draw the mini ships representing the ship life
            self.draw_ship_life1()

        #if the ship has no more lives it will die
        if self.ship.life <= 0:
            self.ship.alive = False
        
        #if the ship has no more lives it will die
        if self.ship1.life <= 0:
            self.ship1.alive = False

        # Determine if the game is over
        if self.ship.alive == False or self.ship1.alive == False :
            view = GameOver() #create and instance of gameover class
            view.score = self.score #copy the score to the gameoverclass
            view.asteroids = self.asteroids #copy the asteroids to the gameoverclass
            view.ship_lives = self.ship.life
            view.ship1_lives = self.ship1.life
            self.window.show_view(view) #show the gameoverview
  
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        ShipKeys(self.ship, self.held_keys).check_keys()
        Ship1Keys(self.ship1, self.held_keys).check_keys()
        self.check_collisions()

        # Tell everything to advance or move forward one step in time
        self.ship.advance()
        self.ship.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.ship1.advance()
        self.ship1.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
        #move the bullets
        for bullet in self.bullets:
            bullet.advance()
            bullet.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)

        for bullet1 in self.bullets1:
            bullet1.advance()
            bullet1.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)   

        #move the asterois
        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)

        #add score while the ship alive
        if self.ship.alive:   
            self.score += delta_time

        # Check for collisions
    def check_asteroid_to_asteriod_collisions(self):
       #Compare an Asteroid to the rest of the list of asteroids
        
        for i in range (0, len(self.asteroids)):
            
            #this is to aid in the comparision not avoid picking the same asteroid in the first comparison
            for j in range (i+1, len(self.asteroids)):
                
            # Make sure they are both alive before checking for a collision
            #This will make the asteroid bounce when they hit eachother
                if self.asteroids[i].alive and self.asteroids[j].alive:
                    
                    too_close = self.asteroids[i].radius + self.asteroids[j].radius + 20
                    x1 = self.asteroids[i].center.x
                    y1 = self.asteroids[i].center.y
                    x2 = self.asteroids[j].center.x
                    y2 = self.asteroids[j].center.y
                    distance = ((x2 - x1)**2 + (y2 - y1)**2) **.5
                    
                    if distance < (too_close ) :
                        bounce = Bounce(self.asteroids[i],self.asteroids[j])
                        bounce.collide()  
                              
    def check_ship_to_asteriod_collisions(self):
        for asteroid in self.asteroids:
            # Make sure they are both alive before checking for a collision
            if self.ship.alive and asteroid.alive:
                    too_close = self.ship.radius + asteroid.radius

                    if (abs(self.ship.center.x - asteroid.center.x) < too_close and
                                abs(self.ship.center.y - asteroid.center.y) < too_close):
                        
                            asteroid.alive = True
                            self.ship.life -= 1
                            self.ship.alpha = 1
                            #self.asteroids += asteroid.hit() #add the new asteroids to current list
                            arcade.play_sound(self.hit_sound) #play the sound
                            bounce = Bounce(asteroid, self.ship)
                            bounce.collide()
                            
        for asteroid in self.asteroids:
            # Make sure they are both alive before checking for a collision
            if self.ship1.alive and asteroid.alive:
                    too_close = self.ship1.radius + asteroid.radius

                    if (abs(self.ship1.center.x - asteroid.center.x) < too_close and
                                abs(self.ship1.center.y - asteroid.center.y) < too_close):
                        
                            asteroid.alive = True
                            self.ship1.life -= 1
                            self.ship1.alpha = 1
                            #self.asteroids += asteroid.hit() #add the new asteroids to current list
                            arcade.play_sound(self.hit_sound) #play the sound
                            bounce1 = Bounce(asteroid, self.ship1,)
                            bounce1.collide()
                            
    def check_bullet_to_asteriod_collisions(self):
        for bullet in self.bullets:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                abs(bullet.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False #kill the bullet
                        
                        #### lowers down life points and slows the speed of the asteroid 
                        asteroid.life_points -=1
                        if asteroid.velocity.dx >=0:
                            asteroid.velocity.dx -= .2
                    
                        else: 
                            asteroid.velocity.dx +.2
                            
                        if asteroid.velocity.dy >= 0:
                            asteroid.velocity.dy -= .2
                            
                        else:  
                            asteroid.velocity.dy += .2
                        
                        #When the asteroid's life points reach zero...
                        if asteroid.life_points == 0:
                            asteroid.alive = False #kill the asteroid
                            self.asteroids += asteroid.hit() #add the new asteroids to current list
                            arcade.play_sound(self.hit_sound) #play sound
                            
        for bullet1 in self.bullets1:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if bullet1.alive and asteroid.alive:
                    too_close = bullet1.radius + asteroid.radius

                    if (abs(bullet1.center.x - asteroid.center.x) < too_close and
                                abs(bullet1.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet1.alive = False #kill the bullet
                        asteroid.life_points -=1
                        
                        #if the asteroid is hit and is going right...slow it down by making it go left 
                        if asteroid.velocity.dx >=0:
                            asteroid.velocity.dx -= .2
                        
                        else: 
                            asteroid.velocity.dx +.2
                            
                        #if aster is hit and is going up...slow it down and make it go down
                        if asteroid.velocity.dy >= 0:
                            asteroid.velocity.dy -= .2
                            
                        else:  
                            asteroid.velocity.dy += .2
                         
                        if asteroid.life_points == 0:
                            asteroid.alive = False #kill the asteroid
                            self.asteroids += asteroid.hit() #add the new asteroids to current list
                            arcade.play_sound(self.hit_sound) #play sound
                            
    def check_bullet_to_ship_collisions(self):
        for bullet in self.bullets:
            # Make sure they are both alive before checking for a collision
            if self.ship1.alive and bullet.alive:
                    too_close = self.ship1.radius + bullet.radius

                    if (abs(self.ship1.center.x - bullet.center.x) < too_close and
                                abs(self.ship1.center.y - bullet.center.y) < too_close):
                        
                            bullet.alive = False
                            self.ship1.life -= 1
                            self.ship1.alpha = 1
                            arcade.play_sound(self.hit_sound) #play the sound
    
        for bullet1 in self.bullets1:
            # Make sure they are both alive before checking for a collision
            if self.ship.alive and bullet1.alive:
                    too_close = self.ship.radius + bullet1.radius

                    if (abs(self.ship.center.x - bullet1.center.x) < too_close and
                                abs(self.ship.center.y - bullet1.center.y) < too_close):
                        
                            bullet1.alive = False
                            self.ship.life -= 1
                            self.ship.alpha = 1
                            arcade.play_sound(self.hit_sound) #play the sound

    def check_collisions(self):
        """
        Checks to see if bullets have hit asteroids.
        Updates scores and removes dead items.
        :return:
        """
        # on progress this should bounce the asteroid when it hit ship and other asteroid
        
        # ship and asteroid
        self.check_ship_to_asteriod_collisions()
        
        # asteriod to asteriod
        self.check_asteroid_to_asteriod_collisions()
        
        # bullets and asteroid
        self.check_bullet_to_asteriod_collisions()

        # bullet to ship1
        self.check_bullet_to_ship_collisions()
        
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
        
        for bullet1 in self.bullets1:
            if not bullet1.alive:
                self.bullets1.remove(bullet1)

        #clean up asteroids
        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # Fire the bullet here!
                # Fire!
                ship = self.ship

                #get the instance of bullet then align it with the ship's location and angle
                bullet = Bullet()
                bullet.fire(ship)
                #my addtional sound
                arcade.play_sound(self.fire_sound) #playsound
                self.bullets.append(bullet) #add the new bullet to the list
        
        if self.ship1.alive:
            self.held_keys.add(key)

            if key == arcade.key.ENTER:
                # Fire the bullet here!
                # Fire!
                ship1 = self.ship1

                #get the instance of bullet then align it with the ship's location and angle
                bullet1 = Bullet()
                bullet1.fire(ship1)
                #my addtional sound
                arcade.play_sound(self.fire_sound) #playsound
                self.bullets1.append(bullet1) #add the new bullet to the list

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
            #slow down the ship but will still  looks like floating
            self.ship.velocity.dx = math.cos(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy = math.sin(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT
            self.ship1.velocity.dx = math.cos(math.radians(self.ship1.angle + 90)) * SHIP_THRUST_AMOUNT
            self.ship1.velocity.dy = math.sin(math.radians(self.ship1.angle + 90)) * SHIP_THRUST_AMOUNT

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
        x = 25 #position it to the left
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

    def draw_ship_life1(self):
        """
        Draw the mini ships that represent the lives of the ship
        """
        x = SCREEN_WIDTH - 25 #position it to the left
        y = SCREEN_HEIGHT - 30 #position this to the top - 30
        for i in range(self.ship1.life):
            img = SHIP_IMAGE
            texture = arcade.load_texture(img)
            width = texture.width // 4 #reduce the size
            height = texture.height // 4 #reduce the size
            angle = 0 
            alpha = 255
            arcade.draw_texture_rectangle(x, y, width, 
                    height, texture, angle, alpha)
            x -= width #add the new mini ship beside the last ship created        

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
        self.draw_congratulations()
        # arcade.start_render()
        # if len(self.asteroids) > 0:
        #     self.draw_game_over()
        # else:
        #     self.draw_congratulations()

    def on_key_press(self, key: int, modifiers: int):
        """
        If the user presses the space bar, re-start the game.
        """

        if key == arcade.key.SPACE:
            game_view = GameInplay()
            self.window.show_view(game_view)

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
        start_x = CENTER_X
        start_y = CENTER_Y
        play_again_message = 'Hit the "Space Bar" or "click" to play again!'
        
        if self.ship1_lives == 0:
            message = 'PLAYER 1 WINS !!!!!!!!!!'
            lapse = f"Player 2 survived for: {self.score:.2f} seconds... pity"
            arcade.draw_text(message, start_x=start_x, start_y=start_y, font_size= 20, color=arcade.color.WHITE, anchor_x="center")  
            arcade.draw_text(lapse, start_x=start_x, start_y=(start_y - 25), font_size= 20, color=arcade.color.WHITE, anchor_x="center") 
            arcade.draw_text(play_again_message, start_x=start_x, start_y=(start_y - 50), font_size= 20, color=arcade.color.WHITE, anchor_x="center") 
            
        elif self.ship_lives == 0:
            message = 'PLAYER 2 WINS!!!!!!!!'
            lapse = f"Player 1 survived for: {self.score:.2f} seconds... pity"
            arcade.draw_text(message, start_x=start_x, start_y=start_y, font_size= 20, color=arcade.color.WHITE, anchor_x="center")  
            arcade.draw_text(lapse, start_x=start_x, start_y=(start_y - 25), font_size= 20, color=arcade.color.WHITE, anchor_x="center") 
            arcade.draw_text(play_again_message, start_x=start_x, start_y=(start_y - 50), font_size= 20, color=arcade.color.WHITE, anchor_x="center")
             
            
            
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




class StartUpView(arcade.View):
    """ View to show when game starts, showing basic instructions """
    def __init__(self):

        super().__init__()

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        arcade.set_background_color(arcade.color.SMOKY_BLACK)


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()       
        self.draw_game_start_up()


    def on_key_press(self, key: int, modifiers: int):
        """
        If the user presses the space bar, re-start the game.
        """
        if key == arcade.key.SPACE:
            game_view = GameInplay()
            self.window.show_view(game_view)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameInplay()
        self.window.show_view(game_view)


    def draw_game_start_up(self):
        """
        Show the instructions 
        """
        self.background = arcade.load_texture(START_UP_IMAGE)
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)