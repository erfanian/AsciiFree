import unittest
import inputManager
 
class inputTests(unittest.TestCase):
	
	def testLeft(self):
		newInput = inputManager.Input()
		newInput.getInput(260)
		newInput.getInput(113)
		self.assertEqual(newInput.dumpInput(), 260, 'I cannot go left')
		
	def testDown(self):
		newInput = inputManager.Input()
		newInput.getInput(258)
		newInput.getInput(113)
		self.assertEqual(newInput.dumpInput(), 258, 'I cannot go down')
		
	def testRight(self):
		newInput = inputManager.Input()
		newInput.getInput(261)
		newInput.getInput(113)
		self.assertEqual(newInput.dumpInput(), 261, 'I cannot go right')
		
	def testQuit(self):
		newInput = inputManager.Input()
		self.assertEqual(False, newInput.getInput(113), 'I cannot stop collecting input')
	
if __name__ == '__main__':
	unittest.main()