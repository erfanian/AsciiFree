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
## inputManager.py contributors:                                         #
## Eric Erfanian                                                         #
## Chris Cornelius                                                       #
##########################################################################

#http://docs.python.org/3.1/library/queue.html#module-queue
import queue
#http://docs.python.org/3.1/library/threading.html
import threading
import time

class Input (threading.Thread):
	# This class extends threading. Thread so that each object can encapsulate
	# its own thread.  I haven't overridden __init__() because I didn't see
	# the need.  But we basically fall into the main loop when someone tells
	# the object to start().  That loop then waits for characters over and
	# over and over again until it recieves a keypress which tells it to stop
	# OR userQuit gets set to True using the setHalt() method.

	'A generic input class for the game engine to instantiate'
	
	inputChar = 0
	inputEvents = queue.Queue()
	userQuit = False
	screenObject = 0

	def setUp(self, passedScreenObject):
		Input.screenObject = passedScreenObject
		return 
	
	# this is an EXTREMELY unsafe way to quit the
	#     thread.  It doesn't lock in any way, but
	#     it works for now as a demo.
	def setHalt(self):
		self.userQuit = True

	# this method gets called when somebody tells this
	#    object to start() ... all we do here is call
	#    threadMainLoop() which runs until the thread
	#    needs to die.  Then it's done!
	def run(self):
		print("THREAD %s STARTING!" % self.name)

		self.threadMainLoop()

		print( "THREAD %s STOPPING!  Goodbye!" % self.name)
		
		self.screenObject.screenRefresh()
		self.screenObject.stopScreen()

	def threadMainLoop(self):
		# this loop will run until self.userQuit becomes True
		while self.userQuit is not True:
			self.screenObject.stdscr.nodelay(1)

			### get an input character
			inputChar = self.screenObject.stdscr.getch()		#Get the input
			
			### now handle the input
			self.handleInput(inputChar)
			
			### for testing, sleep for 10 msec
			time.sleep(0.01)
			
			self.dumpInput()
			
	# handleInput(inputChar) is called to handle an input
	#    character.  This should only be called inside
	#    threadMainLoop, but it can be called externally
	#    for testing purposes.  Note that this is NOT
	#    synchronized, so if it gets called in two places
	#    at once, you'll have crazy race conditions. 
	def handleInput(self, inputChar):
		if inputChar == 113:
			self.userQuit = True
		elif inputChar == 260:
			self.storeInput(inputChar)
		elif inputChar == 258:		
			self.storeInput(inputChar)
		elif inputChar == 261:
			self.storeInput(inputChar)
		else:
			pass
	
	def storeInput(self, keyPress):
		self.inputEvents.put(keyPress)
		self.inputEvents.task_done()
		return
		
	def dumpInput(self):
		while not self.inputEvents.empty():
			return self.inputEvents.get() #Just change this to return later for the game engine
