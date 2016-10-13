'''--------------------------------------------------------------------------
	Importing The Gym Module
--------------------------------------------------------------------------'''

import gym									#Importing the gym module for creating the evironment

'''-----------------------------------------------------------------------'''

'''--------------------------------------------------------------------------
	Creating The Environment
--------------------------------------------------------------------------'''
	
envment = gym.make('CartPole-v0')						#Creating the CartPole environment and assigning it to the envment variable

'''-----------------------------------------------------------------------'''

'''--------------------------------------------------------------------------
	Running The Environment
--------------------------------------------------------------------------'''

for n_episode in range(20):							#A loop that is used for creating the episodes. Episodes are nothing but they are the ones after which the pole falls of
	observation = envment.reset()						#Here the envment is reseted and assigned to a observation variable
	for n_steps in range(100):						#A loop which is for creating the steps.Steps are the ones which is used for taking random directions
		envment.render()						#This is used for rendering the agent at each step
		print(observation)						#This prints the observation.Observation will be a list of velocities that the CartPole moves 
		action = envment.action_space.sample()				#This takes the random movements for the CartPole
		observation,reward,done,info = envment.step(action)		#Here the step takes the action and returns four values observation:-velocities		
		if done:							#This means if the CartPole has died or not.
			print("Episode is finished ")				#This statement prints Episode is Finished if the CartPole is dead
			break							#This breaks the loop if the CartPole is dead and starts with the next episode

'''------------------------------------------------------------------------'''
