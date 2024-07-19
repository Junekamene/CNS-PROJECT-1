# main.py

import gym  # Import the gym library for reinforcement learning environments
from network_env import NetworkEnv  # Import the custom network environment
from q_learning_agent import QLearningAgent  # Import the Q-learning agent implementation
from network_data_connector import get_network_data, execute_action  # Import functions for interacting with network data
import sqlite3  # Import the SQLite library for database interactions
import numpy as np  # Import NumPy for numerical operations

def train_rl_agent(episodes=1000, max_steps=100):
    """
    Function to train the Q-learning agent in the custom network environment.
    
    :param episodes: Number of episodes for training
    :param max_steps: Maximum number of steps per episode
    """
    # Initialize the environment and agent
    env = NetworkEnv()  # Create an instance of the custom network environment
    state_size = env.observation_space.n  # Get the number of possible states from the environment
    action_size = env.action_space.n  # Get the number of possible actions from the environment
    agent = QLearningAgent(state_size, action_size)  # Create an instance of the Q-learning agent
    
    for episode in range(episodes):
        state = env.reset()  # Reset the environment to the initial state for a new episode
        total_reward = 0  # Initialize the total reward for the current episode
        
        for step in range(max_steps):
            action = agent.choose_action(state)  # Choose an action based on the current state
            next_state, reward, done, _ = env.step(action)  # Apply the action and get the next state, reward, and done flag
            agent.learn(state, action, reward, next_state)  # Update the Q-values based on the agent’s experience
            total_reward += reward  # Accumulate the reward for the current episode
            state = next_state  # Update the current state
            
            if done:
                break  # Exit the loop if the episode is done
        
        # Log the results of the current episode
        print(f"Episode {episode + 1}/{episodes} - Total Reward: {total_reward}")
        
        # Optionally, you can log additional information here, such as to a database or file

if __name__ == "__main__":
    train_rl_agent()  # Call the training function when the script is executed
