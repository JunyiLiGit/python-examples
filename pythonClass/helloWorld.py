# helloWorld.py
# Kacey Coley
# May 10, 2014
# Simple Python class example

import types

class HelloWorld():
    #msg is a variable within the HelloWorld class
    msg = 'Hello World!' 

    #prints the msg variable (assuming a string)
    def greet(self):
        print self.msg

    #override the msg variable (assuming new_msg can be treated as a string)
    def set(self,new_msg):
        #check to see if new_msg is a string
        if isinstance(new_msg, types.StringTypes):
            self.msg = str(new_msg)
        else:
            print "The argument is not a string"
