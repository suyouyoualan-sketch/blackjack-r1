from env.blackjack_env import BlackjackEnv
from agent.agent import BlackjackAgent

import matplotlib.pyplot as plt
import numpy as np

env = BlackjackEnv()
agent = BlackjackAgent()

agent.train(env,5000000)


def test(agent, env, num_episodes):
    wins = 0
    draws = 0
    losses = 0

    for i in range(num_episodes):
        env.reset()
        state = env.state
        terminated = False

        while not terminated:
            action = agent.choose_action(state, epsilon=0)
            next_state, reward, terminated = env.step(action)
            state = next_state

        if reward == 1:
            wins += 1
        elif reward == 0:
            draws += 1
        else:
            losses += 1

    print("win: ", wins)
    print("draws: ", draws)
    print("losses: ", losses)

test(agent, env, 10000)



ace_counts = set()
for state in agent.Q:
    ace_counts.add(state[2])
print(sorted(ace_counts))

def plot_policy(agent):
    ace_values = [0, 1, 2]
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for idx, ace in enumerate(ace_values):
        policy = np.zeros((10, 10))
        for player in range(12, 22):
            for dealer in range(2, 12):
                state = (player, dealer, ace)
                if state in agent.Q:
                    action = np.argmax(agent.Q[state])
                    policy[player-12][dealer-2] = action

        im = axes[idx].imshow(policy, cmap='RdBu', aspect='auto', vmin=0, vmax=1)
        axes[idx].set_xlabel('Dealer showing')
        axes[idx].set_ylabel('Player sum')
        axes[idx].set_xticks(range(10))
        axes[idx].set_xticklabels(range(2, 12))
        axes[idx].set_yticks(range(10))
        axes[idx].set_yticklabels(range(12, 22))
        axes[idx].set_title(f'Ace count = {ace}')

    fig.colorbar(im, ax=axes.tolist(), label='0=Stand  1=Hit')
    plt.suptitle('Blackjack Policy', fontsize=16)
    plt.savefig('policy.png', dpi=150, bbox_inches='tight')
    plt.show()


plot_policy(agent)

