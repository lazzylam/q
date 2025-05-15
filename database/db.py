import json
import os

DB_FILE = "antigcast_db.json"

default_data = {
    "blacklist_users": [],
    "whitelist_users": [],
    "blacklist_words": [],
    "whitelist_words": []
}

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump(default_data, f)

with open(DB_FILE, "r") as f:
    data = json.load(f)

blacklist_users = data["blacklist_users"]
whitelist_users = data["whitelist_users"]
blacklist_words = data["blacklist_words"]
whitelist_words = data["whitelist_words"]

def save_db():
    data = {
        "blacklist_users": blacklist_users,
        "whitelist_users": whitelist_users,
        "blacklist_words": blacklist_words,
        "whitelist_words": whitelist_words
    }
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)
