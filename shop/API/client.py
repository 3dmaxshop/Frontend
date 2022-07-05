from shop.API.models import ModelsApi
from shop.config import config


class ClientAPI:

    def __init__(self, url: str) -> None:
        self.models = ModelsApi(url)


client = ClientAPI(config.backend.url)