##########################################################################
## AsciiFree project #####################################################
## An open-source, ASCII-graphics version of SkiFree #####################
## Spring 2013 ###########################################################
## <<LICENSE INFO HERE>>

# Simple Exception subclass which can be raised if a method must be overridden by a subclass

class SubclassMustImplementException (Exception):
    def __init__(self):
        self.value = "Subclasses must implement this method!"

    def __str__(self):
        return self.value

