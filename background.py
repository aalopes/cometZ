"""

    background.py - module for dealing with background images

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

class Background():
    """
        Class defining background image
        Has method for scrolling the background as a function of time
        or 
        whenever necessary (this is still not implemented)
    """
    # Constructor
    def __init__(self,file):
    
        self.image               = pygame.image.load(file).convert()
        self.x                   = 0
        self.y                   = 0
        (self.width,self.height) = self.image.get_size()
    def scroll(self,ammount):
        """
            Function for scrolling background along x axis (for now)
        """
        self.x -= ammount
        if self.x <= - self.width:  # if it has gotten out of the screen
            self.x = 0              # put it in the initial place