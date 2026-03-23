from env.blackjack_env import BlackjackEnv
from collections import defaultdict
import numpy as np
import random

class BlackjackAgent:
    def __init__(self):
        self.S = defaultdict(lambda : np.zeros(2)) # here it's equivalent to lambda : [0,0], first argument for standing, second is for hitting. S represent the total score
        self.N = defaultdict(lambda : np.zeros(2)) # so that we can later take the average rewards for each (state, action) pair
        self.Q = defaultdict(lambda : np.zeros(2))
    def choose_action(self, state, epsilon):
        if random.random() < epsilon:
            return random.choice([0,1])
        else:
            return np.argmax(self.Q[state])
    def update_Q(self, episode): # episode describe the course for one single game, in the form of ((state 1), action 1, reward == 0), ... , ((final state), final action, reward == 1/-1/0)
        final_reward = episode[-1][2]
        for (state, action, reward) in episode:
            self.N[state][action] += 1
            self.S[state][action] += final_reward
            self.Q[state][action] = self.S[state][action]/self.N[state][action] # I think can also try calculate the average score at the end of the training, which could save time in training
    def train(self, env, num_episodes):
        start = 0.9
        end = 0.1
        for i in range(num_episodes):
            episode = []
            epsilon = 0.9 - (start - end)/num_episodes*i
            env.reset()
            state = env.state
            terminated = False
            while not terminated:
                action = self.choose_action(state, epsilon)
                next_state, reward, terminated = env.step(action)
                episode.append((state, action, reward))
                state = next_state
            self.update_Q(episode)






            # choose a random state
            # choose a random action
            # check the result and get reward, then update the Q sheet