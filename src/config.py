from pydantic import BaseSettings


class Config(BaseSettings):
    port: int = 8000
    host: str = '0.0.0.0'
    reload: bool = True


config = Config()
