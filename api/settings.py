from pydantic import BaseSettings, BaseConfig


class Settings(BaseSettings):
    host: str
    port: int

    class Config(BaseConfig):
        env_file = '.env'
