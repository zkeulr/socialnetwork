from src import collect, visualize
import argparse
from dotenv import load_dotenv
import logging
import os


if __name__ == "__main__":

    load_dotenv(dotenv_path="vars/.env")

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    parser = argparse.ArgumentParser(description="Visualize Instagram followers.")
    parser.add_argument(
        "--username", type=str, default=username, help="Instagram username"
    )
    parser.add_argument(
        "--password", type=str, default=password, help="Instagram password"
    )

    args = parser.parse_args()

    collect.collect(username, password)
    visualize.visualize()
