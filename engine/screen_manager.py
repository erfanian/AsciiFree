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
## screenManager.py contributors:                                        #
## Eric Erfanian                                                         #
## Chris Cornelius                                                       #
##########################################################################

import curses
import logging

logger = logging.getLogger(__name__)

class Screen(object):
  'A generic screen class for now'

  def __init__(self):
    logging.info('Starting screen.')
    self._stdscr = curses.initscr()	#Draw a screen
    curses.noecho()	        #Mute echo
    curses.cbreak() 	#Accept input immediately
    self._stdscr.keypad(1) 	#Translate special keys to regular
    curses.curs_set(0) # cursor visibility
    self.width = curses.COLS
    self.height = curses.LINES

  def get_screen(self):
    """A method to return this object's screen."""

    return self._stdscr

  def move(self, x, y):
    self._stdscr.move(x, y)
	
  def add_str(self, y=0, x=0, output=None):
    self._stdscr.addstr(y, x, output, curses.A_NORMAL)

		
  def stop_screen(self):
    # Give the user her session back - make sure to return to the default echoing parameters.
    curses.nocbreak()
    self._stdscr.keypad(0)
    curses.echo()
    curses.endwin()
    logging.info('Stopped curses module.')
    	
  def screen_refresh(self):
    self._stdscr.refresh()

  def screen_clear(self):
    self._stdscr.clear()
