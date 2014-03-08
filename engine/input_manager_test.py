"""Tests for input_manager.py"""

import input_manager
import screen_manager
import unittest

class InputManagerTests(unittest.TestCase):

  def setUp(self):
    self.screen = screen_manager.Screen()
    self.input_man = input_manager.Input(self.screen.get_screen())

  def tearDown(self):
    self.screen.stop_screen()

  def testSetHalt(self):
    self.input_man.set_halt()

    self.assertEqual(self.input_man.user_quit, True)

  def testPutInput(self):
    self.input_man.put_input(1)
    self.assertEqual(self.input_man.input_events.qsize(), 1)

  def testGetInput(self):
    self.input_man.put_input(1)
    self.input_man.put_input(2)
    retrieved_val = self.input_man.get_input()

    self.assertEqual(retrieved_val, 1)

if __name__ == '__main__':
  unittest.main()
