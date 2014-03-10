"""

    volume.py - module defining classes displaying and handling volume menu
    
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
import pickle

class Volume():

    """
        Class for generating volume menu based on 
        a background image and the current volume
        
        It takes as input a background image and a dictionary containing the
        current volume
        
        We will assume that the only way the volume can be changed throughout the game
        is through the class methods
        
        If one needs to change the text size or color, one can make use of the
        class attributes
    """
    # Constructor
    def __init__(self,backg,volume):

        # Input
        # items  - list of strings (menu elements)
        # backg  - background
        # volume - dictionary of the form {"sound": soundValue, "music": musicValue }
        
        self.items       = ["Back", "Sound Volume", "Music Volume"]
        self.backg       = backg
        self.musicVol    = volume["music"]
        self.soundVol    = volume["sound"]
        self.state       = len(self.items)-1    # currently selected menu item
                                                # in this case there are only 3 states
        
        # Default values
        self.fontType        = "Arial"          # font type
        self.fontSizeNSelec  = 40               # font size for non selected items
        self.fontSizeSelec   = 50               # font size for selected items
        self.spread          = 80               # how far apart the lines are
        self.fontColor       = WHITE            # text color
        
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

    def left(self):
        """
            moving "left" on the menu
        """   
        if self.state == 2:            # if we have the music volume selected
            self.musicVol += -10        # increment
            if self.musicVol < 0:      # if it exceeds the minimum
                self.musicVol = 0

            # save new volume to file
            pickle.dump( {"sound": self.soundVol, 
                          "music": self.musicVol}, 
                          open( "volume.p", "wb" ) )
                              
            return self.musicVol/100. # return value so we can change volume in the game
                              
        elif self.state == 1:          # if we have the sound volume selected
            self.soundVol += -10       # increment
            if self.soundVol < 0: # if it exceeds the minimum
                self.soundVol = 0

            # save new volume to file
            pickle.dump( {"sound": self.soundVol, 
                          "music": self.musicVol}, 
                          open( "volume.p", "wb" ) )
                              
            return self.soundVol/100. # return value so we can change volume in the game
            
    def right(self):
        """
            moving "right" on the menu
        """   
        if self.state == 2:            # if we have the music volume selected
            self.musicVol += 10        # increment
            if self.musicVol > 100:    # if it exceeds the maximum
                self.musicVol = 100

            # save new volume to file
            pickle.dump( {"sound": self.soundVol, 
                          "music": self.musicVol}, 
                          open( "volume.p", "wb" ) )
                              
            return self.musicVol/100. # return value so we can change volume in the game
                              
        elif self.state == 1:         # if we have the sound volume selected
            self.soundVol += 10       # increment
            if self.soundVol > 100:   # if it exceeds the maximum
                self.soundVol = 100

            # save new volume to file
            pickle.dump( {"sound": self.soundVol, 
                          "music": self.musicVol}, 
                          open( "volume.p", "wb" ) )
                              
            return self.soundVol/100. # return value so we can change volume in the game
        
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

        # draw background
        screen.blit(self.backg.image,(self.backg.x,self.backg.y))    
        

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
        
        # generate volume values text (in percentage)
        if self.state == 2:   # music volume selected
            txtMusVol = fontSelected.render( str(self.musicVol) + "%", True, self.fontColor)
            txtSndVol = fontNSelected.render( str(self.soundVol) + "%", True, self.fontColor)
        elif self.state == 1: # sound volume selected
            txtMusVol = fontNSelected.render( str(self.musicVol) + "%", True, self.fontColor)
            txtSndVol = fontSelected.render( str(self.soundVol) + "%", True, self.fontColor)
        elif self.state == 0: # back selected
            txtMusVol = fontNSelected.render( str(self.musicVol) + "%", True, self.fontColor)
            txtSndVol = fontNSelected.render( str(self.soundVol) + "%", True, self.fontColor)
            
        # blitting menu items to the screen
        # we will center everything
        i = 0 # counter
        something = 50
        for text in textList:
            i += 1
            screen.blit(text, [WINDOW_WIDTH/2-text.get_width()/2, WINDOW_HEIGHT/2-text.get_height()/2-i*self.spread+ something*len(self.items)])
        # blit now the volume values
        screen.blit(txtMusVol, [WINDOW_WIDTH/2+textList[-1].get_width()/2 + 30, WINDOW_HEIGHT/2-textList[-1].get_height()/2-3*self.spread+ something*len(self.items)])
        screen.blit(txtSndVol, [WINDOW_WIDTH/2+textList[-2].get_width()/2 + 30, WINDOW_HEIGHT/2-textList[-2].get_height()/2-2*self.spread+ something*len(self.items)])
        
        