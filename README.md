# Blackjack RL

## Overview
This project implements a Blackjack environment and reinforcement learning agents. The goal is to simulate Blackjack game and learn a best policy. In the project, I use Q sheet to track the score of the action under each state. In the end, there is a 10,000 games test, with around 4.2k wins, 5k losses and 0.8k draws. The policy is visualized.

## Structure
- env/: environment
- agent/: agents
- main/: training and visualizing

## How to run
python main.py

## Some comment
I am not a CS student, and this is my first time building a complete Python project from scratch.

Two weeks ago, I was invited to play Blackjack with a friend. I realized that although I wasn't good at the game, there must exist an optimal strategy behind it. That curiosity led me to explore how machines can learn such strategies.

Without relying on auto-completion, I started from zero — writing every line by hand, testing each function, and debugging step by step. After roughly 15 hours of work, I built a working reinforcement learning agent that can play Blackjack better than I can.

This project is more than just code. It represents my first step into understanding how machines learn, make decisions, and improve through experience.

There are many things in this world that I don’t want to miss — and discovering how intelligence emerges from algorithms is one of them.
