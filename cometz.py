import pygame, sys
from constants     import *
from core          import Game


"""
    cometz.py - main module
    
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

# Main function - not actually necessary in Python, but keeps stuff local
#               - also prevents code from running if script is imported



def main():

    # For avoiding sound delay - thanks to BigglesW at StackOverflow
    pygame.mixer.pre_init(44100, -16, 1, 512)
    
    # Initialization ======================
    pygame.init()

    # frames per second setting
    FPS = 60
    fpsClock = pygame.time.Clock()


    
    # set up the window
    screen  = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('CometZ')

    # Setting window icon
    icon = pygame.image.load("iconShip.png")
    pygame.display.set_icon(icon)
    
    # gameState
    # States available:
    # menu, pause, game, gameOver
    
    # Create game instance
    game = Game()
    
    # =====================================

    # Main game loop
    while True:

        # ===========================================================
        # EVENTS     ================================================
        # ===========================================================
        
        # check all events in event list
        for event in pygame.event.get():
            game.handle(event)
                    
        # for continuously pressed keys
        keys = pygame.key.get_pressed()
        game.keys(keys)
        
        
        # ===========================================================    
        # GAME LOGIC ================================================
        # ===========================================================
        
        # update game
        game.update()
        
        # ===========================================================    
        # DRAWING    ================================================
        # ===========================================================
        
        # draw to the screen
        game.draw(screen)
        pygame.display.update()
        
        # ===========================================================    
        # OTHER      ================================================
        # ===========================================================
        
        fpsClock.tick(FPS)       
            
    
# execute main() if this is not being imported
if __name__ == "__main__":
    main()
