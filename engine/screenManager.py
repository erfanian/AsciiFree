 #! /usr/bin/env python3.0
##########################################################################
## AsciiFree project #####################################################
## An open-source, ASCII-graphics version of SkiFree #####################
## Spring 2013 ###########################################################
##########################################################################
## This work is licensed under the #######################################
## Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) ####################
## You can find the full license here: ###################################
## http://creativecommons.org/licenses/by-sa/3.0/deed.en_US ##############
##########################################################################
## inputEngine.py contributors: ##########################################
## Eric Erfanian #########################################################
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

#screenObject = Screen()
#screenObject.startScreen()