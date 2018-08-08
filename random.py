#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 01:45:39 2018

@author: jason
"""

from __future__ import print_function, division
from builtins import range

import gym
import gym.spaces
import gym.wrappers
import numpy as np
import matplotlib.pyplot as plt

from gym import wrappers
# this is for recording video

def get_action(s,w):
    #s for state, w for weights
    return 1 if np.dot(s,w) > 0 else 0

def play_one_episode(env, params):
    observation = env.reset()
    done = False
    t = 0 
    
    while not done and t < 10000:
        #env.render()
        
        t += 1
        action = get_action(observation, params)
        observation, reward, done, info = env.step(action)
        if done: 
            break
    
    return t

def play_multiple_episodes(env, T, params):
    episode_lengths = np.empty(T)
    # np.empty(shape, type = float) Return a new array of given shape and type, without initializing entries.
    
    for i in range(T):
        episode_lengths[i] = play_one_episode(env, params)
        
    avg_length = episode_lengths.mean()
    #print("avg length:", avg_length)
    return avg_length
# this will give the average length of T episodes
    
def random_search(env):
    episode_lengths = []
    best = 0 
    params = None
    for t in xrange(100):
        new_params = np.random.random(4)*2 - 1
        #np.random.random(4) generates 4 numbers float between 0 and 1.  *2-1 gives negative value as well.  
        avg_length = play_multiple_episodes(env, 100, new_params)
        episode_lengths.append(avg_length)
        
        if avg_length > best:
            params = new_params
            best = avg_length
            print('Best avg length: ', best, 'at episode:', (t+1)* 100)
            
        if best > 195.0: 
            print('Solved! at', (t+1) * 100, 'episode')
            break
    #we want to keep the parameters from best performance. 
    return episode_lengths, params

if __name__ == '__main__':
    env = gym.make('CartPole-v0')
    #env.render()
    env = wrappers.Monitor(env, 'video', force = True)
    episode_lengths, params = random_search(env)
    plt.plot(episode_lengths)
    plt.show()
    print('***Final run with best weights***')   
    
    observation = env.reset()
    done = False
    total_reward = 0 
    for i in range(300):
        env.render()
        action = get_action(observation, params)
        observation, reward, done, info = env.step(action)
        total_reward = total_reward + reward
        if done: 
            break

    env.close()
    print(total_reward) 
    