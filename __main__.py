#! /usr/bin/env python3.0

import os
import sys

while True:
  os.system('clear')
  print('|\n')
  user_option = input("Enter 'Q' to quit.")
  try:
    if user_option.lower() == 'q': # makes everything lowercase so it is easier to handle
      sys.exit("Game Terminated.")
  except TypeError:
    print('What?')