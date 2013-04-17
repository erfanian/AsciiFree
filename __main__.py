#! /usr/bin/env python3.0

from engine import screenManager
from engine import inputManager

def main():
	#draw the screen and start it
	screenObject = screenManager.Screen()
	screenObject.startScreen()
	
	#get some input
	newInput = inputManager.Input()
	newInput.setUp(screenObject) #pass the screen object so the input can draw to it.
	newInput.run() # start the thread running
	
main()