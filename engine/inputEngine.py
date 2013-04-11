#! /usr/bin/env python3.0

#That was easy! http://docs.python.org/3.1/howto/curses.html
import curses

#Draw a screen
stdscr = curses.initscr()

#Mute echo
curses.noecho()

#Accept input immediately
curses.cbreak()

#Translate special keys to regular
stdscr.keypad(1)

while True:
	#Wait ntenths of a second for input
	curses.halfdelay(3)
	#Get the input
	c = stdscr.getch()
	#Get a visual on things
	stdscr.clear()	
	stdscr.refresh()	
	print(c)
	if c == ord('q'):
		#Give the user her session back
		curses.endwin()
		break  # Exit the while()
	elif c == curses.KEY_HOME: x = y = 0