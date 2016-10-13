'''------------------------------------------------------------
	This is a simple script that shows us how to create an 
	envionment for the bot to work and how to take a random
	direction at each step
-------------------------------------------------------------'''


'''------------------------------------------------------------
	Importing the gym module from open ai library
-------------------------------------------------------------'''

import gym								#Import gym module for getting the environment

'''-----------------------------------------------------------'''

'''--------------------------------------------------------------
	Creating The Environment
--------------------------------------------------------------'''

env = gym.make('CartPole-v0')						#Making the environment. Here we choose a CartPole environment. This is the region where we are going to train our model
env.reset()								#This indicates that the environment is initialised

'''------------------------------------------------------------'''

'''---------------------------------------------------------------
	Executing The Environment
---------------------------------------------------------------'''

for i in range(1000):							#A loop that continues for 1000 times
	env.render()							#At each iteration the agent will be rendered. Here agent is the CartPole
	env.step(env.action_space.sample())				#This creates a step at each iteration. This means that the agent will take a random direction

'''-------------------------------------------------------------'''

