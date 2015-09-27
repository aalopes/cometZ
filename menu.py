"""

    menu.py - module defining classes for building menus
    
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

class Menu():

    """
        Class for generating a menu based on
        a set of items and a background image
        Still needs some external code to
        handle the state (whenever return is pressed for example)
        
        It takes as input a list of strings (representing the menu items)
        and a background image. The first item in the list is the bottom one
        
        If one needs to change the text size or color, one can make use of the
        class attributes
    """
    # Constructor
    def __init__(self,items,backg):

        # Input
        self.items      = items
        self.backg      = backg
        # Default values
        self.state          = len(self.items)-1    # currently selected menu item
        self.fontType       = "Arial"              # font type
        self.fontSizeNSelec = 40                   # font size for non selected items
        self.fontSizeSelec  = 50                   # font size for selected items
        self.spread         = 80                   # how far apart the menu items are
        self.fontColor      = WHITE                # text color
    def up(self):
        """
            moving up on the menu
        """
        self.state += 1
        # if we go way too up
        if self.state > len(self.items) - 1:
            self.state = len(self.items) - 1 # simply stay at the top item (we could also loop around...)
    def down(self):
        """
            moving down on the menu
        """
        self.state -= 1
        # if we go way too down
        if self.state < 0:
            self.state = 0 # simply stay at the bottom item (we could also loop around...)
    
    
    def press(self):
        """
            whenever the selected item is pressed
        """
        return self.state
        
    def draw(self,screen):
        """
            drawing the menu
        """
        # erase screen
        screen.fill(BLACK)

        # draw background - since the background is scrolling
        # we shall draw two side by side to prevent the background from ending
        # this way it repeats itself
        screen.blit(self.backg.image,(self.backg.x,self.backg.y))
        screen.blit(self.backg.image,(self.backg.x + self.backg.width,self.backg.y))        
        
        # drawing text
        fontNSelected = pygame.font.SysFont(self.fontType, self.fontSizeNSelec)
        fontSelected  = pygame.font.SysFont(self.fontType, self.fontSizeSelec)
        
        textList = [] # we could actually initialize this, 
                  # since we know its size, but this won't impact performance
        # generate all menu items
        for item in self.items:
            textList.append( fontNSelected.render(item, True, self.fontColor) )
        # selected item gets a different font
        textList[self.state] = fontSelected.render(self.items[self.state], True, self.fontColor)
        
        # blitting text to the screen
        # we will center everything
        i = 0 # counter
        something= 50 # this needs to be calculated!
        for text in textList:
            i += 1
            screen.blit(text, [WINDOW_WIDTH/2-text.get_width()/2, WINDOW_HEIGHT/2-text.get_height()/2-i*self.spread+ something*len(self.items)])