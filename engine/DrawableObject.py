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
## DrawableObject.py contributors:                                       #
## Chris Cornelius                                                       #
##########################################################################

#from SubclassMustImplementException import *


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
	payload = "Test Payload"
        
	# nothing much to do in the init method
	def __init__(self):
		pass
	# subclasses must override this method!
	# called by AsciiRenderingManager - returns the character map to use for the given context
	# if you don't care about drawing in multiple contexts, just return one.
	# if you do care, you'll have to handle multiple character maps.  I suggest an array of different maps to draw.
	def characterMapForDrawingContext(self, drawingContext, boundX, boundY):
		pass # raise SubclassMustImplementException()
