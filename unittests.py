import unittest
import time
from engine import screenManager
from engine import inputManager


class inputTests(unittest.TestCase):
	
	def setUp(self):
		global screenObject #TODO find a better way to pass this to the unittests	
		screenObject = screenManager.Screen()
		screenObject.startScreen()

# We don't need to clean up because the quit input cleans this up already.		
#	def tearDown(self):
#		screenObject.stopScreen()
	
	def testQuit(self):
		newInput = inputManager.Input(name='testQuitInputManager')
		newInput.setUp(screenObject)
		newInput.start() # start the thread running
		newInput.handleInput(113) # tell the thread to quit
		time.sleep(0.1) # wait for the thread to die
		self.assertEqual(False, newInput.is_alive(), 'Thread still alive after it was told to quit!')
	
	def testHalt(self):
		newInput = inputManager.Input(name='testHaltInputManager')
		newInput.setUp(screenObject)
		newInput.start() # start the thread running
		
		# manually kill the thread - note that this ISNT
		# synchronized right now, so we need to do a
		# longer wait after we send this signal:
		newInput.setHalt()
		time.sleep(0.1)
		self.assertEqual(False, newInput.is_alive(), 'Thread still alive after it was told to quit!')
	
	
	def testLeft(self):
		newInput = inputManager.Input(name='testLeftInputManager')
		newInput.setUp(screenObject)
		newInput.start() # start the thread running
		newInput.handleInput(260)
		newInput.handleInput(113) # tell the thread to quit
		self.assertEqual(newInput.dumpInput(), 260, 'I cannot go left')

	
	def testDown(self):
		newInput = inputManager.Input(name='testDownInputManager')
		newInput.setUp(screenObject)
		newInput.start() # start the thread running
		newInput.handleInput(258)
		newInput.handleInput(113) # tell the thread to quit
		self.assertEqual(newInput.dumpInput(), 258, 'I cannot go down')
	
	
	def testRight(self):
		newInput = inputManager.Input(name='testRightInputManager')
		newInput.setUp(screenObject)
		newInput.start() # start the thread running
		newInput.handleInput(261)
		newInput.handleInput(113) # tell the thread to quit
		self.assertEqual(newInput.dumpInput(), 261, 'I cannot go right')

	#TODO Test for no input

if __name__ == '__main__':
    unittest.main()
