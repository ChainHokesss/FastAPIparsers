from pydantic import BaseSettings


class Config(BaseSettings):
    port: int = 8080
    host: str = '127.0.0.1'
    reload: bool = True

config = Config()