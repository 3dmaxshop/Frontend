from shop.api.categories import CategoriesApi
from shop.api.models import ModelsApi
from shop.config import config


class ClientAPI:

    def __init__(self, url: str) -> None:
        self.models = ModelsApi(url)
        self.categories = CategoriesApi(url)


client = ClientAPI(config.backend.url)
