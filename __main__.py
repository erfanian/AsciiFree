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
## __main__.py contributors:                                             #
## Eric Erfanian                                                         #
##########################################################################

from engine import screenManager
from engine import inputManager

def renderInput():
	if newInput.dumpInput() == 260:
		screenObject.screenPrint()
	else:
		pass

def main():
	#draw the screen and start it
	screenObject = screenManager.Screen()
	screenObject.startScreen()
	
	#get some input
	newInput = inputManager.Input()
	newInput.setUp(screenObject) #pass the screen object so the input can draw to it.
	newInput.run() # start the thread running
	
	while newInput.userQuit is not True:
		self.renderInput()
	
main()