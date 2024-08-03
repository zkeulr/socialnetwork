from collections import Counter
import re
import utils


def analyze():
    followers = utils.load_connections()
    total_followers = len(followers)

    # See who has the most connections

    # Count posts for each follower

    # Count words in descriptions

    summary = {"total_followers": total_followers}

    return summary


if __name__ == "__main__":
    summary = analyze()
    print(summary)
