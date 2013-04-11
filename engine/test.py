#!/usr/bin/env python3.0

# engine/test.py
# A generic testing script for the engine.  Modify as much as you want... it's just for testing.

import sys

from DrawableObject import *
from GameEngine import *

print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nTESTING SCRIPT BEGIN\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"



try:
    testObj = DrawableObject()
    testObj.characterMapForDrawingContext(0, 100, 100)
except Exception as ex:
    print "Caught exception: " + str(ex)



# now try a fake GameEngine - this will crash
engine = GameEngine()
engine.start()
