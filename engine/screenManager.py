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

#That was easy! http://docs.python.org/3.1/howto/curses.html
import curses

class Screen:
	'A generic screen class for now'
	
	_stdscr = None

	def startScreen(self):
		#global stdscr #Make sure others can access the screen
		print('Screen: starting screen...')
		self._stdscr = curses.initscr()	#Draw a screen
		curses.noecho()	        #Mute echo
		curses.cbreak() 	#Accept input immediately
		self._stdscr.keypad(1) 	#Translate special keys to regular

		# just for fun: RAVE MODE!!!
		# caution: only enable this for fun.
		# self._stdscr.bkgd(35,curses.A_BLINK)

		return

	def move(self, x, y):
		self._stdscr.move(x, y)
	
	def addstr(self, string):
		self._stdscr.addstr(string, curses.A_NORMAL)

		
	def stopScreen(self):
		# Give the user her session back - make sure to return to the default echoing parameters.
		curses.nocbreak()
		self._stdscr.keypad(0)
		curses.echo()
		curses.endwin()
		print('Screen: stopped curses module')
		return
	
	def screenRefresh(self):
		self._stdscr.refresh()
		return
