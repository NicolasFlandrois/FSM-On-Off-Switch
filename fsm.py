#!usr/bin/python3
#Author: Nicolas Flandrois
#Date: Fri 07 Jun 2019 09:52:29 CEST 
#Description:
from random import randint
from time import clock
##================================
#Finite states definition
State = type("State", (object,), {})

class SwitchOn(State):
	"""docstring for SwitchOn"""
	def Execute(State):
		print("Switched On!")
		
class SwitchOff(State):
	"""docstring for SwitchOn"""
	def Execute(State):
		print("Switched Off!")
##================================
#Transitions between states
class Transition(object):
	"""docstring for Transition"""
	def __init__(self, toState):
		self.toState = toState
	def Execute(self):
		print("Transitioning... Please wait....")
##================================
#Finite State Machine
class simpleFSM(object):
	"""docstring for simpleFSM"""
	def __init__(self, char):
		self.char = char
		self.states = {}
		self.transitions = {}
		self.curentState = None
		self.transitionMove = None

	def SetState(self, stateName):
		self.curentState = self.states[stateName]