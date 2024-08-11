from socialnetwork import collect, network, analyze, utils
import argparse
from dotenv import load_dotenv
import os

if __name__ == "__main__":

    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    seed = os.getenv("SEED")
    k = os.getenv("K")
    no_scrape = utils.convert_bool(str(os.getenv("NO_SCRAPE")))
    no_visualize = utils.convert_bool(str(os.getenv("NO_VISUALIZE")))
    no_analyze = utils.convert_bool(str(os.getenv("NO_ANALYZE")))

    if not seed:
        seed = 42
    if not k:
        k = 42

    parser = argparse.ArgumentParser(description="Analyze Instagram follower network.")
    parser.add_argument(
        "--username", type=str, default=username, help="Instagram username"
    )
    parser.add_argument(
        "--password", type=str, default=password, help="Instagram password"
    )
    parser.add_argument("--seed", type=int, default=seed, help="Seed for visualization")
    parser.add_argument("--k", type=int, default=k, help="k value for spring_layout")
    parser.add_argument(
        "--no-scrape",
        action="store_true",
        default=no_scrape,
        help="Do not scrape Instagram followers",
    )
    parser.add_argument(
        "--no-visualize",
        action="store_true",
        default=no_visualize,
        help="Do not generate figures",
    )
    parser.add_argument(
        "--no-analyze",
        action="store_true",
        default=no_analyze,
        help="Do not generate analysis of network",
    )

    args = parser.parse_args()

    print(args)

    if not args.no_scrape:
        print("Scraping Instagram followers...")
        collect.collect(args.password, args.username)
    if not args.no_visualize:
        print("Generating network visualization...")
        network.network(args.seed, args.k)
    if not args.no_analyze:
        print("Analyzing network...")
        analysis = analyze.analyze()
        print(analysis)