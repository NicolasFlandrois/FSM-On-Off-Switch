#!usr/bin/python3
#Author: Nicolas Flandrois
#Date: Fri 07 Jun 2019 09:52:29 CEST 
#Description: Simple binary switch machine, that runs a designated amount of 
#time, using Finite State Machine structure.
from random import randint
from time import clock
##================================
#Finite states definition
State = type("State", (object,), {})

class SwitchOn(State):
	"""SwitchOn"""
	def Execute(State):
		print("Switched On!")
		
class SwitchOff(State):
	"""SwitchOn"""
	def Execute(State):
		print("Switched Off!")
##================================
#Transitions between states
class Transition(object):
	"""Transition runs Transitions between states"""
	def __init__(self, toState):
		self.toState = toState
	def Execute(self):
		print("Transitioning... Please wait....")
##================================
#Finite State Machine
class simpleFSM(object):
	"""simpleFSM is our Finite State Machine script"""
	def __init__(self, char):
		self.char = char
		self.states = {}
		self.transitions = {}
		self.curentState = None
		self.transitionState = None

	def SetState(self, stateName):
		self.curentState = self.states[stateName]

	def Transition(self, transName):
		self.transitionState = self.transitions[transName]

	def Execute(self):
		if (self.transitionState):
			self.transitionState.Execute()
			self.SetState(self.transitionState.toState)
			self.transitionState = None
		self.curentState.Execute()
##================================
#Character class holding attributes, or properties: Here a Lightbulbe's switch.
class Char(object):
	"""Character class holding attributes, or properties: Here a Lightbulbe's 
	switch."""
	def __init__(self):
		self.FSM = simpleFSM(self)
		self.SwitchOn = True
##================================
#Run engin Main/Manage/Control
if __name__=="__main__":
	switch = Char()

	switch.FSM.states["On"] = SwitchOn()
	switch.FSM.states["Off"] = SwitchOff()
	switch.FSM.transitions["toOn"] = Transition("On")
	switch.FSM.transitions["toOff"] = Transition("Off")

	switch.FSM.SetState("On") #Initial State defined here.

	#Program that actually run through and connect the dots (Manage or Control).
	for i in range(20): 
	#Change to range(n) with int(input()) methode, to ask how many times to flip the switch.
		startTime = clock()
		timeInterval = 1
		while (startTime + timeInterval > clock()):
			pass
		if (randint(0, 2)):
			if (switch.SwitchOn):
				switch.FSM.Transition("toOff")
				switch.SwitchOn = False
			else:
				switch.FSM.Transition("toOn")
				switch.SwitchOn = True
		switch.FSM.Execute()