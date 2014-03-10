"""
    enemies.py - module used to declare classes for constructing enemies
    
    ---------------------------------------------------------------------------
    
    Copyright 2014 Alexandre Lopes <aalopes@ovi.com>
    
    This file is part of CometZ.

    CometZ is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    CometZ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with CometZ.  If not, see <http://www.gnu.org/licenses/>.
    
    ---------------------------------------------------------------------------
"""

import pygame
from constants   import *
from spriteTools import SpriteSheet
from random      import randint
from math        import cos


class EnemyShip(pygame.sprite.Sprite):
    """
        SuperClass for enemy ships
        
        file        - sprite sheet file
        alpha       - alpha color
        x,y         - initial coordinates of object
        speed       - speed
        nSprites    - number of sprites in sprite sheet
        sprRow      - number of the row where the sprites are located (assuming animation is in same row)
        sprWidth     - width of each sprite
        sprHeight   - height of each sprite
        
        Methods are defined for updating ship animation
    """
    # Constructor
    def __init__(self,x,y,speed):   
        # Calling parent class constructor
        pygame.sprite.Sprite.__init__(self) 
               
        
    def animate(self):
        """
            Method for updating sprite animation
        """
        self.state += 1
        if self.state > len(self.sprites)-1:
            self.state = 0
        self.image = self.sprites[self.state]
        self.image.set_colorkey(self.alpha)  
        


class EnemyShipX001(EnemyShip):
    """
        X001 enemies
        Movement: linear movement
    """
    # Constructor
    def __init__(self,x,y,speed):  
        # Call the parent constructor
        EnemyShip.__init__(self,x,y,speed)
        
        # Sprite parameters:
        file  = SPR_FOLDER + "badGirl003.png"
        self.alpha = ALPHA 
        sprRow      = 0
        sprWidth    = 64
        sprHeight   = 32
        nSprites    = 2
        
        # Load sprite image
        #self.image = pygame.image.load(file).convert()

        # Load sprite sheet
        self.sprites = []
        sprites = SpriteSheet(file)
        for sprColumn in range(nSprites):
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight)) 
            # doubling the thing so the refresh speed is slower
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight)) 
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight)) 

        # Load first sprite
        self.image = self.sprites[0]
        # Rectangular limits of the sprite
        self.rect = self.image.get_rect()

        # Initial values --------------
        self.rect.x    = x
        self.rect.y    = y
        self.direction = "right"
        self.speed     = speed
        self.state     = 0        # animation state
        self.score     = 10
        
        # alpha color
        self.image.set_colorkey(self.alpha)
        # Mask - for using perfect pixel collisions
        self.mask = pygame.mask.from_surface(self.image)
        #------------------------------
    
    # Override method (shouldn't override completely, it should throw an error if its not defined above)
    # Also probably the sprite should go in here but okay
    def update(self):
        """
            Method for updating state
        """
        # moving in a straight line
        self.rect.x = self.rect.x + self.speed
     

class EnemyShipX002(EnemyShip):
    """
        X002 enemies
        Movement: zig-zag pattern
    """
    # Constructor
    def __init__(self,x,y,speed):  
        # Call the parent constructor
        EnemyShip.__init__(self,x,y,speed)
            
        # Sprite parameters:
        file  = SPR_FOLDER + "bad006.png"
        self.alpha = ALPHA
        sprRow      = 0
        sprWidth    = 32
        sprHeight   = 32
        nSprites    = 2
        
        # Load sprite image
        #self.image = pygame.image.load(file).convert()

        # Load sprite sheet
        self.sprites = []
        sprites = SpriteSheet(file)
        for sprColumn in range(nSprites):
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight)) 
            # doubling the thing so the refresh speed is half
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight))
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight))
        # Load first sprite
        self.image = self.sprites[0]
        
        # Rectangular limits of the sprite
        self.rect = self.image.get_rect()

        # Initial values --------------
        self.rect.x    = x
        self.rect.y    = y
        self.direction = "right"
        self.speed     = speed
        self.state     = 0        # animation state
        self.score     = 40
        
        # alpha color
        self.image.set_colorkey(self.alpha)
        # Mask - for using perfect pixel collisions
        self.mask = pygame.mask.from_surface(self.image)
        #------------------------------

        # decide whether ship is going up or down
        if randint(1,2) == 1:
            self.speedY = self.speed # up
        else:
            self.speedY = -self.speed # down
        
    # Override method (shouldn't override completely, it should throw an error if its not defined above)
    # Also probably the sprite should go in here but okay
    def update(self):
        """
            Method for updating state
        """
        # This one moves in a zig zag fashion and bounces off the window's walls
        # We code here only the bouncing on the top and bottom boundary
 
        self.rect.x = self.rect.x + self.speed   # move forward
        self.rect.y = self.rect.y + self.speedY  # move up (speed is negative)
        # if it hits top wall
        if self.rect.y <= 0:
            self.rect.y = 0            # put it back into the window 
            self.speedY = -self.speedY # reverse speed
        # if it hits bottom wall
        if self.rect.y + self.rect.width >= WINDOW_HEIGHT:
            self.rect.y = WINDOW_HEIGHT - self.rect.width    # put it back into the window 
            self.speedY = -self.speedY                       # reverse speed               
            
            
class EnemyShipX003(EnemyShip):
    """
        X002 enemies
        Movement: helix
    """
    # Constructor
    def __init__(self,x,y,speed):  
        # Call the parent constructor
        EnemyShip.__init__(self,x,y,speed)
            
        # Sprite parameters:
        file  = SPR_FOLDER + "badBoy002.png"
        self.alpha = ALPHA
        sprRow      = 0
        sprWidth    = 32
        sprHeight   = 32
        nSprites    = 2
        
        # Load sprite image
        #self.image = pygame.image.load(file).convert()

        # Load sprite sheet
        self.sprites = []
        sprites = SpriteSheet(file)
        for sprColumn in range(nSprites):
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight)) 
            # doubling the thing so the refresh speed is half
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight))
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight))
        # Load first sprite
        self.image = self.sprites[0]
        
        # Rectangular limits of the sprite
        self.rect = self.image.get_rect()

        # Initial values --------------
        self.rect.x           = x
        self.rect.y           = y
        self.yInitial         = y
        self.direction        = "right"
        self.speed            = speed
        self.state            = 0        # animation state
        self.score            = 20
        
        # alpha color
        self.image.set_colorkey(self.alpha)
        # Mask - for using perfect pixel collisions
        self.mask = pygame.mask.from_surface(self.image)
        #------------------------------

        # decide whether ship is going up or down
        if randint(1,2) == 1:
            self.speedY = self.speed # up
        else:
            self.speedY = -self.speed # down
        
    # Override method (shouldn't override completely, it should throw an error if its not defined above)
    # Also probably the sprite should go in here but okay
    def update(self):
        """
            Method for updating state
        """
        # This one moves in a zig zag fashion and bounces off the window's walls
        # We code here only the bouncing on the top and bottom boundary
 
        self.rect.x = self.rect.x + self.speed   # move forward
        self.rect.y = 100*cos(0.01*self.rect.x) + self.yInitial
        # if it hits top wall
        if self.rect.y <= 0:
            self.rect.y = 0            # put it back into the window 
        # if it hits bottom wall
        if self.rect.y + self.rect.width >= WINDOW_HEIGHT:
            self.rect.y = WINDOW_HEIGHT - self.rect.width    # put it back into the window 