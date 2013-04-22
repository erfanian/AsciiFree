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
##########################################################################

#That was easy! http://docs.python.org/3.1/howto/curses.html
import curses

class Screen:
	'A generic screen class for now'
	
	def startScreen(self):
		#global stdscr #Make sure others can access the screen
		self.stdscr = curses.initscr()	#Draw a screen
		curses.noecho()	#Mute echo
		curses.cbreak() 	#Accept input immediately
		self.stdscr.keypad(1) 	#Translate special keys to regular
		print('Starting Screen')
		return
		
	def stopScreen(self):
		#Give the user her session back
		curses.endwin()
		print('Stopping Screen')
		return
	
	def screenRefresh(self):
		self.stdscr.clear()	
		self.stdscr.refresh()
		return
	
	def screenPrint(self):
		print("Hello")