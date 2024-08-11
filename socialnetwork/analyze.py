try:
    from . import utils
except ImportError:
    import utils


def analyze():
    followers = utils.load_connections()
    total_followers = len(followers)

    # See who has the most connections
    max = 0
    for follower, connections in followers.items():
        if len(connections) > max:
            max = len(connections)
            max_follower = follower

    # Count posts for each follower

    # Count words in descriptions

    summary = {
        "total_followers": total_followers,
        "max_follower": max_follower,
        "max_connections": max,
    }

    return summary


if __name__ == "__main__":
    summary = analyze()
    print(summary)
