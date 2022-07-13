class Bounce:
    """
        This will bounce the given objects
    """

    def __init__(self, object_1, object_2):
        self.object_1 = object_1
        self.object_2 = object_2

    def collide(self):
        """
        Bounce the object when they collide
        """
        if self.object_1.radius == self.object_2.radius:
                           
            swap1x = self.object_1.center.x 
            swap1y = self.object_1.center.y 
            
            self.object_1.center.x = self.object_2.center.x 
            self.object_1.center.y = self.object_2.center.y 
            
            self.object_2.center.x = swap1x 
            self.object_2.center.y = swap1y 
            
        elif self.object_1.radius > self.object_2.radius:
            
            swap1x = self.object_1.center.x 
            swap1y = self.object_1.center.y 
            
            #this is to set the obejct a set space away from the bigger object
            if swap1x > 0:
                swap1x += 25
                
            else:
                swap1x -= 25
            
            if swap1y > 0:
                swap1x += 25
                
            else:
                swap1y -= 25

            self.object_2.center.x = swap1x 
            self.object_2.center.y = swap1y 
            self.object_2.bounce_horizontal()
            
            self.object_1.bounce_vertical()

        elif self.object_1.radius < self.object_2.radius:
            
            swap2x = self.object_2.center.x 
            swap2y = self.object_2.center.y 
            
            if swap2x > 0:
                swap2x += 25
                
            else:
                swap2x -= 25
            
            if swap2y > 0:
                swap2x += 25
                
            else:
                swap2y -= 25

            self.object_1.center.x = swap2x 
            self.object_1.center.y = swap2y 
            self.object_1.bounce_horizontal()
            
            self.object_2.bounce_vertical()
