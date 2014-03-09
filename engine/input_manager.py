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
## inputManager.py contributors:                                         #
## Eric Erfanian                                                         #
## Chris Cornelius                                                       #
##########################################################################

import logging
import queue
import threading
import time

logger = logging.getLogger(__name__)

class Input (threading.Thread):

  def __init__(self, screen_object=None):
    """The internal init function.

    Args:
      screen_object: (curses.initscr()) A curses screen.
    """
    super(Input, self).__init__()
    self.input_char = None
    self.input_events = queue.Queue()
    self.user_quit = False
    self.screen_object = screen_object 
    self.name = "InputManager"
    self.lock = threading.Lock()

  def set_halt(self):
    """Flips a bit to indicate the user would like to quit."""
    self.user_quit = True

  def run(self):
    """The internal function that is run when the thread is started."""
    logging.info("THREAD %s STARTING!", self.name)

    self.thread_main_loop()

    logging.info("THREAD %s STOPPING! Goodbye!", self.name)
	

  def thread_main_loop(self):
    """The main loop that is called when the thread is run()."""
    while self.user_quit is not True:

      # Get a character of input
      self.input_char = self.screen_object.getch()

      if self.lock.acquire(True):
        self.put_input(self.input_char)
        self.lock.release()
		
  def put_input(self, input_char):
    """A method to store input from the buffer into a queue object.

    Args:
      input_char: An input character from the screen_object.
    """
    # Quit on escape character.
    if input_char == 113:
      self.user_quit = True

    self.input_events.put(input_char)
	
  def get_input(self):
    """A method to return input from the FIFO queue.

    Returns:
      return_cal: (string) A character from the input queue.
    """
    return_val = None
	
    try:
      return_val = self.input_events.get(block=False)
    except queue.Empty as e:
      pass

    return return_val

