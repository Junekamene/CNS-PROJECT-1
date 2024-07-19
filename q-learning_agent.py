import numpy as np

class QLearningAgent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.99, exploration_rate=1.0, exploration_decay=0.995):
        self.state_size = state_size  # Number of possible states
        self.action_size = action_size  # Number of possible actions
        self.learning_rate = learning_rate  # Rate at which the agent updates the Q-values
        self.discount_factor = discount_factor  # Discount factor for future rewards
        self.exploration_rate = exploration_rate  # Initial exploration rate
        self.exploration_decay = exploration_decay  # Rate at which exploration decreases over time
        self.q_table = np.zeros((state_size, action_size))  # Initialize Q-table with zeros

    def choose_action(self, state):
        # Choose an action based on the exploration-exploitation trade-off
        if np.random.rand() <= self.exploration_rate:  # Explore
            return np.random.randint(self.action_size)  # Choose a random action
        return np.argmax(self.q_table[state])  # Exploit: Choose the action with the highest Q-value

    def learn(self, state, action, reward, next_state):
        # Update Q-values based on the agent's experience
        best_next_action = np.argmax(self.q_table[next_state])  # Find the best action for the next state
        td_target = reward + self.discount_factor * self.q_table[next_state, best_next_action]  # Calculate the target Q-value
        td_error = td_target - self.q_table[state, action]  # Calculate the TD error
        self.q_table[state, action] += self.learning_rate * td_error  # Update Q-value for the current state-action pair
        self.exploration_rate *= self.exploration_decay  # Decay the exploration rate
