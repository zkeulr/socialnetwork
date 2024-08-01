from tqdm import tqdm
import instaloader
import json


def collect(username, password):
    L = instaloader.Instaloader()

    try:
        L.load_session_from_file(username=username, filename="vars/session_file")
    except:
        login(L, username, password)

    profile = instaloader.Profile.from_username(L.context, "zkeulr")
    followers = get_followers(profile)

    analyzed_data = load_analyzed_data().copy()
    analyzed_data.popitem()
    common = {}

    try:
        for username in tqdm(
            followers, desc="Find connected followers", total=len(followers) - len(analyzed_data)
        ):
            if username in analyzed_data:
                continue

            follower = instaloader.Profile.from_username(L.context, username)
            subfollowers = get_followers(follower)
            common_followers = list(set(followers).intersection(set(subfollowers)))
            common[follower] = common_followers
    except Exception as e:
        print(e)
        print(f"The last follower added was {username}")

    save(common)


def load_analyzed_data(filename="vars/connections.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def login(L, username, password):
    try:
        L.login(username, password)
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        two_factor_code = input("Enter 2FA code sent to your device: ")
        L.two_factor_login(two_factor_code)

    L.save_session_to_file(filename="vars/session_file")


def get_followers(profile):
    return [follower.username for follower in profile.get_followers()]


def save(dict, filename="vars/connections.json"):
    with open(filename, "w") as f:
        json.dump(dict, f)
