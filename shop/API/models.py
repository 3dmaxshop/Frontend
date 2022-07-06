import httpx
import orjson

from shop.api.schemas import Model


class ModelsApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[Model]:
        response = httpx.get(f'{self.url}/api/v1/models/')
        response.raise_for_status()

        return [Model(**model) for model in response.json()]

    def delete(self, uid):
        response = httpx.delete(f'{self.url}/api/v1/models/{uid}')
        response.raise_for_status()

    def change(self, model):
        model = Model(**model)
        dict_model = model.dict()
        json_model = orjson.dumps(dict_model)
        headers = {
            'Content-Type': 'application/json',
        }
        response = httpx.put(f'{self.url}/api/v1/models/', content=json_model, headers=headers)
        response.raise_for_status()

    def add(self, model):
        model = Model(**model)
        dict_model = model.dict()
        json_model = orjson.dumps(dict_model)
        headers = {
            'Content-Type': 'application/json',
        }
        response = httpx.post(f'{self.url}/api/v1/models/', content=json_model, headers=headers)
        response.raise_for_status()
