import os
from dataclasses import dataclass


@dataclass
class ServerConf:
    host: str
    port: int


@dataclass
class BackendConf:
    url: str


@dataclass
class Config:
    backend: BackendConf
    server: ServerConf


def load() -> Config:
    return Config(
        backend=BackendConf(url=os.environ['BACKEND_URL']),
        server=ServerConf(
            host=os.environ['APP_HOST'],
            port=int(os.environ['APP_PORT']),
        ),
    )


config = load()