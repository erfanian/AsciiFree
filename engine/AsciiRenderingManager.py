##########################################################################
## AsciiFree project #####################################################
## An open-source, ASCII-graphics version of SkiFree #####################
## Spring 2013 ###########################################################
## <<LICENSE INFO HERE>>

import curses


class AsciiRenderingManager:
        # the manager for display of the game environment to
        # the screen.  Tracks a list of DrawableObjects which
        # it draws every time draw() is called.  Also
        # performs boundschecking, collision detection, and 
        # displays an error message if the terminal is sized
        # too small to continue.

        # ivars
        _drawableObjectsArray = []  # will hold all the DrawableObjects we want to write to the screen
	_screen = None
	
        # sets up the rendering engine
        # requires a minimum X and Y dimensions that are allowed
        def __init__(self, screen, minX, minY):
		# TODO
		self._screen = screen
		pass
	
        # register an object for drawing
        def addDrawableObject(self, objectToAdd):
		# TODO
		pass

        # remove an object from the drawing stack
        def removeDrawableObject(self, objectToRemove):
		# TODO
		pass

        # cause the manager to draw all objects
        # pass an int for drawingContext to send a message to all the drawableObjects
        def draw(self, drawingContext=0):
		# TODO
		pass
        

        # helpers
        def clearScreen(self):
		# TODO
		pass

        def forceRedraw(self):
		# TODO
		pass

        # internals for rendering the screen
        def drawCharacterMap(self, characterMapToDraw):
		# TODO
		pass
        
        def requestScreenUpdateForRegion(self):
		# TODO
		pass
