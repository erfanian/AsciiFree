##########################################################################
## AsciiFree project #####################################################
## An open-source, ASCII-graphics version of SkiFree #####################
## Spring 2013 ###########################################################
## <<LICENSE INFO HERE>>

from SubclassMustImplementException import *


class DrawableObject:
        # represents an object that can be drawn in ASCII
        # This class is our basic sprite - everything to be drawn
        # will be a DrawableObject subclass.  I'm still not
        # entirely clear on how to handle the character map yet...
        # I'm thinking I'll leave it up to the subclasses to keep
        # track of that and make this class completely abstract.

        # ivars
        posX = 0   # the origin.  type int
        posY = 0
        name = "<unnamed>"
        
	# nothing much to do in the init method
        def __init__(self):
		pass
        # subclasses must override this method!
        # called by AsciiRenderingManager - returns the character map to use for the given context
        # if you don't care about drawing in multiple contexts, just return one.
        # if you do care, you'll have to handle multiple character maps.  I suggest an array of different maps to draw.
        def characterMapForDrawingContext(self, drawingContext, boundX, boundY):
                raise SubclassMustImplementException()
