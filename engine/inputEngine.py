#! /usr/bin/env python3.0

#That was easy! http://docs.python.org/3.1/howto/curses.html
import curses

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
	global inputList
	inputList = []

	while True:
		curses.halfdelay(3)		#Wait ntenths of a second for input
		inputChar = stdscr.getch()		#Get the input
		if inputChar == ord('q'):
			stopScreen()
			break  # Exit the while()
		elif inputChar == 260:
			print('Left')
			storeInput()
		elif inputChar == 258:
			print('Down')
			storeInput()
		elif inputChar == 261:
			print('Right')
			storeInput()
		else:
			screenRefresh()
			print(inputChar)		#Get a visual on things
			
def storeInput():
	inputList.append(inputChar)
	return
	
def dumpInput():
	for i in inputList:
		print(i) #Just change this to return later for the game engine
	inputList[:] = [] #Clear the input list

startScreen()
getInput()
dumpInput()