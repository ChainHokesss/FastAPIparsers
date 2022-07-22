from pydantic import BaseSettings


CONFIG_PREFIX = 'FASTAPI_SERVICE_'


class Service(BaseSettings):
    port: int
    host: str
    reload: bool = True

    class Config:
        env_prefix = CONFIG_PREFIX
        env_file = '.env'

class Mongo(BaseSettings):
    username: str
    password: str

    class Config:
        env_prefix = CONFIG_PREFIX + "MONGO_"
        env_file = '.env'

class Config:
    service: Service = Service()
    mongo: Mongo = Mongo
