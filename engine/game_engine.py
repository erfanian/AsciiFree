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
    self._screen_manager = ascii_rendering_manager.AsciiRenderingManager(screen_manager.Screen())
    self._input_man = input_manager.Input(self._screen_manager._screen.get_screen())
    self._input_man.start()
    self._should_keep_running = True
    self._show_title = True


  def iteration(self):
    # This method is called on every time through the game loop.  In
    # this method, you should check input, determine what the display 
    # should be, and return quickly.

    eval_char = self._input_man.get_input()

    self._screen_manager.screen_refresh()

    if eval_char == 10 and self._show_title:
      self._show_title = False
      self._screen_manager._drawable_objects.pop("start_screen")

    if eval_char == 113:
      # a 'q' means quit!
      self._should_keep_running = False # TODO: make a helper method for this assignment
    else:
      pass
    
    if not self._show_title:
      if eval_char == 258:
        self._screen_manager.set_object_payload("cursor", "\/")
        self._screen_manager.checkBounds(0, 1) # down
      elif eval_char == 259:
        self._screen_manager.set_object_payload("cursor", "/\\")
        self._screen_manager.checkBounds(0, -1) # up
      elif eval_char == 260:
        self._screen_manager.set_object_payload("cursor", "<")
        self._screen_manager.checkBounds(-1, 0) # left
      elif eval_char == 261:
        self._screen_manager.set_object_payload("cursor", ">")
        self._screen_manager.checkBounds(1, 0) # right

    if self._show_title:
      self._screen_manager.screen_clear()
      self._screen_manager.draw()

    elif eval_char is not None:
      self._screen_manager.screen_clear()
      self._screen_manager.draw()
    
    self._screen_manager.screen_refresh()

  # public - call but do not override!
  def start(self):
    self.run_loop()
        
  def set_active_drawing_context(self, new_context):
    self._drawing_context = new_nontext

  # private - do not touch!
  def run_loop(self):
    self._screen_manager.screen_clear()
    self._screen_manager.screen_refresh()

    while (self._should_keep_running):
      # here is where we call self.iteration() and then redraw the UI
      self.iteration()
      self._screen_manager.draw()

    self._screen_manager.stop_screen()

if __name__ == '__main__':
  engine = GameEngine()
  engine.start()

