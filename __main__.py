#! /usr/bin/env python2.0

import os
import sys
#http://www.pygame.org/wiki/about
import pygame

while True:
  os.system('clear')
  print('|\n')
  user_option = raw_input("Enter 'Q' to quit.")
  try:
    if user_option.lower() == 'q': # makes everything lowercase so it is easier to handle
      sys.exit("Game Terminated.")
  except TypeError:
    print('What?')