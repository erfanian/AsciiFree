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
#http://docs.python.org/3.1/library/queue.html#module-queue
import queue
#http://docs.python.org/3.1/library/threading.html
import threading

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

#dummyScreen = Screen()
#dummyScreen.startScreen()
		
#------------- Above for things that will be moved to their own display library

class Input:
	'A generic input class for the game engine to instantiate'
	
	inputChar = 0
	inputEvents = queue.Queue()
	userQuit = False

	def getInput(self, inputChar):

		while self.userQuit is not True:
	#			screenObject.stdscr.nodelay(1)
	#			inputChar = screenObject.stdscr.getch()		#Get the input
			if inputChar == 113:
	#				dummyScreen.stopScreen()
				self.userQuit = True
			elif inputChar == 260:
	#				dummyScreen.screenRefresh()			
				self.storeInput(inputChar)
			elif inputChar == 258:
	#				dummyScreen.screenRefresh()			
				self.storeInput(inputChar)
			elif inputChar == 261:
	#				dummyScreen.screenRefresh()
				self.storeInput(inputChar)
			else:
				pass
			
		return False
				
	def storeInput(self, keyPress):
		Input.inputEvents.put(keyPress)
		Input.inputEvents.task_done()
		return
		
	def dumpInput(self):
		while not Input.inputEvents.empty():
			return Input.inputEvents.get() #Just change this to return later for the game engine


#dummyInput = Input()

#getInputThread = threading.Thread(target=dummyInput.getInput()) #inputThread Object
#dumpInputThread = threading.Thread(target=dummyInput.dumpInput()) #dumpThread Object
#getInputThread.start() #Start the thread
#dumpInputThread.start() #Start the thread