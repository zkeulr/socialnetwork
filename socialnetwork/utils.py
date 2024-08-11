import json
import os
from datetime import datetime

def convert_bool(string):
        return string.lower() in {"1", "yes", "true", "y"}


def save_connections(
    dict, data_directory="data/connections.json", history_directory="history/"
):
    with open(os.path.join(data_directory, "connections.json"), "w") as f:
        json.dump(dict, f, indent=4)

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(history_directory, f"connections_{timestamp}.json")
    with open(filepath, "w") as f:
        json.dump(dict, f, indent=4)


def load_connections(filename="data/connections.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save(fig, filename, output_directory="output/", history_directory="history/"):
    fig.write_html(os.path.join(output_directory, f"{filename}.html"))
    fig.write_image(
        os.path.join(output_directory, f"{filename}.png"),
        width=1920,
        height=1080,
        scale=2,
    )

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(history_directory, f"{filename}_{timestamp}.html")
    fig.write_html(filepath)
    filepath = os.path.join(history_directory, f"{filename}_{timestamp}.png")
    fig.write_image(filepath, width=1920, height=1080, scale=2)
