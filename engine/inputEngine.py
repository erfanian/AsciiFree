#! /usr/bin/env python3.0

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
	global inputChar
	global inputEvents
	inputEvents = queue.Queue()

	while True:
		stdscr.nodelay(1)
		inputChar = stdscr.getch()		#Get the input
		if inputChar == ord('q'):
			stopScreen()
			break  # Exit the while()
		elif inputChar == 260:
			print('Left')
			storeInput(inputChar)
		elif inputChar == 258:
			print('Down')
			storeInput(inputChar)
		elif inputChar == 261:
			print('Right')
			storeInput(inputChar)
		else:
			screenRefresh()
			print(inputChar)		#Get a visual on things
			
def storeInput(keyPress):
	inputEvents.put(keyPress)
	return
	
def dumpInput():
	while not inputEvents.empty():
		print(inputEvents.get()) #Just change this to return later for the game engine
	while inputEvents.empty():
		inputEvents.task_done()

startScreen()
getInput()
dumpInput()