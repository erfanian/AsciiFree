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
import drawable_object 


class AsciiRenderingManager(object):
  # the manager for display of the game environment to
  # the screen.  Tracks a list of DrawableObjects which
  # it draws every time draw() is called.  Also
  # performs boundschecking, collision detection, and 
  # displays an error message if the terminal is sized
  # too small to continue.
  drawable_object_start_screen = drawable_object.DrawableObject()
  drawable_object_start_screen.payload = """
      ___              _ _ ______             
     /   |  __________(_|_) ____/_______  ___ 
    / /| | / ___/ ___/ / / /_  / ___/ _ \/ _ \ 
   / ___ |(__  ) /__/ / / __/ / /  /  __/  __/
  /_/  |_/____/\___/_/_/_/   /_/   \___/\___/
  
    Press enter to continue, and q to quit."""
	
  _drawable_objects_dictionary = {'drawable_object_start_screen' : drawable_object_start_screen.payload}
  _screen = None
	
  def __init__(self, screen, min_x, min_y):
    # TODO
    self._screen = screen
    pass
	
  # register an object for drawing
  def add_drawable_object(self, object_to_add):
    # TODO
    pass

  # remove an object from the drawing stack
  def remove_drawable_object(self, object_to_remove):
    # TODO
    pass

  # cause the manager to draw all objects
  # pass an int for drawingContext to send a message to all the drawableObjects
  def draw(self, drawing_context=None):
    # TODO
    pass
        
  # helpers
  def clear_screen(self):
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
