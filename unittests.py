import unittest
import time
from engine import screenManager
from engine import inputManager
 
class inputTests(unittest.TestCase):
	
	def testQuit(self):
		newInput = inputManager.Input(name='testQuitInputManager')
		newInput.start() # start the thread running
		newInput.handleInput(113) # tell the thread to quit
		time.sleep(0.1) # wait for the thread to die
		self.assertEqual(False, newInput.is_alive(), 'Thread still alive after it was told to quit!')


	def testHalt(self):
		newInput = inputManager.Input(name='testHaltInputManager')
		newInput.start() # start the thread running
		
		# manually kill the thread - note that this ISNT
		# synchronized right now, so we need to do a
		# longer wait after we send this signal:
		newInput.setHalt() 
		time.sleep(0.1)

		self.assertEqual(False, newInput.is_alive(), 'Thread still alive after it was told to quit!')

	def testLeft(self):
		newInput = inputManager.Input(name='testLeftInputManager')
		newInput.start() # start the thread running
		newInput.handleInput(260)
		newInput.handleInput(113) # tell the thread to quit
		self.assertEqual(newInput.dumpInput(), 260, 'I cannot go left')
		
	def testDown(self):
		newInput = inputManager.Input(name='testDownInputManager')
		newInput.start() # start the thread running
		newInput.handleInput(258)
		newInput.handleInput(113) # tell the thread to quit
		self.assertEqual(newInput.dumpInput(), 258, 'I cannot go down')
		
	def testRight(self):
		newInput = inputManager.Input(name='testRightInputManager')
		newInput.start() # start the thread running
		newInput.handleInput(261)
		newInput.handleInput(113) # tell the thread to quit
		self.assertEqual(newInput.dumpInput(), 261, 'I cannot go right')
	
if __name__ == '__main__':
	unittest.main()
