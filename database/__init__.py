from .db import *

class DB:
    def __init__(self):
        self.blacklist_users = blacklist_users
        self.whitelist_users = whitelist_users
        self.blacklist_words = blacklist_words
        self.whitelist_words = whitelist_words

db = DB()