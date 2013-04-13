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

def startScreen():
	global stdscr #Make sure others can access the screen
	stdscr = curses.initscr()	#Draw a screen
	curses.noecho()	#Mute echo
	curses.cbreak() 	#Accept input immediately
	stdscr.keypad(1) 	#Translate special keys to regular
	print('Starting Screen')
	return
	
def stopScreen():
	#Give the user her session back
	curses.endwin()
	print('Stopping Screen')
	return

def screenRefresh():
	stdscr.clear()	
	stdscr.refresh()
	print('Refreshing Screen')
	return
		
#------------- Above for things that will be moved to their own display library


def getInput():
	inputChar = 0
	global inputEvents
	inputEvents = queue.Queue()

	while True:
		stdscr.nodelay(1)
		inputChar = stdscr.getch()		#Get the input
		if inputChar == ord('q'):
			stopScreen()
			try:
				inputEvents.task_done()
			except ValueError:
				print('Nothing happened.') #Handles no user input.
			break  # Exit the while()
		elif inputChar == 260:
			screenRefresh()			
			print('Left')
			storeInput(inputChar)
		elif inputChar == 258:
			screenRefresh()			
			print('Down')
			storeInput(inputChar)
		elif inputChar == 261:
			screenRefresh()
			print('Right')
			storeInput(inputChar)
		else:
			pass
			
def storeInput(keyPress):
	inputEvents.put(keyPress)
	return
	
def dumpInput():
	while not inputEvents.empty():
		print(inputEvents.get()) #Just change this to return later for the game engine

startScreen()
getInputThread = threading.Thread(target=getInput()) #inputThread Object
getInputThread.start() #Start the thread
dumpInputThread = threading.Thread(target=dumpInput()) #dumpThread Object
dumpInputThread.start() #Start the thread