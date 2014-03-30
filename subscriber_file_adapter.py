from subscriber import Subscriber
import os, sqlite3


class Subscriber():
    """docstring for Subscriber"""
    def __init__(self, db_conn, subscriber=None):
        self.db_conn = db_conn
        self.subscriber = subscriber
        self._ensure_table_exists()

    def _ensure_table_exists(self):
        pass

