# CNS-PROJECT-1# Reinforcement Learning-Based Dynamic Intrusion Detection and Prevention System (DIDPS)

## Overview

This project aims to develop a Reinforcement Learning (RL)-based Dynamic Intrusion Detection and Prevention System (DIDPS) using the Q-learning algorithm. The system is designed to detect and respond to network intrusions in real-time by integrating RL techniques with network simulation environments and a SQLite database.

## Project Structure

- **`main.py`**: The entry point for training the Q-learning agent in the custom network environment.
- **`q_learning_agent.py`**: Contains the implementation of the Q-learning agent.
- **`network_env.py`**: Defines the custom RL environment using OpenAI Gym.
- **`network_data_connector.py`**: Includes functions for interacting with network data and executing actions.
- **`database_setup.py`**: Manages SQLite database setup and data logging.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- SQLite
- Required Python libraries:
  - `numpy`
  - `gym`
  - `requests`
  - `sqlite3` (comes with Python standard library)
  - `tensorflow` or `pytorch` (depending on your RL library)

## Installation

1. **Clone the Repository:**
   ```bash 
   git clone https://github.com/Junekamene/CNS-PROJECT-1
   cd CNS-PROJECT-1
   
