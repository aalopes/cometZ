"""
    player.py - module to define player related classes: ships and weapons
    
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

class Ship(pygame.sprite.Sprite):
    """
        SuperClass for user ships
        
        alpha       - alpha color
        x,y         - initial coordinates of object
        speed       - speed
        nSprites    - number of sprites in sprite sheet
        sprRow      - number of the row where the sprites are located (assuming animation is in same row)
        sprWidth     - width of each sprite
        sprHeight   - height of each sprite
        
        Methods are defined for updating ship animation and moving it

    """
    # Constructor
    def __init__(self):       
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

    def left(self):
        """
            Method for moving ship left
        """
        self.rect.x -= self.speed
        
    def right(self):
        """
            Method for moving ship right
        """
        self.rect.x += self.speed
        
    def up(self):
        """
            Method for moving ship up
        """
        self.rect.y -= self.speed
        
    def down(self):
        """
            Method for moving ship down
        """
        self.rect.y += self.speed
        
        
class ShipY001(Ship):
    """
        User ShipY001
        
    """
    # Constructor
    def __init__(self):
        # Calling parent class constructor
        Ship.__init__(self)

        # Sprite parameters:
        file        = SPR_FOLDER + "shipz007.png"
        sprRow      = 0
        sprWidth    = 128
        sprHeight   = 64
        nSprites    = 2
        self.alpha  = ALPHA

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
        self.rect.x    = 10
        self.rect.y    = 10
        self.direction = "right"
        self.shield    = 100
        self.hull      = 100
        self.state     = 0        # animation state
        self.speed     = 0
        # ----------------------------
        
        # alpha color
        self.image.set_colorkey(self.alpha)
        # Mask - for using perfect pixel collisions
        self.mask = pygame.mask.from_surface(self.image)
        #------------------------------     
        
class Laser(pygame.sprite.Sprite):
    """
        Class for laser weapons
    """
    def __init__(self,x,y):
    
        # Calling parent class constructor
        pygame.sprite.Sprite.__init__(self) 
        # Sprite parameters:
        file        = SPR_FOLDER + "laser.png"
        sprRow      = 0
        sprWidth    = 64
        sprHeight   = 16
        nSprites    = 1
        self.alpha  = ALPHA

        # Load sprite sheet
        self.sprites = []
        sprites = SpriteSheet(file)
        for sprColumn in range(nSprites):
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight))
        # Load first sprite
        self.image = self.sprites[0]
               
        # Rectangular limits of the sprite
        self.rect = self.image.get_rect()

               
        # Initial values --------------
        self.rect.x    = x
        self.rect.y    = y
        self.direction = "right"
        self.speed     = 30
        self.state     = 0        # animation state

        
        # alpha color
        self.image.set_colorkey(self.alpha)
        # Mask - for using perfect pixel collisions
        self.mask = pygame.mask.from_surface(self.image)
        #------------------------------    
        
        #------------------------------
    def update(self):
        """
            Method for updating state
        """
        
        self.rect.x = self.rect.x + self.speed
        
    def animate(self):
        """
            Method for updating sprite animation
        """
        self.state += 1
        if self.state > len(self.sprites)-1:
            self.state = 0
        self.image = self.sprites[self.state]
        self.image.set_colorkey(self.alpha) 