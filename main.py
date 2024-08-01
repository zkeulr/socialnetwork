from src import collect, visualize, analyze
import argparse
from dotenv import load_dotenv
import os

if __name__ == "__main__":

    load_dotenv(dotenv_path="vars/.env")

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    cookies = None

    parser = argparse.ArgumentParser(
        description="Visualize Instagram follower network."
    )
    parser.add_argument(
        "--username", type=str, default=username, help="Instagram username"
    )
    parser.add_argument(
        "--password", type=str, default=password, help="Instagram password"
    )

    args = parser.parse_args()

    collect.collect(args.password, args.username)
    visualize.visualize()
    analyze.analyze()
