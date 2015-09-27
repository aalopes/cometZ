"""

    poweUps.py - module for declaring power ups
    
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

class PowerUp(pygame.sprite.Sprite):
    """
        Power-ups superclass
        
        file        - sprite sheet file
        alpha       - alpha color
        x,y         - initial coordinates of object
        speed       - speed
        nSprites    - number of sprites in sprite sheet
        sprRow      - number of the row where the sprites are located (assuming animation is in same row)
        sprWidth     - width of each sprite
        sprHeight   - height of each sprite
    """
    # Constructor
    def __init__(self):
        # Calling parent class constructor
        pygame.sprite.Sprite.__init__(self) 
        
        
    def update():
        """
            Method for updating state of powerUp
        """
        pass
        # must throw exception if not defined!
    
    def pickUp():
        pass
        # must throw exception if not defined!
    def animate():
        pass
        # throw exception!
    
    
class Health25(PowerUp):
    def __init__(self,x,y,speed):
        # Calling parent class constructor
        PowerUp.__init__(self)
        
        # Sprite parameters:
        file  = SPR_FOLDER + "powerUp.png"
        self.alpha = ALPHA 
        sprRow      = 0
        sprWidth    = 32
        sprHeight   = 32
        nSprites    = 4
        
        # Load sprite image
        #self.image = pygame.image.load(file).convert()

        # Load sprite sheet
        self.sprites = []
        sprites = SpriteSheet(file)
        for sprColumn in range(nSprites):
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight)) 
            # doubling the thing so the refresh speed is slower
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight))
            
        # Load first sprite
        self.image = self.sprites[0]
        # Rectangular limits of the sprite
        self.rect = self.image.get_rect()

        # Initial values --------------
        self.rect.x    = x
        self.rect.y    = y
        self.speed     = speed
        self.state     = 0        # animation state
        self.power     = 25
        
        # alpha color
        self.image.set_colorkey(self.alpha)
        # Mask - for using perfect pixel collisions
        self.mask = pygame.mask.from_surface(self.image)
        #------------------------------            

        
    def animate(self):
        """
            Method for updating sprite animation
        """
        self.state += 1
        if self.state > len(self.sprites)-1:
            self.state = 0
        self.image = self.sprites[self.state]
        self.image.set_colorkey(self.alpha) 
        
    def update(self):
        """
            Method for updating state of powerUp
        """
        self.rect.x = self.rect.x + self.speed
        
    def pickUp(self,player):
        player.shield += self.power
        if player.shield > 100:
            player.shield = 100

class Health100(PowerUp):
    def __init__(self,x,y,speed):
        # Calling parent class constructor
        PowerUp.__init__(self)
        
        # Sprite parameters:
        file  = SPR_FOLDER + "powerUp100.png"
        self.alpha = ALPHA 
        sprRow      = 0
        sprWidth    = 32
        sprHeight   = 32
        nSprites    = 4
        
        # Load sprite image
        #self.image = pygame.image.load(file).convert()

        # Load sprite sheet
        self.sprites = []
        sprites = SpriteSheet(file)
        for sprColumn in range(nSprites):
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight)) 
            # doubling the thing so the refresh speed is slower
            self.sprites.append(sprites.getImageGrid(sprRow,sprColumn,sprWidth,sprHeight))
            
        # Load first sprite
        self.image = self.sprites[0]
        # Rectangular limits of the sprite
        self.rect = self.image.get_rect()

        # Initial values --------------
        self.rect.x    = x
        self.rect.y    = y
        self.speed     = speed
        self.state     = 0        # animation state
        self.power     = 100
        
        # alpha color
        self.image.set_colorkey(self.alpha)
        # Mask - for using perfect pixel collisions
        self.mask = pygame.mask.from_surface(self.image)
        #------------------------------            

        
    def animate(self):
        """
            Method for updating sprite animation
        """
        self.state += 1
        if self.state > len(self.sprites)-1:
            self.state = 0
        self.image = self.sprites[self.state]
        self.image.set_colorkey(self.alpha) 
        
    def update(self):
        """
            Method for updating state of powerUp
        """
        self.rect.x = self.rect.x + self.speed
        
    def pickUp(self,player):
        player.shield += self.power
        if player.shield > 100:
            player.shield = 100
        