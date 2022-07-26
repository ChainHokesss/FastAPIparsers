from pymongo import MongoClient

from src.config.config import Config


class Mongo:
    def __init__(self, config: Config):
        self._client = MongoClient(config.mongo.host, config.mongo.port)
        self._db = None

    @property
    def db(self):
        return self._client.db
