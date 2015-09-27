"""

    credits.py - module defining classes for displaying credits
    
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

from constants import *
import pygame

class Credits():

    """
        Class for generating credits based on 
        a set of items and a background image
        
        It takes as input a list of strings (each corresponding to a line on
        the screen) and a background image. 
        The first item in the list is the bottom one
        
        If one needs to change the text size or color, one can make use of the
        class attributes
    """
    # Constructor
    def __init__(self,items,backg):

        # Input
        self.items      = items
        self.backg      = backg
        # Default values
        self.fontType   = "Arial"              # font type
        self.fontSize   = 30                   # font size 
        self.spread     = 80                   # how far apart the lines are
        self.fontColor  = WHITE                # text color
        self.textList   = []                   # we could initialize this but
                                               # there are no performance issues
        
        # generating all text
        font = pygame.font.SysFont(self.fontType, self.fontSize)
        for item in self.items:
            self.textList.append( font.render(item, True, self.fontColor) )
        
        
    def draw(self,screen):
        """
            drawing the credits
        """
        # erase screen
        screen.fill(BLACK)

        # draw background
        screen.blit(self.backg.image,(self.backg.x,self.backg.y))    
                
        # blitting text to the screen
        # we will center everything
        i = 0 # counter
        something = 50
        for text in self.textList:
            i += 1
            screen.blit(text, [WINDOW_WIDTH/2-text.get_width()/2, WINDOW_HEIGHT/2-text.get_height()/2-i*self.spread+ something*len(self.items)])
    