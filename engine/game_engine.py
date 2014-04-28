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
## Eric Erfanian                                                         #
##########################################################################

import curses
import math

import ascii_rendering_manager
import screen_manager
import input_manager

class GameEngine(object):
  # The main engine for a game - implement your game by making a subclass
  #     of this object.  Manages I/O, events processing, screen drawing,
  #     and the run loop for the game.  Subclassers should take note of
  #     which methods to override and which to let alone.
  def __init__(self):
    self._screen = screen_manager.Screen()
    self._input_man = input_manager.Input(self._screen.get_screen())
    self._rendering_manager = ascii_rendering_manager.AsciiRenderingManager(
		    self._screen, 20, 20)
    self._input_man.start()
    self._should_keep_running = True
    self._show_title = True
    self._title_text = str(self._rendering_manager.
		       _drawable_objects_dictionary.get(
		      'drawable_object_start_screen'))
    self._cur_x = 0
    self._cur_y = 0
    self._cur_char = "0"
    
  def checkBounds(self, x_delta, y_delta):
    if self._cur_x + x_delta >= 0:
      self._cur_x += x_delta
      
    if self._cur_x == (self._screen.width - len(self._cur_char)):
      self._cur_x -= 1

    if self._cur_y + y_delta >= 0:
      self._cur_y += y_delta

    if self._cur_y == self._screen.height:
      self._cur_y -= 1
      
    
  def iteration(self):
    # This method is called on every time through the game loop.  In
    # this method, you should check input, determine what the display 
    # should be, and return quickly.

    eval_char = self._input_man.get_input()

    self._screen.screen_refresh()

    if eval_char == 10:
      self._show_title = False

    if eval_char == 113:
      # a 'q' means quit!
      self._should_keep_running = False # TODO: make a helper method for this assignment
    else:
      pass
    
    if eval_char == 258:
      self._cur_char = "\/"
      self.checkBounds(0, 1) # down
    elif eval_char == 259:
      self._cur_char = "/\\"
      self.checkBounds(0, -1) # up
    elif eval_char == 260:
      self._cur_char = "<"
      self.checkBounds(-1, 0) # left
    elif eval_char == 261:
      self._cur_char = ">"
      self.checkBounds(1, 0) # right

    if self._show_title:
      self._screen.screen_clear()
      i = 0
      line_len = 0
      line_height = 0
      for line in self._title_text.splitlines():
        if len(line) > line_len:
          line_len = int(len(line)/2)
        line_height += 1
      for line in self._title_text.splitlines():
       self._screen.add_str(y=int((self._screen.height/2) - int(line_height/2) + i),
			    x=(int(self._screen.width/2) - line_len),
                            output=line)
       i += 1
    elif eval_char is not None:
      self._screen.screen_clear()
      self._screen.add_str(self._cur_y,
			   self._cur_x,
			   self._cur_char)
    
    self._screen.screen_refresh()

  # public - call but do not override!
  def start(self):
    self.run_loop()
        
  def set_active_drawing_context(self, new_context):
    self._drawing_context = new_nontext

  # private - do not touch!
  def run_loop(self):
    self._screen.screen_clear()
    self._screen.screen_refresh()

    while (self._should_keep_running):
      # here is where we call self.iteration() and then redraw the UI
      self.iteration()
      self._rendering_manager.draw()

    self._screen.stop_screen()

if __name__ == '__main__':
  engine = GameEngine()
  engine.start()

