#! /usr/bin/env python3.0

#That was easy! http://docs.python.org/3.1/howto/curses.html
import curses

def startScreen():
	#Draw a screen
	stdscr = curses.initscr()
	
	#Mute echo
	curses.noecho()
	
	#Accept input immediately
	curses.cbreak()
	
	#Translate special keys to regular
	stdscr.keypad(1)
	
	return
	
def stopScreen():
	#Give the user her session back
	curses.endwin()
	return

def screenRefresh():
		stdscr.clear()	
		stdscr.refresh()
		return
		
#------------- Above for things that will be moved to their own display library

def getInput():
	inputChar = 0
	inputArray = []

	while True:
		#Wait ntenths of a second for input
		curses.halfdelay(3)
		#Get the input
		inputChar = stdscr.getch()
		#Get a visual on things
		print(inputChar)
		if c == ord('q'):
			stopScreen()
			break  # Exit the while()
		else:
			screenRefresh()