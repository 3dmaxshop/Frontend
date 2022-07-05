from typing import Any
from shop.API.schemas import Model

import httpx


class ModelsApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[dict[str, Any]]:
        response = httpx.get(f'{self.url}/api/v1/models/')
        response.raise_for_status()

        return [Model(**model) for model in response.json()]
