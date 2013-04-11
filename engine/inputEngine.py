#! /usr/bin/env python3.0

#That was easy!
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
	#Don't wait for user input
	stdscr.nodelay(1)
	#Get the input
	c = stdscr.getch()
	#Get a visual on things
	print('Hello')
	if c == ord('q'):
		#Give the user her session back
		curses.endwin()
		break  # Exit the while()
	elif c == curses.KEY_HOME: x = y = 0