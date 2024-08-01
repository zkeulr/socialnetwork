from src import collect, cluster, network
import argparse
from dotenv import load_dotenv
import os

if __name__ == "__main__":

    load_dotenv(dotenv_path="vars/.env")

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    seed = os.getenv("SEED")
    k = os.getenv("K")

    if not seed:
        seed = 42
    if not k:
        k = 42

    parser = argparse.ArgumentParser(
        description="Visualize Instagram follower network."
    )
    parser.add_argument(
        "--username", type=str, default=username, help="Instagram username"
    )
    parser.add_argument(
        "--password", type=str, default=password, help="Instagram password"
    )
    parser.add_argument(
        "--seed", type=int, default=seed, help="Seed for visualization"
    )
    parser.add_argument(
        "--k", type=int, default=k, help="k value for spring_layout"
    )

    args = parser.parse_args()

    # collect.collect(args.password, args.username)
    network.network(args.seed, args.k)
    cluster.cluster(args.seed, args.k)
