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
  drawable_object_start_screen.name = "start_screen"
  drawable_object_start_screen.payload = """
      ___              _ _ ______             
     /   |  __________(_|_) ____/_______  ___ 
    / /| | / ___/ ___/ / / /_  / ___/ _ \/ _ \ 
   / ___ |(__  ) /__/ / / __/ / /  /  __/  __/
  /_/  |_/____/\___/_/_/_/   /_/   \___/\___/
  
    Press enter to continue, and q to quit."""
  drawable_object_start_screen.human_position = "center"
  drawable_object_cursor = drawable_object.DrawableObject()
  drawable_object_cursor.name = "cursor"
  drawable_object_cursor.payload = ""
	
  _drawable_objects = {"start_screen" : drawable_object_start_screen,
		       "cursor": drawable_object_cursor}
	
  def __init__(self, screen):
    self._screen = screen
	
  # register an object for drawing
  def add_drawable_object(self, object_to_add):
    # TODO
    pass

  # remove an object from the drawing stack
  def remove_drawable_object(self, object_to_remove):
    # TODO
    pass

  # cause the manager to draw all objects
  def draw(self, drawing_context=None):
    for item in self._drawable_objects.values():
      if item.human_position == "center":
        i = 0
        line_len = 0
        line_height = 0
        for line in item.payload.splitlines():
          if len(line) > line_len:
            line_len = int(len(line)/2)
          line_height += 1
        for line in item.payload.splitlines():
          self._screen.add_str(y=int((self._screen.height/2) - int(line_height/2) + i),
                               x=(int(self._screen.width/2) - line_len),
                               output=line)
          i += 1
      else:
        self._screen.add_str(self._screen._cur_y,
                             self._screen._cur_x,
                             item.payload)

  # helpers
  def screen_clear(self):
    self._screen.screen_clear()
    
  def screen_refresh(self):
    self._screen.screen_refresh()
    
  def stop_screen(self):
    self._screen.stop_screen()

  def set_object_payload(self, name, payload):
    obj = self._drawable_objects.get(name)
    obj.payload = payload
    
  def checkBounds(self, x_delta, y_delta):
    self._screen.checkBounds(x_delta, y_delta)

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
