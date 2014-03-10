"""
    spriteTools.py - module to define tools for manipulating sprites
    
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

class SpriteSheet():
    """
        Class to get sprites from a sprite sheet
    """
    # Constructor
    def __init__(self,file):
        self.imageSheet = pygame.image.load(file).convert()
    
    def getImagePixel(self,x,y,width,height):
        """
         Grab a sprite from a sprite sheet based on the top left x,y position
         of the sprite, its width and its height
        """
    
        # blank image
        sprite = pygame.Surface([width,height]).convert()
        
        # copy sprite from sprite sheet
        sprite.blit(self.imageSheet,(0,0),(x,y,width,height))
        
        return sprite
    
    def getImageGrid(self,row,column,width,height):
        """
         Grab a sprite from a sprite sheet assuming it is based on a grid.
         One needs the width and height of each sprite, and the row and column
         of the sprite one wants to extract. The top left one is row=0, column=0.
         """    
         
        # blank image
        sprite = pygame.Surface([width,height]).convert()
        
        # copy sprite from sprite sheet
        sprite.blit(self.imageSheet,(0,0),(width*column,height*row,width*(column+1),
                    height*(row+1)))

        return sprite