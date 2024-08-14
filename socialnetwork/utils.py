import json
import os
from datetime import datetime
from argparse import ArgumentParser
from glob import glob
from os.path import expanduser
from platform import system
from sqlite3 import OperationalError, connect

try:
    from instaloader import ConnectionException, Instaloader
except ModuleNotFoundError:
    raise SystemExit("Instaloader not found.\n  pip install [--user] instaloader")


def get_cookiefile():
    default_cookiefile = {
        "Windows": "~/AppData/Roaming/Mozilla/Firefox/Profiles/*/cookies.sqlite",
        "Darwin": "~/Library/Application Support/Firefox/Profiles/*/cookies.sqlite",
    }.get(system(), "~/.mozilla/firefox/*/cookies.sqlite")
    cookiefiles = glob(expanduser(default_cookiefile))
    if not cookiefiles:
        raise SystemExit("No Firefox cookies.sqlite file found. Use -c COOKIEFILE.")
    return cookiefiles[0]


def import_session(cookiefile, sessionfile):
    print("Using cookies from {}.".format(cookiefile))
    conn = connect(f"file:{cookiefile}?immutable=1", uri=True)
    try:
        cookie_data = conn.execute(
            "SELECT name, value FROM moz_cookies WHERE baseDomain='instagram.com'"
        )
    except OperationalError:
        cookie_data = conn.execute(
            "SELECT name, value FROM moz_cookies WHERE host LIKE '%instagram.com'"
        )
    instaloader = Instaloader(max_connection_attempts=1)
    instaloader.context._session.cookies.update(cookie_data)
    username = instaloader.test_login()
    if not username:
        raise SystemExit("Not logged in. Are you logged in successfully in Firefox?")
    print("Imported session cookie for {}.".format(username))
    instaloader.context.username = username
    instaloader.save_session_to_file(sessionfile)


def collect_cookies():
    p = ArgumentParser()
    p.add_argument("-c", "--cookiefile")
    args = p.parse_args()
    try:
        import_session(
            args.cookiefile or get_cookiefile(), "socialnetwork/session_file"
        )
    except (ConnectionException, OperationalError) as e:
        raise SystemExit("Cookie import failed: {}".format(e))


def convert_bool(string):
    return string.lower() in {"1", "yes", "true", "y"}


def save_connections(dict, data_directory="data/", history_directory="history/"):
    filepath = os.path.join(data_directory, "connections.json")
    dict.update(load_connections(filepath))

    write_json(filepath, dict)

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(history_directory, f"connections_{timestamp}.json")
    write_json(filepath, dict)


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def load_connections(filepath="data/connections.json"):
    if not os.path.exists(filepath):
        return {}
    if os.path.getsize(filepath) == 0:
        return {}
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
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


if __name__ == "__main__":
    collect_cookies()
