##########################################################################
## AsciiFree project #####################################################
## An open-source, ASCII-graphics version of SkiFree #####################
## Spring 2013 ###########################################################
## <<LICENSE INFO HERE>>


# needed system components
import curses


# engine components
from SubclassMustImplementException import *
from AsciiRenderingManager import *
from EventsManager import *

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
        raise SubclassMustImplementException()






    # public - call but do not override!
    def start(self):
        self.runloop()
        
    def setActiveDrawingContext(self, newContext):
        self._drawingContext = newContext


    # private - do not touch!
    def runloop(self):
        while (self._shouldKeepRunning):
            # TODO: here is where we call self.iteration() and then redraw the UI
            self.iteration()
            self._renderingManager.draw(self._drawingContext)
        # end of eternal run loop



    def __init__(self):
#        self._screen = curses.initscr()
        self._renderingManager = AsciiRenderingManager(self._screen, 20, 20)
        self._eventsManager    = EventsManager()


    # private - ivars
    _shouldKeepRunning = True
    


    # private - managers
    # these are set up in the __init__ method
    _screen = None
    _renderingManager = None
    _eventsManager = None
    _drawingContext = 0










