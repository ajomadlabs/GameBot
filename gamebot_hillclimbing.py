'''-------------------------------------------------------------------------------
	This is a simple CartPole gamebot which uses openai library.This uses a 
	policy called hill climbing policy.In this initially a random weight is 
	given to the weight after which at each iteration the weight is updated
	and the uses the memory to decide the best reward.
-------------------------------------------------------------------------------'''

'''-------------------------------------------------------------------------------
	Importing The Gym and Numpy Module
-------------------------------------------------------------------------------'''

import gym										#Importing the gym module to create the environment
import numpy as np									#Importing the numpy module for calculation purposes

'''----------------------------------------------------------------------------'''

'''-------------------------------------------------------------------------------
	Episode Creation Function
-------------------------------------------------------------------------------'''

def bot_run_episode(envment,parmtrs):							#A function for creating the episode with two parameters, environment and paramtrs where paramtrs are the weights
	observation = envment.reset()							#An observation variable is used for creating the first vset values where the pole should be
	tot_reward = 0									#A variable tot_rewardd is assigned to 0
	for steps in range(200):							#This is a loop for creating the steps
		envment.render()							#This renders the agent that is the CartPole at each step
		action = 0 if np.matmul(parmtrs,observation) < 0 else 1			#This tells the Pole to move left or right based on values if < 0 the left else right
		observation,reward,done,info = envment.step(action)			#This execute the action and returns four variables
		tot_reward += reward							#The tot_reward is added each time with the reward				
		if done:								#If dead/not dead
			break								#If dead breaks the loop
	return tot_reward								#Returns the tot_reward

'''------------------------------------------------------------------------------'''

'''---------------------------------------------------------------------------------
	Training Creation Function 
---------------------------------------------------------------------------------'''


def bot_train(submit):									#A funtion which is used to train the bot
	envment = gym.make('CartPole-v0')						#An environment is created
	
	episode_per_update = 5								#This indicates the number of episodes
	weight_update = 0.1								#This indicates the initial scaling value of the weight

	parmtrs = np.random.rand(4) * 2 -1						#This initialises a random value at first
	bst_reward = 0									#A variable to calclate the best moves 
	
	for episodes in range(2000):							#A loop for creating the episodes
		new_parmtrs = parmtrs + (np.random.rand(4) * 2 -1) * weight_update	#A varible to updates the new weights by adding the previous and multiplying with the scaling value
		reward = bot_run_episode(envment,new_parmtrs)				#A variable which get the tot_reward for each iteration by passing the updated weights
		print("Reward %d Best %d" % (reward, bst_reward))			#Prints the reward and best reward
		if reward > bst_reward:							#Checks if reward is greater or not
			bst_reward = reward						#If greater then that is the best reward
			parmtrs = new_parmtrs						#weights will be the updated weights
			if reward == 200:						#Checking the reward
				break							#Exits the loop

'''--------------------------------------------------------------------------------'''

'''-----------------------------------------------------------------------------------
	Bot Running
------------------------------------------------------------------------------------'''

bot_final = bot_train(submit=False)							#This calls the Trained bot
print(bot_final)									#This prints the best 

'''----------------------------------------------------------------------------------'''
