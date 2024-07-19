import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('didps.db')
cursor = conn.cursor()

# Create table for storing network traffic logs
cursor.execute('''
CREATE TABLE IF NOT EXISTS network_traffic (
    id INTEGER PRIMARY KEY,  # Unique identifier for each record
    timestamp TEXT,  # Timestamp of the log entry
    data TEXT  # Data related to network traffic
)
''')

# Create table for storing intrusion alerts
cursor.execute('''
CREATE TABLE IF NOT EXISTS intrusion_alerts (
    id INTEGER PRIMARY KEY,  # Unique identifier for each record
    timestamp TEXT,  # Timestamp of the alert
    alert TEXT  # Details of the intrusion alert
)
''')

# Create table for storing RL training data
cursor.execute('''
CREATE TABLE IF NOT EXISTS rl_training_data (
    id INTEGER PRIMARY KEY,  # Unique identifier for each record
    state INTEGER,  # State during training
    action INTEGER,  # Action taken during training
    reward REAL,  # Reward received during training
    next_state INTEGER  # Next state after taking the action
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
def log_network_traffic(data):
    # Insert network traffic log into the database
    conn = sqlite3.connect('didps.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO network_traffic (timestamp, data) VALUES (CURRENT_TIMESTAMP, ?)', (data,))
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection

def log_intrusion_alert(alert):
    # Insert intrusion alert into the database
    conn = sqlite3.connect('didps.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO intrusion_alerts (timestamp, alert) VALUES (CURRENT_TIMESTAMP, ?)', (alert,))
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection

def log_rl_training_data(state, action, reward, next_state):
    # Insert RL training data into the database
    conn = sqlite3.connect('didps.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rl_training_data (state, action, reward, next_state) VALUES (?, ?, ?, ?)', (state, action, reward, next_state))
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection
