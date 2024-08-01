import json

def visualize():
    data = load_data

def load_data(filename="vars/connections.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
