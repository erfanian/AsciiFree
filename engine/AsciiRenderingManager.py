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
## AsciiRenderingManager.py contributors:                                #
## Chris Cornelius                                                       #
##########################################################################

import curses
from engine.DrawableObject import  * 


class AsciiRenderingManager:
        # the manager for display of the game environment to
        # the screen.  Tracks a list of DrawableObjects which
        # it draws every time draw() is called.  Also
        # performs boundschecking, collision detection, and 
        # displays an error message if the terminal is sized
        # too small to continue.
	DrawableObjectStartScreen = DrawableObject
	DrawableObjectStartScreen.payload = "    ___              _ _ ______             \n   /   |  __________(_|_) ____/_______  ___ \n  / /| | / ___/ ___/ / / /_  / ___/ _ \/ _ \ \n / ___ |(__  ) /__/ / / __/ / /  /  __/  __/\n/_/  |_/____/\___/_/_/_/   /_/   \___/\___/ \n"
	
        # ivars
	_drawableObjectsDictionary = {'DrawableObjectStartScreen' : DrawableObjectStartScreen.payload}  # will hold all the DrawableObjects we want to write to the screen
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
