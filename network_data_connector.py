import requests

def get_network_data():
    # Fetch network data from a given API endpoint
    response = requests.get('http://localhost:8080/network_data')  # Send GET request to the server
    return response.json()  # Parse the response as JSON and return it
def execute_action(action):
    # Send an action to be executed by the network management system
    requests.post('http://localhost:8080/execute_action', json={'action': action})  # Send POST request with the action
