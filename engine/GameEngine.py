#! /usr/bin/env python3.0
##########################################################################
## AsciiFree project #####################################################
## An open-source, ASCII-graphics version of SkiFree #####################
## Spring 2013 ###########################################################
# This program is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# This program is distributed in the hope that it will be useful,        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
##########################################################################
## GameEngine.py contributors:                                           #
## Chris Cornelius                                                       #
##########################################################################

# needed system components
import curses


# engine components
from engine.SubclassMustImplementException import *
from engine.AsciiRenderingManager import *
from engine.EventsManager import *
from engine.screenManager import Screen
from engine.inputManager import Input

class GameEngine:
    # The main engine for a game - implement your game by making a subclass
    #     of this object.  Manages I/O, events processing, screen drawing,
    #     and the run loop for the game.  Subclassers should take note of
    #     which methods to override and which to let alone.




    # subclassable - override these!
    def iteration(self):
        # This method is called on every time through the game loop.  In
        # this method, you should check input, determine what the display 
        # should be, and return quickly.

        evalChar = self._inputManager.dumpInput()
        
        if evalChar == None:
            # we got no input - nothing to do
            pass
        else:
            self._screen.move(1,0)
            self._screen.addstr(str(evalChar))
            self._screen.screenRefresh()


            if evalChar == 113:
                # a 'q' means quit!
                self._screen
                self._shouldKeepRunning = False # TODO: make a helper method for this assignment
            else:
                pass
            

        # the following is for later:
        pass # raise SubclassMustImplementException()






    # public - call but do not override!
    def start(self):
        self.runloop()
        
    def setActiveDrawingContext(self, newContext):
        self._drawingContext = newContext


    # private - do not touch!
    def runloop(self):
        self._screen.addstr(self._renderingManager._drawableObjectsDictionary['DrawableObjectStartScreen'])

        while (self._shouldKeepRunning):
            # here is where we call self.iteration() and then redraw the UI
            self.iteration()
            self._renderingManager.draw(self._drawingContext)
        # end of eternal run loop
        self._screen.stopScreen()


    def __init__(self):
        self._screen = Screen()
        self._screen.startScreen()
        self._renderingManager = AsciiRenderingManager(self._screen, 20, 20)
        self._inputManager = Input()
        self._inputManager.setUp(self._screen)
        self._inputManager.start()

    # private - ivars
    _shouldKeepRunning = True
    


    # private - managers
    # these are set up in the __init__ method
    _screen = None
    _renderingManager = None
    _inputManager = None
    _drawingContext = 0










