from socialnetwork import collect, cluster, network, analyze
import argparse
from dotenv import load_dotenv
import os

if __name__ == "__main__":

    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    seed = os.getenv("SEED")
    k = os.getenv("K")
    no_scrape = os.getenv("NO_SCRAPE")

    if not seed:
        seed = 42
    if not k:
        k = 42

    parser = argparse.ArgumentParser(
        description="Analyze Instagram follower network."
    )
    parser.add_argument(
        "--username", type=str, default=username, help="Instagram username"
    )
    parser.add_argument(
        "--password", type=str, default=password, help="Instagram password"
    )
    parser.add_argument("--seed", type=int, default=seed, help="Seed for visualization")
    parser.add_argument("--k", type=int, default=k, help="k value for spring_layout")
    parser.add_argument(
        "--no_scrape",
        type=bool,
        default=no_scrape,
        help="Do not scrape Instagram followers",
    )

    args = parser.parse_args()

    if not args.no_scrape:
        collect.collect(args.password, args.username)
    network.network(args.seed, args.k)
    cluster.cluster(args.seed, args.k)
    analysis = analyze.analyze()
    print(analysis)
