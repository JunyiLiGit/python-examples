#!/usr/bin/python
import helloWorld as hello

#Create an instance of HelloWorld
hi = hello.HelloWorld()
#Call the greet function
hi.greet()
#Override the greeting
hi.set("Hello Again!")
#Call the greet function again
hi.greet()
